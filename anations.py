import os


classes = {'Class_1': 0, 'Class_2': 1, 'Class_3': 2, 'Class_4': 3, 'Class_5': 4, 'Class_6': 5, 'Class_7': 6}
# вывести текущую директорию

print("Текущая деректория:", os.getcwd())

if not os.path.isdir("anations"):
     os.mkdir("anations")

# os.chdir("folder")


def transform_coords(coords):
    print(coords)
    return [coords[0], ' '.join(list(map(lambda i: str(int(i) / 2101), coords[1:])))]


spisoc = os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_txt_1')
spisoc_jpg = list(map(lambda i: i[:-8], os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_1')))

for i in spisoc:
    if i[:-4] in spisoc_jpg:
        os.chdir("TC-Satellite-DataSet-main")
        os.chdir("TC_by_Classes_txt_1")
    
        with open(i) as f:
            line = f.readlines()
            line = [i[:-1].split(', ') for i in line]

        line = [transform_coords(i) for i in line ]
        for j in range(len(line)):
            line[j][0] = str(classes[line[j][0]])
            line[j] = ' '.join(line[j])
        line = '\n'.join(line)

        os.chdir("..")
        os.chdir("..")
        os.chdir("anations")

        with open(i[:-4] + '_pro.txt', 'w') as f:
            f.write(line)

        os.chdir("..")

spisoc_jpg = list(map(lambda i: i[:-8], os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_2')))


for i in spisoc:

    if i[:-4] in spisoc_jpg:

        os.chdir("TC-Satellite-DataSet-main")
        os.chdir("TC_by_Classes_txt_1")
    
        with open(i) as f:
            line = f.readlines()
            line = [i[:-1].split(', ') for i in line]

        line = [transform_coords(i) for i in line ]
        for j in range(len(line)):
            line[j][0] = str(classes[line[j][0]])
            line[j] = ' '.join(line[j])
        line = '\n'.join(line)

        os.chdir("..")
        os.chdir("..")
        os.chdir("anations")

        with open(i[:-4] + '_pro.txt', 'w') as f:
            f.write(line)

        os.chdir("..")

print('анатации готовы')



    

          
     