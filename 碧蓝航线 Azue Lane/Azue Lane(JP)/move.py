from os import listdir, replace
from os.path import isfile, join
import re

mypath = '.'
regex = re.compile('^icon_(.+)\.png$')
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and regex.search(f)]
for file in onlyfiles:
    modelName = regex.search(file).group(1)
    print(modelName)
    try:
        replace(file, modelName + '/' + file)
    except FileExistsError as e:
        print('file exists: ' + file)