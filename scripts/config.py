#!/usr/bin/python3
#
# set variables to appropriate values for course & session
#
# See also environment.sh

import os, re, sys

# unset possibly dangerous environment variables
for variable in "CDPATH IFS LOCALE LD_LIBRARY_PATH LD_PRELOAD LD_AUDIT ORIGIN".split():
    os.environ.pop(variable, None)

# /home/class/bin needed so this wworks in exam environment
os.environ['PATH'] = '/bin/:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/home/class/bin:/home/give/stable/bin.:'+ os.environ.get('PATH', '')
os.environ['LANG'] = 'en_AU.utf8'
os.environ['LANGUAGE'] = 'en_AU.UTF-8'
os.environ['LC_ALL'] = 'en_AU.UTF-8'
os.environ['LC_COLLATE'] = 'POSIX'

course_name='Software Construction'
postgraduate_course_code='COMP9041'
# these values need to updated every session
course_forum_url='https://piazza.com/class/j5ji4vjjra62a3'
lecture_recordings_url='https://moodle.telt.unsw.edu.au/course/view.php?id=27708'

# these values are only used if they can't be extracted from sys.argv[0]
public_html_session_directory='/web/cs2041/17s2'
course_account='cs2041'
unsw_session='17s2'

#
# if we are running as a CGI script at CSE
# home directories are not mounted
# and public_html directory are mounted as /web/account/
#


dir = os.path.dirname(os.path.realpath(sys.argv[0]))
m = re.search(r'^(.*\b([a-z][a-z]\d{4})(cgi)?\b.*\b(\d\d[sx][12])\b).*', dir)
if m:
    (public_html_session_directory, course_account, unsw_session) = (m.group(1), m.group(2),  m.group(4))
else:
    m = re.search(r'^(.*\b([a-z][a-z]\d{4})(cgi)?(/public_html)?)\b.*', dir)
    if m:
        (public_html_session_directory, course_account, unsw_session) = (m.group(1), m.group(2), unsw_session)

home_mount_pathname = re.sub('/tmp_amd/\w+/export/\w+/\d/(\w+)', r'/home/\1', public_html_session_directory)
web_mount_pathname = re.sub('/tmp_amd/\w+/export/\w+/\d/(\w+)/public_html', r'/web/\1', public_html_session_directory)
if os.path.exists(home_mount_pathname):
    public_html_session_directory = home_mount_pathname
elif os.path.exists(web_mount_pathname):
    public_html_session_directory = web_mount_pathname

course_code = course_account
for (short,full) in {'cs':'COMP', 'en':'ENGG', 'se':'SENG', 'bi':'BINF'}.items():
    if course_code.startswith(short):
        course_code = course_code.replace(short, full)
        break

variables = {
    'public_html_session_directory' : public_html_session_directory,
    'base_directory' : public_html_session_directory, # backwards compatibility
    'public_html_directory' : os.path.dirname(public_html_session_directory),
    'scripts_directory' : os.path.join(public_html_session_directory, 'scripts'),
    'home_directory' : os.path.join('/home', course_account),
    'bin_directory' : os.path.join('/home', course_account, 'bin'),
    'course_account' : course_account,
    'course_code' : course_code,
    'course_number' : course_code[4:],
    'postgraduate_course_code' : postgraduate_course_code,
    'course_name' : course_name,
    'unsw_session' : unsw_session,
    'canonical_url' : 'https://cgi.cse.unsw.edu.au/~' + course_account + '/',
    'github_repo_url' : 'https://github.com/{}UNSW/course_materials'.format(course_code),
    'course_forum_url': course_forum_url,
    'lecture_recordings_url': lecture_recordings_url,
    'WORK' : os.path.join(public_html_session_directory , 'work'),
    'OUT' : os.path.join(public_html_session_directory , 'work', '.out'),
    'MARKED' : os.path.join(public_html_session_directory , 'work', '.out', '.marked'),
    'SMSDB' : os.path.join(public_html_session_directory , 'work', unsw_session+'db.sms'),

    'course_codes' : [course_code, postgraduate_course_code], # including aliases
    'tlb_directory' : os.path.join(public_html_session_directory, 'tlb'),
    'lecture_directory' : os.path.join(public_html_session_directory, 'lec'),
    'flask_cache_directory' :  os.path.join(public_html_session_directory, 'flask_cache'),
    'testing_results_file' : os.path.join(public_html_session_directory, 'work', 'testing_results.json'),
    'enrollments_file' : os.path.join(public_html_session_directory, 'work', 'enrollments.json'),
    'unsw_ldap_password_file' : os.path.join('/web', course_account, '.unsw_ldap_password'),
    'autotest_upload_url' : 'https://cgi.cse.unsw.edu.au/~{}/cgi/autotest_upload.cgi'.format(course_account),
}
variables['PATH'] = ':'.join((variables['scripts_directory'], variables['bin_directory'],   os.environ['PATH']))

for variable in "WORK OUT MARKED SMSDB PATH".split():
    os.environ[variable] = variables[variable]
