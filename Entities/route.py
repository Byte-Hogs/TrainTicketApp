from collections import deque
from Entities.station import Station

class quanta (int):
    def __init__(self, value:int) -> None:
        super().__init__(value)

class RoutePoint (object):
    def __init__(self, station:Station, timeDelta:quanta) -> None:
        self.station = station
        self.time = timeDelta

class Route (object):
    def __init__(self, startingStation:Station = Station(), departureTime:quanta = 0) -> None:
        self.__routePoints = deque([ RoutePoint(startingStation, departureTime) ])
        self.__size = 1
    
    def departure(self) -> RoutePoint:
        return self.__routePoints[0]
    
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