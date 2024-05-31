

def longParameterList(a:int,b:int,c:int,d:int):
  l = a+b
  r = c+d
  return l%r + 3


class dog:
  def bark(self):
    print("wuff")


class cat:
  def miau(self):
    print("miau")


class AnimalShelter:
  def __init__(self) -> None:
    self.animals = []


if __name__ == "__main__":
  a : dog = dog()
  b : cat = cat()
  S :AnimalShelter = AnimalShelter()

  S.animals.append(a) 