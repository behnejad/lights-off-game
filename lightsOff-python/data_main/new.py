file_temp = open('edit.txt', 'r')
file_temp_core = file_temp.read()
file_temp.close()
level_map = []
num_level = int(len(file_temp_core)/25)
for i in range(num_level):
    level_map.append([])
    for j in range(5):
        level_map[i].append([])
        for k in range(5):
            level_map[i][j].append(int(file_temp_core[i*25 + j*5 + k]))

print level_map
