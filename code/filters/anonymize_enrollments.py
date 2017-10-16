#!/usr/bin/python
import re, random, fileinput
from collections import defaultdict
enrollments = []
course_code_count= defaultdict(int)
seen = defaultdict(int)
first_name_count = defaultdict(lambda:defaultdict(int))
last_name_count = defaultdict(lambda:defaultdict(int))
for line in fileinput.input():
    enrollment =line.rstrip().split('|')
    enrollments.append(enrollment)
    (code,upi,name,program,plan,wam,session,birthdate,gender) = enrollment[0:9]
    course_code_count[code] += 1
    if upi not in seen:
        last_name = re.sub(r",.*", "", name)
        first_name = re.sub(r".*,\s*", "", name)
        first_name = re.sub(r"\s.*", "", first_name)
        first_name_count[gender][first_name] += 1
        last_name_count[gender][last_name] += 1
        seen[upi] += 1
for gender in first_name_count.keys():
	for (name,count) in  first_name_count[gender].items():
		if count < 3:
			first_name_count[gender].pop(name, 0)
	for (name,count) in  last_name_count[gender].items():
		if count < 3:
			last_name_count[gender].pop(name, 0)
upis = range(5000000,5100000)
enrolled_in = {}
student_details = {}
for enrollment in enrollments:
    (code,upi,name,program,plan,wam,session,birthdate,gender) = enrollment[0:9]
    if gender not in ['M', 'F']: continue
    if upi not in student_details:
        last_name = random.choice(last_name_count[gender].keys())
        if random.random() < 0.002:
        	first_name = '.'
        else:
	        first_name = random.choice(first_name_count[gender].keys())
	        for i in range(0, 5):
	        	if random.random() < 0.25:
		        	first_name += " " + random.choice(first_name_count[gender].keys())
        student_details[upi] = [str(upis.pop(random.randrange(len(upis)))), "%-50s"%((last_name+", "+first_name)[0:50])]
        for i in range(3,9):
            student_details[upi].append(random.choice(enrollments)[i])
        student_details[upi][6] = str(int(student_details[upi][6]) + 10000 * random.randint(-5, 5))
        student_details[upi][7] = gender
    if upi not in enrolled_in:
        enrolled_in[upi] = {}
#    possible_codes = [c for c in course_code_count.keys() if not re.match(r'COMP[49][5-9]', c) and c not in enrolled_in[upi]]
#    anonymized_code = random.choice(possible_codes)
#    enrolled_in[upi][anonymized_code] = 1
	anonymized_code = code
    print "|".join([code]  + student_details[upi])
