from route import Route, quanta
from station import Station
from weekdist import WeekDist

class SeatingClassCapacity (object):
    def __init__(self, firstAC:int = 0, secondAC:int = 0, thirdAC:int = 0, sleeper:int = 0, reserved:int = 0) -> None:
        self.__dist = {
            "first AC" : firstAC,
            "second AC" : secondAC,
            "third AC" : thirdAC,
            "sleeper" : sleeper,
            "reserved" : reserved
        }
    
    def get(self, classType:str) -> float:
        return self.__dist.get(classType)
    
    def set(self, classType:str, value:float) -> None:
        return self.__dist.update({ classType : value })

class SeatingClassCost (object):
    def __init__(self, firstAC:float = 0.0, secondAC:float = 0.0, thirdAC:float = 0.0, sleeper:float = 0.0, reserved:float = 0.0) -> None:
        self.__dist = {
            "first" : firstAC,
            "second" : secondAC,
            "third" : thirdAC,
            "sleeper" : sleeper,
            "reserved" : reserved
        }
    
    def get(self, classType:str) -> float:
        return self.__dist.get(classType)
    
    def set(self, classType:str, value:float) -> None:
        return self.__dist.update({ classType : value })

class StatusReport (object):
    def __init__(self, id:int, name:str, time:quanta) -> None:
        self.__id = id
        self.__name = name
        self.__time = time
    
    def id(self) -> int:
        return self.__id
    
    def name(self) -> str:
        return self.__name
    
    def estimatedArrival(self) -> quanta:
        return self.__time

class CoachStats (object):
    def __init__(self, capacityChart:SeatingClassCapacity = SeatingClassCapacity(), costChart:SeatingClassCost = SeatingClassCost()) -> None:
        self.__capacity = capacityChart
        self.__cost = costChart
    
    def getCost(self, type:str) -> float:
        return self.__cost.get(type)

    def getCapacity(self, type:str) -> int:
        return self.__capacity.get(type)

    def setCost(self, type:str, value:float) -> None:
        return self.__cost.update({ type, value })

    def setCapacity(self, type:str, value:int) -> None:
        return self.__capacity.update({ type, value })

class Train:
    def __init__(self, id:int, name:str = "", coach:CoachStats = CoachStats(), routePerWeek:WeekDist = WeekDist()) -> None:
        self.__id = id
        self.__name = name
        self.__coach = coach
        self.__weekRoute = routePerWeek
    
    def __eq__(self, __o: object) -> bool:
        return self.id() == __o.id()

    def __ne__(self, __o: object) -> bool:
        return self.id() != __o.id()

    def id(self) -> int:
        return self.__id
    
    def name(self) -> str:
        return self.__name
    
    def cost(self, classType:str) -> float:
        return self.__coach.getCost(classType)
    
    def capacity(self, classType:str) -> int:
        return self.__coach.getCapacity(classType)

    def updateCoach(self, coach:CoachStats) -> None:
        self.__coach = coach

    def queryStatus(self, station:Station, currentTime:quanta, day:str) -> StatusReport:
        return StatusReport(self.id(), self.name(), self.__weekRoute.get(day).timeToStation(station))
    
    def updateRoute(self, route:Route, day:str) -> None:
        self.__weekRoute.set(day, route)