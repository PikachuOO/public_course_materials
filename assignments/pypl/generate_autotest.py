#!/usr/bin/python3
import glob, re, subprocess, os

print("""
max_cpu=3
max_wall_clock=30
program=pypl.pl
shell=1
""")

for level in "0 1 2 3".split():
	for file in glob.glob("examples/%s/*.py" % level):
		with open(file) as f:
			contents=f.read()
#		 if re.search(r'(\b(ls|gcc|pwd|cd)\b)|[\*\?]', contents):
#			 continue
		basename = re.sub(r'.*/', '',  file)
		basename = re.sub(r'\.[^\.]*$', '',	 basename)
		label = "%s-%s" % (level, basename)
		input = "examples/input"
		custom_input = "examples/%s/%s.input" % (level, basename)
		if os.path.exists(custom_input):
			input = custom_input
		arguments = ""
		if 'sys.argv' in contents:
			arguments = "24 42 13 14 15"
		command = "./pypl.pl <%s >tmp.pl; chmod +x tmp.pl;./tmp.pl %s" % (file, arguments)
		if input == custom_input or 'sys.stdin' in contents:
			command += ' <'+ input
		print("{} command=\"{}\" description=\"{}\"".format(label, command, file))
		subprocess.call("<%s %s %s	>autotest/%s.expected_stdout"  % (input, file,	arguments, label), shell=True)
