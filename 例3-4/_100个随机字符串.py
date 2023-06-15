'''
import string
import random
# 生成包含1000个随机字符的字符串
x = string.ascii_letters+string.digits
z = ''.join((random.choice(x) for i in range(1000)))

# 统计每个字符串的出现次数
d= dict()
for ch in z:
    d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(k,':',v)
'''
import random
import string
from collections import Counter

# 生成包含1000个随机字符的字符串
random_string = ''.join(random.choices(string.ascii_letters, k=1000))

# 统计每个字符串的出现次数
count_string = Counter(random_string)

# 针对每一个字符串，将字符串和它的出现次数组合成一个新的字符串表示
string_counts = [s + ': ' + str(c) for s, c in count_string.items()]

# 隔行输出
for i in range(0, len(string_counts), 2):
    print(string_counts[i])
    if i + 1 < len(string_counts):
        print(string_counts[i + 1])
    print()