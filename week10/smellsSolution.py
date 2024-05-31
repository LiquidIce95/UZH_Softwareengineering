from abc import ABC,abstractmethod

class ArgumentForLongParList:
  """
  params:
  a @ some number
  b @ some number
  """
  def __init__(self,a:int,b:int,c:int,d:int):
    self.a = a
    """
    explains why the Attribute is important to avoid forgetting its meaning
    """
    self.b = b
    self.c = c
    self.d = d

def longParameterList(O:ArgumentForLongParList):

  numberOflocations : int  = 3

  
  l = O.a+O.b
  r = O.c+O.d
  return l%r + numberOflocations

class animal(ABC):
  @abstractmethod
  def makeNoise(self):
    pass

class dog(animal):
  def makeNoise(self):
    print("wuff")


class cat(animal):
  def makeNoise(self):
    print("miau")


class AnimalShelter:
  def __init__(self) -> None:
    self.animals = []

  def addAnimal(self,x:animal):
    self.animals.append(x)


if __name__ == "__main__":
  a : dog = dog()
  b : cat = cat()
  S :AnimalShelter = AnimalShelter()

  S.addAnimal(a) 