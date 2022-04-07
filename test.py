from Entities.station import Station, LinkStations

stay = Station(2, "no")
stay1 = Station(3, "yes")
stay2 = Station(1, "maybe")
# stay2 = Station(1, "maybe", [ stay, stay1 ])

try:
    stay1.addNeighbour(stay)
# stay2.addNeighbour(stay2)
# LinkStations(stay, stay2)
# LinkStations(stay1, stay2)
except Station.NeighbourException as e:
    print('caught neighbour exception:', e)
    exit(2)
except:
    print('Caught unknown exception')
    exit(1)

print(stay)
print(stay1)
print(stay2)

print("\nneighbours")

for s in (stay, stay1, stay2):
    print("\n" + str(s), end = ": ")
    # print(s.neighbours())
    for neighbour in s.neighbours():
        print(neighbour, end = "\t")