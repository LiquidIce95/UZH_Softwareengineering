
class invoice:
  def __init__(self,recipient:str,sender:str,amount:int):
    self.recipient = recipient
    self.sender = sender
    self.amount = amount

class University:
  """we get rid of subjects, since the professors at an university enable the university to teach certain subjects"""
  """also any student (which is assumed to be enrolled in some class) is therefore assigned at least one professor"""
  def __init__(self,professors:list[prof]):
    self.professors = professors

class prof:
  """if professors can only be accessed via an university then it will always be clear from which university that professor is"""
  def __init__(self,salary:int, university:University,subject:str,students:list[student]):
    self.salary = salary
    self.subject = subject
    self.studnets = students



"""we can get completey rid of subjects since they can be modelled as simply strings"""


"""since every studnet is assignemt to some professor its now also clear which subjects the student is taking"""
class student:
  def __init__(self,grades:dict[str,int],invoices:list[invoice]):
    self.grades = grades
    self.invoices = invoices

"""with these changes we now have the universisty class which is only coupled with professors, then professors which are coupled with students and students which are
coupled with invoices in one way, if starting from university all the entities have access to all the information as before, however if starting at student for example
then it might not be possible to know which and if any university that studnet is assigned. but even that could be cirumvented by using weakref in python"""

"""or the remaining of the programm enforces that studnets and profeesors only exist as fields in university"""



if __name__ == "__main__":
  pass