
import csv

with open('versao_final/game/maps/map1.csv','r') as current_map:
    csv.reader(current_map)
    map_array = list(current_map)
    for i in range(0, len(map_array)):
        map_array[i] = map_array[i].split(',')
    
    print(map_array)
