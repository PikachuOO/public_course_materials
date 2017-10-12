#!/bin/sh

# written by andrewt@cse.unsw.edu.au
# Aug 2017 as a COMP2041 programming example

if test $# != 1
then
    echo "Usage: $0 <course-prefix>"
    exit 1
fi

# get current year
year=`date '+%Y'`
course_prefix=$1
first_letter=`echo $course_prefix|sed 's/\(.\).*/\1/'`
base_url="http://www.handbook.unsw.edu.au/vbook$year/brCoursesByAtoZ.jsp"
ugrad_url="$base_url?StudyLevel=Undergraduate&descr=$first_letter"
pgrad_url="$base_url?StudyLevel=Postgraduate&descr=$first_letter"

wget -q -O- "$ugrad_url" "$pgrad_url"|
egrep "$course_prefix[0-9][0-9][0-9][0-9].html"|
sed "s/.*\($course_prefix[0-9][0-9][0-9][0-9]\)\.html[^>]*> *\([^<]*\).*/\1 \2/"|
sed 's/ *$//'|
sort|
uniq
