class Station (object):
    '''
    Stations containing an unique id number, a name, and a list of neighbouring stations
    '''

    class IDRepeatException (Exception):
        '''
        Station ID Repetition Exception
        '''
        def __init__(self, message:str, errors = []) -> None:
            super().__init__(message)
            self.errors = errors

    class NeighbourException (Exception):
        '''
        Neigbour-based Exception
        '''
        def __init__(self, message:str, errors = []) -> None:
            super().__init__(message)
            self.errors = errors

    idList = set()  
    '''
    list of all station IDs to enforce uniqueness of IDs
    '''
    
    def __init__(self, id:int = 0, name:str = "", neighbours:list = []) -> None:
        '''
        CONSTRUCTOR
            tracks ID number
        
        PARAMETERS: unique ID number : int, station name : str, neighbouring stations list : list[Station]
        '''
        self.__id = id
        
        if self.__id in Station.idList:
            raise Station.IDRepeatException("Station #%d already exists" %self.__id)
        
        Station.idList.add(self.__id)
        
        self.__name = name
        self.__neighbours = neighbours
    
    def __del__(self) -> None:
        '''
        DESTRUCTOR
            removes ID number
        '''
        Station.idList.remove(self.__id)
    
    def __eq__(self, __o: object) -> bool:
        '''
        EQUALITY OPERATOR
            compares Station IDs exclusively
        '''
        return self.id() == __o.id()

    def __ne__(self, __o: object) -> bool:
        '''
        INEQUALITY OPERATOR
            compares Station IDs exclusively
        '''
        return self.id() != __o.id()

    def __str__(self):
        '''
        STRING OPERATOR
            regresses to Station name
        '''
        return self.__name

    def id(self) -> int:
        return self.__id
    
    def name(self) -> str:
        return self.__name
    
    def neighbours(self) -> list:
        return self.__neighbours
    
    def isNeighbour(self, neighbour) -> bool:
        '''
        METHOD isNeighbour
           checks if a neighbour is in the neighbour list

        PARAMETERS: neighbour : Station
        '''
        return neighbour in self.__neighbours

    def addNeighbour(self, neighbour) -> None:
        '''
        METHOD addNeighbour
            adds a neighbour to the neighbour list provided that the following exceptions aren't thrown
                
                Station.NeighbourException for self-reference/station repetition
        
        PARAMETERS: neighbour : Station
        '''
        if neighbour == self:
            raise Station.NeighbourException("Station #%d attemepting to neighbour itself" %self.__id)

        try:
            assert(not self.isNeighbour(neighbour))
            self.__neighbours.append(neighbour)
        
        except AssertionError:
            raise Station.NeighbourException("Station #%d is already a neighbour to station #%d" %(neighbour.id(), self.__id))

    def removeNeighbour(self, neighbour) -> None:
        '''
        METHOD removeNeighbour
            removes a neighbour from the neighbour list provided that the following exceptions aren't thrown
                
                Station.NeighbourException for non-neighbour station reference
        
        PARAMETERS: neighbour : Station
        '''
        try:
            self.__neighbours.remove(neighbour)
        
        except ValueError:
            return Station.NeighbourException("Station #%d is not a neighbour to station #%d" %(neighbour.id(), self.__id))

def LinkStations(A:Station, B:Station) -> None:
    '''
    FUNCTION LinkStations
        performs mutual neighbouring of stations
    
    PARAMETERS: A : Station, B : Station
    '''
    A.addNeighbour(B)
    B.addNeighbour(A)