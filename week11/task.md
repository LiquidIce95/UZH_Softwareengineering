1.Create a fucntion which demonstrates the difference between branch and path coverage
def foo(x):
  if x >0: print("a")
  if x >5: print("b")

branch coverage 100% can be achieved with all x >5
however for path coverage 100% one also needs one test with some x with 5>x>0, since these are the only possible paths.

2.Describe one scenario in which a regression test would not be sensible and one where it absolutely is.

lets say you deleted comments or added comments, then your changes have literally no effect on the code, so regression testing would only waste time, however lets say you changed variable names or file names, even though youre sure you catched all the modifications, regression test is still advisable since the chances of missing one single change leads to an error or unexpected behaviour.

3.How can one use state design pattern to minimize tests?
by using the sate deisgn pattern one gets rid of if statements and gets complete coverage of the execution logic only with unit tests of the state objects

4.Give a concrete exapmle where blackbock testing might come handy for developers.
Testing via interfaces, one can test interfaces with pre and post conditions without knowing about current or future implementations

5.Give 3 Differences between black and white box testing
black covers input space, white covers paths
black tests based on specs, white tests based on code
black aims to test as much specified behaviour as possible
white aims to test as much code as possible


6.What is the purpose of mutation testing?
its supposed to test the effectiveness of your testSuite