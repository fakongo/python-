'''import urllib.request
fp=urllib.request.urlopen(r'https://www.python.org/')
print(fp.read(100))
print(fp.read(100).decode())
fp.close()
'''

import urllib.request
import urllib.parse
params=urllib.parse.urlencode({'spam':1,'eggs':2,'bacon':0})
url="https://mp.weixin.qq.com/s/P9Wke8FSNPxOvfLyaPcv8Q" % params
with urllib.request.urlopen(url) as f:print(f.read().decode('utf-8'))


'''
from re import findall
from urllib.request import urlopen
url='https://store.steampowered.com/'
with urlopen(url)as fp:
    content=fp.read().decode()
pattern = 'data-type="ico" data-src="(.+?)"'
result=findall(pattern,content)
for index,item in enumerate(result):
    with urlopen(str(item)) as fp:
        with open(str(index)+'.ico','wb') as fp1:
            fp1.write(fp.read())
'''
'''
from re import findall
from urllib.request import urlopen

url='https://mp.weixin.qq.com/s/P9Wke8FSNPxOvfLyaPcv8Q'

with urlopen(url) as fp:content = fp.read().decode()

pattern = ' data-type="png" data-src="(.+?)"'
result = findall(pattern, content)

for index,item in enumerate(result):
    with urlopen(str(item)) as fp:
        with open(str(index)+'.png','wb') as fp1:
            fp1.write(fp.read())
'''