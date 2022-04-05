class Station (object):
    def __init__(self, id:int = 0, name:str = "", neighbours:list = []) -> None:
        self.__id = id
        self.__name = name
        self.__neighbours = neighbours
    
    def __eq__(self, __o: object) -> bool:
        return self.id() == __o.id()

    def __ne__(self, __o: object) -> bool:
        return self.id() != __o.id()

    def __str__(self):
        return self.__name

    def id(self) -> int:
        return self.__id
    
    def name(self) -> str:
        return self.__name
    
    def neighbours(self) -> list:
        return self.__neighbours
    
    def isNeighbour(self, neighbour) -> bool:
        return neighbour in self.__neighbours

    def addNeighbour(self, neighbour) -> bool:
        if self.isNeighbour(neighbour):
            return False
        
        self.__neighbours.append(neighbour)
        return True

    def removeNeighbour(self, neighbour) -> bool:
        try:
            self.__neighbours.remove(neighbour)
        except ValueError:
            return False
        
        return True

def LinkStations(A:Station, B:Station) -> None:
    A.addNeighbour(B)
    B.addNeighbour(A)