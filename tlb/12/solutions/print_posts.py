#!/usr/bin/python3

import glob, os, sys

dataset = "dataset-medium"

def student_post_filenames(student):
	post_filenames = glob.glob(os.path.join(dataset, student, '*.txt'))
	return sorted(post_filenames, reverse=True) 

for user in sys.argv[1:]:
	print(" ".join(student_post_filenames(user)))
