# Jenkins Log Parser

Parase the Jenkins Log and print the errors with count

## Getting Started

git clone https://github.com/bkumaran/jenkins_parser.git

## Prerequisites

Python 2.7.10

## Running the script
python jenkins_log_parser.py http://qa.sc.couchbase.com/job/test_suite_executor/13090/consoleText


## Notes
* Works only when the log is in  pass 0 , fail 0 format.
* Not useful when the number of tests run/failed is less.


