# practicing OS automation

import os

for fileName in os.listdir('../download_list'):
    print(fileName)
    aFile = open('../download_list/' + fileName)
    for line in aFile:
        print('\t' + line, end = '')
