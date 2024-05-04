


class University:
  def __init__(self,subjects:list[subject], students:list[student],professors:list[prof]):
    self.subjects = subjects
    self.students = students
    self.professors = professors

class invoice:
  def __init__(self,recipient:str,sender:str,amount:int):
    self.recipient = recipient
    self.sender = sender
    self.amount = amount

class subject:
  def __init__(self,professors:list[prof]):
    self.professors = professors

class prof:
  def __init__(self,salary:int, university:University,subject:subject):
    self.salary = salary
    self.university = university
    self.subject = subject

class student:
  def __init__(self,grades:dict[subject,int],invoices:list[invoice],subjects:list[subject]):
    self.grades = grades
    self.invoices = invoices
    self.subjects = subjects





if __name__ == "__main__":
  pass