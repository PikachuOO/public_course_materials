#!/usr/bin/python3.5

import datetime, glob, html, json, os, re, subprocess, traceback
from collections import defaultdict, OrderedDict

from flask import Flask, render_template, request, abort, send_file
from werkzeug.routing import BaseConverter
from bs4 import BeautifulSoup


# config.variables contains appropriate pathnames for this course & session
import config

app = Flask(__name__, template_folder=os.path.join(config.variables['public_html_session_directory'],'.'), static_folder=os.path.join(config.variables['public_html_session_directory'], 'static'))
app.config.from_object(__name__)

# add gzip compression (mod_deflate would be better if it were enabled)
# taken from http://flask.pocoo.org/snippets/122/
from flask import after_this_request
from io import BytesIO as IO
import gzip
import functools

def gzipped(f):
	@functools.wraps(f)
	def view_func(*args, **kwargs):
		@after_this_request
		def zipper(response):
			accept_encoding = request.headers.get('Accept-Encoding', '')
			if 'gzip' not in accept_encoding.lower():
				return response
			response.direct_passthrough = False
			if (response.status_code < 200 or
				response.status_code >= 300 or
				'Content-Encoding' in response.headers):
				return response
			gzip_buffer = IO()
			gzip_file = gzip.GzipFile(mode='wb', fileobj=gzip_buffer)
			gzip_file.write(response.data)
			gzip_file.close()
			response.data = gzip_buffer.getvalue()
			response.headers['Content-Encoding'] = 'gzip'
			response.headers['Vary'] = 'Accept-Encoding'
			response.headers['Content-Length'] = len(response.data)
			return response
#		def cache(response):
#			cache_filename = '/web/cs2041/flask_cache' + request.path
#			if (response.status_code < 200 or
#				response.status_code >= 300 or
#				response.headers.get('Content-Encoding', '') != 'gzip' or
#				response.headers.get('Content-Type', '') != 'text/html; charset=utf-8' or
#				request.path.endswith('/') or
#				os.path.exists(cache_filename) or
#				is_tutor()):
#				return
#			try:
#				dir = os.path.dirname(cache_filename)
#				os.makedirs(dir, mode=0o755, exist_ok=True)
#				temporary_pathname = '%s.%50d.tmp' % (cache_filename, os.getpid())
#				fd = os.open(temporary_pathname, os.O_WRONLY|os.O_CREAT|os.O_EXCL, 0o666)
#				with os.fdopen(fd, 'wb') as f:
#					f.write(response.data)
#				os.rename(temporary_pathname, cache_filename)
#			except IOError:
#				pass
#			return
		return f(*args, **kwargs)
	return view_func

# Add regex matching for URLs
#
class RegexConverter(BaseConverter):
	def __init__(self, url_map, *items):
		super(RegexConverter, self).__init__(url_map)
		self.regex = items[0]
app.url_map.converters['regex'] = RegexConverter


# HTML files in top-level directory, assignments, code, exam or home computing sub-trees
@app.route("/<string:subpath>.html")
@app.route("/<regex(r'assignments|code|exam|home_computing'):top_level_dir>/<path:subpath>.html")
@gzipped
def html_url(**kwargs):
	return render_template_with_variables(request.path)

# non-HTML files in top-level directory, assignments, code, exam or home computing sub-trees
# FIXME - this function has to avoid serving unreleased solutions etc but need
# to serve code - perhaps it should check for public read to distinguish?

@app.route("/assignments/<string:assignment>/examples/<regex(r'\d+'):subset>/<string:filename>")
@app.route("/<regex(r'assignments|code|exam|home_computing'):top_level_dir>/<path:subpath><regex(r'.*\.(jpg|png|pbm|zip|txt)$'):filename>")
@gzipped
def plain_files(**kwargs):
	return check_send_file(config.variables['public_html_session_directory'] + request.path)


# supplied code for tuts and labs
# solutions will be in sub-directory solutions and aren't served directly
# note this must not match .html suffixes
@app.route("/<regex(r'tut|lab|lab|test'):tut_or_lab_or_test>/<regex(r'\d\d'):week>/<regex(r'.*\.\w{1,3}'):filename>")
@gzipped
def supplied_code(tut_or_lab_or_test, week, filename):
	return check_send_file(config.variables['tlb_directory'], week, filename)

# tutorial & lab questions & answers
@app.route("/<regex(r'tut|lab|test'):tut_or_lab_or_test>/<regex(r'\d\d'):week>/<regex(r'questions|answers'):questions_or_answers>")
@gzipped
def tlb_url(tut_or_lab_or_test, week, questions_or_answers):
	template_variables = get_common_template_variables()
	template_variables['week'] = week
	template_variables['exercise_name'] = tut_or_lab_or_test + week
	template_variables['directory_relative_pathname'] = os.path.join('tlb', week)
	if not os.path.isdir(template_variables['directory_relative_pathname']):
		abort(404)
	template_variables['tut_or_lab_or_test'] = tut_or_lab_or_test
	template_variables['questions_or_answers'] = questions_or_answers
	# we also try to protect unreleased solutions with rewriting rules in htaccess.cgi_account
	page = os.path.join('tlb', week,  tut_or_lab_or_test + '.html')
	if not week in template_variables['tlb_list'][tut_or_lab_or_test][questions_or_answers]['released'] and not is_tutor():
		return render_template_with_variables('templates/unreleased.html', **template_variables)

	# probably delete this and set program in lab exercises
	for dir in [tut_or_lab_or_test + '_' + 'autotest',	'autotest']:
		try:
			with open(os.path.join(template_variables['directory_relative_pathname'], dir , 'PROGRAMS')) as f:
				programs = f.read().strip().split()
			for p in programs:
				if '.' not in p:
					p += '.c'
			template_variables['programs'] = ' '.join(programs)
			break
		except IOError:
			template_variables['programs'] = '<programs>'

	try:
		with open(config.variables['testing_results_file']) as f:
			testing_results = json.load(f)
	except (FileNotFoundError,PermissionError,IOError,ValueError):
		testing_results = {}

	for exercise_results in testing_results.values():
		for autotest_automarking in exercise_results.values():
			for test_group_results in autotest_automarking.values():
				for individual_test in test_group_results.get('individual_tests', {}).values():
					 n = individual_test.setdefault('passed', 0) + individual_test.setdefault('failed', 0)
					 individual_test['passed_fraction'] = individual_test['passed'] / (n or 1)
				n = test_group_results.setdefault('passed', 0) + test_group_results.setdefault('failed', 0)
				test_group_results['passed_fraction'] = test_group_results['passed'] / (n or 1)
	template_variables['testing_results'] = testing_results
	if questions_or_answers == 'answers':
		return render_template_with_variables(page, **template_variables)
	else:
		return str(delete_answers(render_template_with_variables(page, **template_variables)))

# weekly notes for tutors
@app.route("/notes/<regex(r'\d\d'):week>")
@gzipped
def tlb_notes_url(week):
	if not is_tutor():
		abort(404)
	return render_template_with_variables(os.path.join('tlb', week,	 'notes.html'), week=week)

# lecture slides
@app.route("/lec/<string:topic>/<regex(r'slides|notes'):slides_or_notes>")
def lecture_slides_url(topic, slides_or_notes):
	return check_send_file(config.variables['lecture_directory'], '%s%s.pdf' % (topic, '_notes' if slides_or_notes == 'notes' else ''))

# lecture code examples - html file can't be match here
# they need to be templated above
@app.route("/code/<string:topic>/<regex(r'\w+(|\.\w{1,3})'):filename>")
@gzipped
def tlb_code_example_url(topic, filename):
	return check_send_file(config.variables['public_html_session_directory'], 'code', topic, filename)

# pretty listing of example code for lecture topic
@app.route('/code/<string:topic>')
@app.route('/code/<string:topic>/')
@app.route('/code/<string:topic>/index')
@app.route('/code/<string:topic>/index.html')
@gzipped
def lecture_code_topic_url(topic):
	topic_directory = os.path.join('code', topic)
	if os.path.normpath(topic_directory).rstrip('/') != topic_directory.rstrip('/'):
		abort(405) # directory traversal attack has escaped rewriting
	if not os.path.isdir(topic_directory):
		abort(404)
	code_files = OrderedDict()
	try:
		with open(os.path.join(topic_directory, 'index.txt')) as f:
			for line in f.readlines():
				code_files[html.escape(line.strip())] = None
	except IOError:
		pass
	for pathname in glob.glob(os.path.join(topic_directory, '*.?')) + glob.glob(os.path.join(topic_directory, '*.??')):
		code_files[html.escape(os.path.basename(pathname))] = None
	return render_template_with_variables('templates/lecture_example_code.html', topic=topic, code_files=code_files.keys())

@app.route('/')
@app.route('/index.html')
@app.route('/<path:path>')
@gzipped
def catchall_url(**kwargs):
	return render_template_with_variables('templates/index.html')

@app.errorhandler(Exception)
def handle_error(e):
	return render_template_with_variables('templates/error.html', error_message='Internal error from %s: %s' % (request.base_url, e), backtrace = traceback.format_exc())

def check_send_file(*pathname_components):
	pathname = os.path.join(*pathname_components)
	if os.path.normpath(pathname) != pathname:
		abort(405) # directory traversal attack has got through somehow
	extension = os.path.splitext(pathname)[1]
#	 print(pathname, extension[1:].lower())
	try:
		# force mime-type text/plain for code files
		if extension[1:].lower() in ['c', 'h', 'py','pl','sh','cgi']:
			return send_file(pathname, mimetype='text/plain')
		else:
			return send_file(pathname)
	except IOError:
		abort(404)

## return a list of lecture topics
#def lecture_topics():
#	topics = ()
#	try:
#		with open(os.path.join(config.variables['lecture_directory'], 'index.txt')) as f:
#			for line in f:
#				topic = line.strip()
#				if not topic:
#					continue
##				 topic_directory = os.path.join(config.variables['lecture_directory'], topic)
##				 if not os.path.isdir(topic_directory):
##					 continue
#				topics[topic] = html.escape(topic.replace('_', ' ').replace('-', ' - ').title())
#	except IOError:
#		pass
#	return topics

#
# delete any part of a HTML document marked as an answer
#
def delete_answers(page):
	soup = BeautifulSoup(page, "lxml")
	for tag in soup.findAll({'div':True,'span':True,'pre':True}, { "class" : re.compile(r'\banswer\b')}):
		p = soup.new_tag('p')
		tag.replaceWith(p)
	return soup

def read_code(*args, header_only=False, body_only=False, function_only='', max_lines=300):
	pathname = os.path.join(*args)
	extension = os.path.splitext(pathname)[1]
	body_start_regex = r'^(#|\s*int\s+main\s*\()' if extension == '.c' else r'^\s*[^#\s]'
	function_start_regex = r'^\w.*\b%s\(.*\{\s*$' % function_only if extension == '.c' else r'^\w.*\b{}\b'
	if 'template' in pathname:
		body_start_regex = r'^'	 # kludge to get template.c handled nicely
	try:
		with open(pathname) as f:
			if header_only:
				header_comment = []
				for line in f:
					if re.match(body_start_regex, line):
						break
					if re.search(r'^#!', line): continue
					if re.search(r'(writ|by|andrewt).*@(cse.)?unsw.edu.au', line, flags=re.I): continue
					if re.search(r'\d{1,2}/\d{1,2}/\d{1,2}', line): continue
					if re.search(r'[A-Z][a-z]+ \d\d\d\d$', line): continue
					if re.search(r'COMP\d\d\d\d', line): continue
					line = html.escape(line)
					line = re.sub(r'(http://\S+)', r'<a href="\1">\1</a>', line)
					line = re.sub(r'^\s*#\s*', '', line)
					if extension  == '.c':
						line = re.sub(r'\s*//\s*', '', line, count=1)
						line = re.sub(r'\/\*', '<pre>', line)
						line = re.sub(r'\*\/', '</pre>', line)
						line = re.sub(r'^ \*', '', line)
					else:
						line = re.sub(r'^\s*#\s*', '', line)
					if re.search(r'^\s*$|^[A-Z]', line):
						line = '<p>' + line
					header_comment.append(line)
				return "".join(header_comment)
			elif body_only:
				body = []
				for line in f:
					if re.match(body_start_regex, line):
						body.append(line)
						break
				for (line_number,line) in enumerate(f):
					body.append(line)
					if line_number > max_lines:
						break
				if len(body) > max_lines:
					return "".join(body[0:32] + ["..."])
				else:
					return "".join(body)
			elif function_only:
				function = []
				for line in f:
					if re.match(function_start_regex, line):
						function.append(line)
						break
				for line in f:
					function.append(line)
					if line and line[0] == '}':
						break
				print(function_only, function_start_regex, len(function))
				return "".join(function)
			else:
				return f.read()
	except IOError:
		return 'INTERNAL ERROR MISSING FILE: "%s"' % (pathname)

def execute_shell_command(shell_command, cwd=None, input=None):
	p = subprocess.run(shell_command, cwd=cwd, input=input, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,  universal_newlines=True)
	return p.stdout

# should we show things that are only visible to course staff
def is_tutor():
	return request.script_root.endswith('flask_tutors.cgi') or not request.script_root


def render_template_with_variables(page, **template_variables):
	if os.path.normpath(page).rstrip('/') != page.rstrip('/'):
		abort(405) # a directory traversal attack has got through somehow
	tv = get_common_template_variables()
	tv['template_pathname'] = page.lstrip('/')
	tv.update(template_variables)
	if is_tutor():
		tv['directory_relative_pathname'] = os.path.join('private', tv['directory_relative_pathname'])
	tv['directory_absolute_pathname'] = os.path.join(config.variables['public_html_session_directory'], tv['directory_relative_pathname'])
	tv['current_directory'] = tv['directory_absolute_pathname'] # backwards compatibility
	if is_tutor():
		page = os.path.join('private', page)
	return render_template(page, **tv)

# create variables available in all templates
def get_common_template_variables(static_checking=False):
	tv = config.variables

	if os.path.normpath(request.path).rstrip('/') != request.path.rstrip('/'):
		abort(405) # directory traversal attack has got through somehow

	# set default values assuming URL maps into filesystem
	tv['directory_relative_pathname'] = os.path.dirname(request.path).lstrip('/')
	tv['todays_date'] = datetime.date.today()

	# pass in some functions from this file so they can beused in templates
	tv['read_code'] = read_code
	tv['execute_shell_command'] = execute_shell_command

	# pass in some modules used in templates
	tv['os'] = os
	tv['glob'] = glob
	tv['re'] = re

	# pass in some standard functions
	tv['isinstance'] = isinstance
	tv['len'] = len
	tv['sorted'] = sorted
	tv['str'] = str

	if static_checking:
		# fake these for static checking
		dummy_url = "http://a.b/"
		tv['tut_or_lab_or_test'] = 'tut'
		tv['url_for'] = lambda *a, **k: dummy_url
		tv['url'] = dummy_url
		tv['url_root'] = re.sub(r'\w*\.cgi/?$', '', dummy_url)
	else:
		# these fail when static checking a template because there is no http request
		tv['url'] = request.url
		tv['directory_url'] = re.sub(r'/\w*\.cgi/', '/', re.sub(r'[^/]*$', '', request.url))
		tv['url_root'] = re.sub(r'\w*\.cgi/?$', '', request.url_root)
		tv['script_root'] = request.script_root
		tv['is_tutor'] = is_tutor()
	tv['full_name'] = {
			'tut': {'self': 'Tutorial', 'questions': 'Questions', 'answers' :  'Sample Answers'},
			'lab': {'self': 'Laboratory', 'questions': 'Exercises', 'answers' :	 'Sample Solutions'},
			'test': {'self': 'Weekly Test', 'questions': 'Questions', 'answers' :	'Sample Solutions'},
	}
	tv['tlb_list'] = defaultdict(lambda:defaultdict(lambda:defaultdict(lambda:[])))
	tv['tlb_list']['notes'] = []
	tv['weeks'] = set()
	for tlb_path in sorted(glob.glob(os.path.join(config.variables['tlb_directory'], '[0-9][0-9]'))):
		week = os.path.basename(tlb_path)
		for tut_or_lab_or_test in ['tut', 'lab', 'test']:
			for questions_or_answers in ['questions', 'answers']:
				if os.path.exists(os.path.join(tlb_path, tut_or_lab_or_test + '.html')):
					if os.path.exists(os.path.join(tlb_path, '%s_%s_released' % (tut_or_lab_or_test, questions_or_answers))):
						tv['tlb_list'][tut_or_lab_or_test][questions_or_answers]['released'].append(week)
						tv['weeks'].add(week)
					else:
						tv['tlb_list'][tut_or_lab_or_test][questions_or_answers]['unreleased'].append(week)
		if os.path.exists(os.path.join(tlb_path, 'notes.html')):
			tv['tlb_list']['notes'].append(week)

	tv['lecture_topics'] = OrderedDict()
	try:
		with open(os.path.join(config.variables['lecture_directory'], 'index.txt')) as f:
			for line in f:
				topic = line.strip()
				if topic:
					tv['lecture_topics'][topic] = html.escape(topic.replace('_', ' ').replace('-', ' - ').title())
	except IOError:
		pass

	tv['code_files'] = {}
	for topic in tv['lecture_topics']:
		topic_directory = os.path.join(config.variables['public_html_session_directory'], 'code', topic)
		code_files = OrderedDict()
		try:
			with open(os.path.join(topic_directory, 'index.txt')) as f:
				for line in f.readlines():
					code_files[html.escape(line.strip())] = None
		except IOError:
			pass
		# This code would include files not listed in index.txt
#		 for pathname in glob.glob(os.path.join(topic_directory, '*.?')) + glob.glob(os.path.join(topic_directory, '*.??')):
#			 code_files[html.escape(os.path.basename(pathname))] = None
		tv['code_files'][topic] = code_files
	tv['lecture_details'] = defaultdict(lambda:defaultdict(lambda:{}))
	tv['current_lecture_topic'] = ''

	for lecture_description_file in sorted(glob.glob(os.path.join(config.variables['public_html_session_directory'], 'lec', 'week*_*.txt'))):
		m = re.search(r'(\d\d)_(.*)\.txt$', lecture_description_file)
		if not m:
			continue
		(week,day) = m.groups()
		full_day = {'mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday'}.get(day, day)
		details = tv['lecture_details'][week][day]
		details['full_day'] = full_day
		tv['weeks'].add(week)
		try:
			with open(lecture_description_file) as f:
				date = f.readline().strip()
				details['date'] = date
				details['full_day_date'] = full_day + ' ' + date
				details['topics'] = OrderedDict()
				details['key_examples'] = {}
				for line in f:
					f = line.split()
					if f:
						topic = f[0]
						key_examples =	f[1:]
						tv['current_lecture_topic'] = topic
						details['topics'][topic] = key_examples
						for code_file in key_examples:
							if topic in tv['code_files']:
								tv['code_files'][topic][code_file] = full_day + ' ' + date
		except IOError:
			pass

	if tv['weeks']:
		tv['weeks'] = sorted(tv['weeks'])
		tv['current_week'] = tv['weeks'][-1]
	else:
		tv['current_week'] = ''
	tv['template_variables'] = tv
	return tv

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
