import re

file = '../data/keyword-extraction-datasets-master/keyword-extraction-datasets-master/fao30/documents/a0011e00.txt'
fr = open(file)
i = 0
for obj in fr:
    obj = obj.strip().split(' ')
    pattern = re.compile('\W')
    if len(obj) > 3:
        print obj
        for i in range(len(obj)):
            obj[i] = pattern.sub('', obj[i])
        print obj
        i = i + 1

print i
