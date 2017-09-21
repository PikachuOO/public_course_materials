#!/bin/sh
#
# set variables to appropriate values for course & session
#
# See also environment.py

# unset possibly dangerous environment variables
unset CDPATH IFS LOCALE LD_LIBRARY_PATH LD_PRELOAD LD_AUDIT ORIGIN

export PATH=/bin/:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/home/class/bin:.:$PATH
export LANG=en_AU.UTF-8
export LANGUAGE=en_AU:en
export LC_ALL=en_AU.UTF-8
export LC_COLLATE=POSIX
export GIVEHOME=/home/give/stable
export ARCH=pc.i86.linux

course_name='Software Construction'
postgraduate_course_code='COMP9041'
course_code_regex=`echo "$course_code_uc"|sed 's/COMP2041/COMP[29]041/'`

# these values need to updated every session
course_forum_url='https://piazza.com/class/j5ji4vjjra62a3'
lecture_recordings_url='https://moodle.telt.unsw.edu.au/course/view.php?id=27708'

# these values are only used if they can't be extracted from $0
public_html_session_directory='/web/cs2041/17s2'
public_html_directory='/web/cs2041'
course_account='cs2041'
unsw_session='17s2'


# if we are running as a CGI script at CSE
# home directories are not mounted
# and public_html directory are mounted as /web/account/


dir=$(dirname $(readlink -f $0))
case "$dir" in
*/public_html/[0-9][0-9]??/*)
    public_html_session_directory=$(echo "$dir"|sed 's?\(.*public_html/[0-9][0-9]..\).*?\1?')
    unsw_session=$(basename "$public_html_session_directory")
    public_html_directory=$(dirname "$public_html_session_directory")
    course_account=$(basename $(dirname "$public_html_directory")|sed 's/[a-z]*$//')
    ;;

/web/*/[0-9]][0-9]??/*)
    public_html_session_directory=$(dirname "$dir")
    unsw_session=$(basename "$public_html_session_directory")
    public_html_directory=$(dirname "$public_html_session_directory")
    course_account=$(basename "$public_html_directory"|sed 's/[a-z]*$//')
    ;;

esac

scripts_directory="$public_html_session_directory/scripts"
home_directory="/home/$course_account"
bin_directory="$home_directory/bin"

course_code_lower_case=`echo $course_account|sed 's/.*cs/comp/;s/.*se/seng/;s/.*bi/binf/;s?/.*??'`
course_code=`echo $course_code_lower_case|tr a-z A-Z`
course_number=`echo $course_code|sed 's/[^0-9]//'`
course_code_regex=`echo "$course_code"|sed 's/COMP2041/COMP[29]041/'`

canonical_url="https://cgi.cse.unsw.edu.au/~$course_account/"
github_repo_url="https://github.com/${course_code}UNSW/course_materials"
tlb_directory=$public_html_session_directory/tlb/
lecture_directory=$public_html_session_directory/lec
flask_cache_directory=$public_html_session_directory/flask_cache
testing_results_file="$public_html_session_directory/work/testing_results.json"
autotest_upload_url="${canonical_url}cgi/autotest_upload.cgi"

export WORK=$home_directory/$unsw_session.work/
export OUT=$WORK/.out/
export MARKED=$OUT/.marked/
export SMSDB=$WORK/${unsw_session}db.sms
export PATH="$script_directory:$bin_directory:$PATH"
export PYTHONPATH="$public_html_session_directory/lib/python:$PYTHONPATH"
test -n "$DEBUG" && set -x
