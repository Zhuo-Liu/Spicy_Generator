import numpy as np
import pandas as pd
import random
import xlwt

path = r'./post6.xlsx'

data = pd.read_excel(path)
data = data.dropna()
URL = data['URL'].values
Name = data['Name'].values
Post_Type = data['PostType'].values
N = len(Name)

i = 0
data_list = []
while i< N:
    if Post_Type[i] == 'Post':
        temp = [URL[i],Name[i]]
        data_list.append(temp)
    i=i+1

Name_list = [entry[1] for entry in data_list]
Name_set = set(Name_list)

results = {}

for name in Name_set:
    temp_url_list= [entry[0] for entry in data_list if entry[1] == name] 
    leng = len(temp_url_list)
    if leng >= 5:
        random_list = random.sample(range(0,leng),5)
    else:
        random_list = range(0,leng)
    ans = []
    for k in random_list:
        ans.append(temp_url_list[k])

    results[name] = ans

p = './posts_6_result.xls'
# f = open(p,'w',encoding='utf-8')
# for k,v in results.items():
#     f.write(k+'\n')
#     for entry in v:
#         f.write(str(entry))
#         f.write(',')
#     f.write('\n')
#     f.write('\n')
# f.close()


# workbook = xlwt.Workbook()
# sheet = workbook.add_sheet('facebook_url')
# j=0
# for k,v in results.items():
#     i = 0
#     sheet.write(i,j,k)
#     i = i+1
#     for entry in v:
#         sheet.write(i,j,entry)
#         i = i+1
#     j = j+1
# workbook.save(p)

# workbook = xlwt.Workbook()
# sheet = workbook.add_sheet('facebook_url')
# j=0
# for k,v in results.items():
#     i = 0
#     sheet.write(i,j,k)
#     j = j+1
#     for entry in v:
#         sheet.write(i,j,entry)
#         i = i+1
#     j = j+1
# workbook.save(p)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('facebook_url')
i = 0
for k,v in results.items():
    j = 0
    sheet.write(i,j,k)
    j = j + 5
    for entry in v:
        sheet.write(i,j,entry)
        i = i + 1
workbook.save(p)




