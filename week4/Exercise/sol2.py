
def returnLowerCaseList(string:str)->list:
  return [ch for ch in string if ch.islower()]

def returnUpperCaseList(string:str)->list:
  return [ch for ch in string if ch.isupper()]

def returnSortedList(string:str)->list:
  return sorted(string)

def solveTask(string:str)->tuple:
  return returnUpperCaseList(string),returnLowerCaseList(string),returnSortedList(string)

if __name__ == "__main__":
  pass