class Station (object):

    class IDRepeatException (Exception):
        def __init__(self, message:str, errors = []) -> None:
            super().__init__(message)
            self.errors = errors

    class NeighbourException (Exception):
        def __init__(self, message:str, errors = []) -> None:
            super().__init__(message)
            self.errors = errors

    idList = set()

    def __init__(self, id:int = 0, name:str = "", neighbours:list = []) -> None:
        self.__id = id
        
        if self.__id in Station.idList:
            raise Station.IDRepeatException("Station #%d already exists" %self.__id)
        
        Station.idList.add(self.__id)
        
        self.__name = name
        self.__neighbours = neighbours
    
    def __del__(self) -> None:
        Station.idList.remove(self.__id)
    
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

    def addNeighbour(self, neighbour) -> None:
        if neighbour == self:
            raise Station.NeighbourException("Station #%d attemepting to neighbour itself" %self.__id)

        try:
            assert(not self.isNeighbour(neighbour))
            self.__neighbours.append(neighbour)
        
        except AssertionError:
            raise Station.NeighbourException("Station #%d is already a neighbour to station #%d" %(neighbour.id(), self.__id))

    def removeNeighbour(self, neighbour) -> None:
        try:
            self.__neighbours.remove(neighbour)
        except ValueError:
            return Station.NeighbourException("Station #%d is not a neighbour to station #%d" %(neighbour.id(), self.__id))

def LinkStations(A:Station, B:Station) -> None:
    A.addNeighbour(B)
    B.addNeighbour(A)