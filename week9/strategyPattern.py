from abc import ABC,abstractmethod

class LobbyService(ABC):
  @abstractmethod
  def joinSomeLobby(self):
    pass
  

class GameMode1Service(LobbyService):
  def joinSomeLobby(self):
    print("for this gamemode implementations")


class GameMode2Service(LobbyService):
  def joinSomeLobby(self):
    print("another impl.")


class Context:
  def __init__(self,type):
    if type == 1: self.Service=GameMode1Service()
    elif type == 2: self.Service=GameMode2Service()



if __name__ == "__main__":
  pass