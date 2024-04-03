def solveTask(string:str):

  """exception , provided for you"""
  lowerCaseASCII = [chr(i) for i in range(97,122)]
  upperCAseAScii = [chr(i) for i in range(65,90)]

  
  lowercase = []
  uppercase = []
  sortedStr = []

  j = 0

  while (string[j] != string[-1]):
    if string[j] in lowerCaseASCII:
      lowercase = lowercase+[string[j]]
    elif string[j] in upperCAseAScii:
      uppercase = uppercase+[string[j]]  

    j+=1

  """now you would actually need to implement the sorting algorithm..."""
  



if __name__ == "__main__":
  solveTask()