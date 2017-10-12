#!/usr/bin/python
import glob, sys, re

if len(sys.argv) != 2:
    sys.stdout.write("Usage: %s <function-name>\n\n" % sys.argv[0])
    sys.exit(1)

function = sys.argv[1]

for c_file in glob.glob("*.c"):
    with open(c_file) as cf:
        # note use of \b (word boundary) to match function
        function_regex = r'\b%s\s*\(' % function
        line_number = 0
        for line in cf:
            line_number = line_number + 1
            # remove single-line comments & strings (breaks if strings contain ")
            line = re.sub(r'\/\/.*', '', line)
            line = re.sub(r'".*?"', '', line)
            if not re.search(function_regex, line):
                continue
            # if line is indented it should be a call to the function
            if re.search(r'^\s', line):
                which = "used"
            elif re.search(r';', line):
                which = "declared"
            else:
                which = "defined"
            print("%s:%d function %s %s" % (c_file, line_number, function,  which))
