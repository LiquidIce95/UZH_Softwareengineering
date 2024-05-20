from abc import ABC,abstractmethod
from enum import Enum

class GameModes(Enum):
  GameMode1 = 1
  GameMode2 = 2


class LobbyInterface(ABC):
  def __init__(self,playerLimit:int,gameMode:GameModes):
    self.playerLimit = playerLimit
    self.gameMode = gameMode

  @abstractmethod
  def joinLobby(self):
    pass

class GameMode1Lobby(LobbyInterface):
  def joinLobby(self):
    print("lobby joined")


class GameInterface(ABC):
  def __init__(self,playerLimit:int,gameMode:GameModes):
    self.playerLimit = playerLimit
    self.gameMode = gameMode

  @abstractmethod
  def joinLobby(self):
    pass

class Game(GameInterface):

  def playGame(self):
    print("game is played")



class AbstractFactory(ABC):

  @abstractmethod
  def createLobby()->LobbyInterface:
    pass

  @abstractmethod
  def createGame()->GameInterface:
    pass


class GameMode1(AbstractFactory):
  def createLobby() -> GameMode1Lobby:
    return GameMode1Lobby()
  
  def createGame() -> Game:
    return Game()


if __name__ == "__main__":
  pass