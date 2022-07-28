import csv

with open('versao_final/game/maps/map1.csv','r') as current_map:
    csv.reader(current_map)
    map_array = list(current_map)
    print(map_array)
