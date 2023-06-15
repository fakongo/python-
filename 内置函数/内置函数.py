x='Kongo.'
print(len(x),max(x),min(x))
print(list(zip(x,x)))
print(sorted(x))
print(' '.join(reversed(x)))
print(list(enumerate(x)))
def add(ch1,ch2):
    return ch1+ch2
print(list(map(add,x,x)))
