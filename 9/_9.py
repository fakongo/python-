from audioop import reverse
from unittest import result


s = '啊啊啊啊啊啊\n不不不\n踩踩踩踩踩踩踩\n'
with open('sample.txt','w') as fp:
    fp.write(s)
with open('sample.txt') as fp:
    print(fp.read())

with open('sample.txt') as fp:
    for line in fp:
        print(line)

with open('胡晓龙.txt','r') as fp:
    data = fp.readlines()
data = [int(item) for item in data]
data.sort(reverse=True)
data = [str(item)+'\n' for item in data]
with open('胡晓龙.txt','w') as fp:
    fp.writelines(data)
    print(data)

with open('sample.txt') as fp:
    result = [0,'']
    for line in fp:
        t = len(line)
        if t > result[0]:
            result = [t,line]
print(result)