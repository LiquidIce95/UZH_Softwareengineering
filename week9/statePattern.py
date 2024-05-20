from abc import ABC,abstractmethod

class GameStates(ABC):
  @abstractmethod
  def setPoints(self):
    pass

class firstRound(GameStates):
  def setPoints(self):
    print("logic for setting points is in first round different")
  
class midRound(GameStates):
  def setPoints(self):
    print("setting points for a mid round")

class lastRound(GameStates):
  def setPoints(self):
    print("setting points in last round")

class Game:
  def __init__(self,state:GameStates):
    self.state = state

  def join(self):
    pass

  def leave(self):
    pass




if __name__=="__main__":
  pass