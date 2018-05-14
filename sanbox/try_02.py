# practicing OS automation

import os

for fileName in os.listdir('../download list'):
    print(fileName)
    aFile = open('../download list/' + fileName)
    for line in aFile:
        print('\t' + line, end = '')
