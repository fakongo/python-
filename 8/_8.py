import re
text='''Suppose my Phone No.is 0535-1234567,
        yours is 010-12345678,
        his is 025-87654321'''
matchRe=re.findall(r'(\d{3,4})-(\d{7,8})',text)
for item in matchRe:
    print(item[0],item[1],sep='-')

import re
def longest1(s):
    '''查找所有连续的数字'''
    t = re.findall('\d+',s)
    if t:
        return max(t,key=len)
    return'No'
def longest2(s):
    '''使用非数字作为分隔符'''
    t = re.split('[^\d]+',s)
    if t:
        return max(t,key=len)
    return'No'

import re
def reverse(s):
    t=re.split('\s+',s.strip())
    t.reverse()
    return ' '.join(t)
print(reverse('i like guangzhou.'))
print(reverse('Simple is better than complex.'))