import os
import shutil

print("Текущая деректория:", os.getcwd())

if not os.path.isdir("image"):
     os.mkdir("image")


spisoc_txt = list(map(lambda i: i[:-4], os.listdir('anations')))
spisoc = os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_1')
spisoc_jpg = list(map(lambda i: i[:-8], os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_1')))


for i in spisoc:
     # print(i[:-8])
     if i[:-4] in spisoc_txt:
          shutil.copy(f'TC-Satellite-DataSet-main/TC_by_Classes_jpg_1/{i}', 'image')

spisoc = os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_2')
spisoc_jpg = list(map(lambda i: i[:-8], os.listdir('TC-Satellite-DataSet-main/TC_by_Classes_jpg_2')))


for i in spisoc:
     # print(i[:-8])
     if i[:-4] in spisoc_txt:
          shutil.copy(f'TC-Satellite-DataSet-main/TC_by_Classes_jpg_2/{i}', 'image')
