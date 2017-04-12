# Jenkins Log Parser

Parase the Jenkins Log and print the errors with count

## Getting Started

git clone https://github.com/bkumaran/jenkins_parser.git

### Prerequisites

Python 2.7.10

## Running the script

python jenkins_log_parser.py http://qa.sc.couchbase.com/job/test_suite_executor/13090/consoleText
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Error                                                                                                                                                  Count   
--------------------------------------------------------------------------------------------------------------------------------------------------------------
AssertionError: deleting bucket succeeded during gsi rebalance                                                                                         1       
InvalidArgumentException: controller/rebalance with error message {"noKVNodesLeft":1} failed when invoked with parameters: password=password&ejectedNo 9       
AssertionError: index creation did not fail as expected                                                                                                1       
AssertionError: unable to reach the host @ 172.23.98.187                                                                                               2       
IndexError: list index out of range                                                                                                                    17      
AssertionError: Rebalance Failed: {u'status': u'none', u'errorMessage': u'Rebalance failed. See logs for detailed reason. You can try again.'} - rebal 13      
AssertionError: timed out waiting for cbindex move to complete                                                                                         2       
AssertionError: build index did not fail during gsi rebalance with expected error message: See MB-23452 for more details                               1       
AssertionError: rebalance failed, stuck or did not complete                                                                                            2       
FailoverFailedException: Failover Node failed :Last active node cannot be failed over.                                                                 1       
CBQError: CBQError: host 172.23.98.187: ERROR:{u'status': u'errors', u'errors': [{u'msg': u'GSI CreateIndex() - cause: Fail to create index or replcia 1       
AssertionError: cbindex move succeeded during a rebalance                                                                                              1       
AssertionError: rebalance failed with some unexpected error : controller/rebalance with error message {"noKVNodesLeft":1} failed when invoked with par 4       
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Total Errors                                                                                                                                           55      
--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Notes
* Not Really useful when the number of tests run/failed is less


