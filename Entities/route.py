from collections import deque
from station import Station

class quanta (int):
    def __init__(self, value:int, unit:str) -> None:
        super().__init__()
        
        if unit in ('s', 'seconds'):
            self.__d = 86400
            self.__h = 3600
            self.__m = 60
            self.__s = 1
        
        elif unit in ('m', 'minutes'):
            self.__d = 1440
            self.__h = 60
            self.__m = 1
            self.__s = 1 / 60
    
        elif unit in ('h', 'hours'):
            self.__d = 24
            self.__h = 1
            self.__m = 1 / 60
            self.__s = 1 / 3600
        elif unit in ('h', 'hours'):
            self.__d = 1
            self.__h = 60 / 24
            self.__m = 1 / 1440
            self.__s = 1 / 86400
    
    def days(self) -> float:
        return self / self.__d
    
    def hours(self) -> float:
        return self / self.__h
    
    def minutes(self) -> float:
        return self / self.__m
  
    def seconds(self) -> float:
        return self / self.__s
    
    def clock(self) -> list:
        x = self
        
        clock = [ int(x // self.__d) ]
        x -= clock[0] * self.__d
        
        clock.append( int(x // self.__h) )
        x -= clock[1] * self.__h
        
        clock.append( int(x // self.__m) )
        x -= clock[2] * self.__m
        
        clock.append( int(x // self.__s) )
        x -= clock[3] * self.__s

        return clock

    def __str__(self):
        chronos = self.clock()
        return str(chronos[0]) + " days " + str(chronos[1]) + " hours " + str(chronos[2]) + " minutes " + str(chronos[3]) + " seconds"

class RoutePoint (object):
    def __init__(self, station:Station, timeDelta:quanta) -> None:
        self.station = station
        self.time = timeDelta

class Route (object):
    def __init__(self, startingStation:Station = Station(), departureTime:quanta = 0) -> None:
        self.__routePoints = deque([ RoutePoint(startingStation, departureTime) ])
        self.__size = 1
    
    def __str__(self) -> str:
        return str(self.__routePoints[0].station) + " to " + str(self.__routePoints[-1].station)

    def departure(self) -> RoutePoint:
        return self.__routePoints[0]
    
    def finalStation(self) -> Station:
        return self.__routePoints[-1].station

    def size(self) -> int:
        return self.__size

    def append(self, newRoutePoint:RoutePoint) -> bool:
        endStation = self.__routePoints[-1].station

        if endStation.isNeighbour(newRoutePoint.station):
            self.__routePoints.append(newRoutePoint)
            self.__size += 1
            return True
        
        return False
    
    def insert(self, newRoutePoint:RoutePoint, index:int) -> bool:
        _prev = self.__routePoints[index]
        _next = self.__routePoints[index + 1]

        if newRoutePoint.time < _next.time and _prev.station.isNeighbour(newRoutePoint.station) and _next.station.isNeighbour(newRoutePoint.station):
            self.__routePoints[index + 1].time -= newRoutePoint.time
            self.__routePoints.insert(index, newRoutePoint)
            self.__size += 1
            return True
        
        return False
    
    def remove(self, deadStation:Station) -> bool:
        for rp in self.__routePoints:
            if rp.station == deadStation:
                self.__routePoints.remove(rp)
                return True
        
        return False

    def progress(self) -> bool:
        if self.size() == 1: return False

        current = self.__routePoints.popleft()
        self.__size -= 1
        self.__routePoints[0].time += current.time

        return True

    def timeToStation(self, station:Station) -> quanta:
        time = quanta(0)

        for rp in self.__routePoints:
            if rp.station == station: return time
            time += rp.time
        
        return quanta(-1)
    
    def reversed(self, departureTime:quanta):
        backTrace = self.__routePoints.copy()
        backTrace.reverse()
        
        for index in range(self.size() - 1):
            backTrace[index + 1].time = backTrace[index].time
        
        backTrace[0].time = departureTime
        return backTrace