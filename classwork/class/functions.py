

x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x)

class Truth:
    pass
x=Truth()
print(bool(x))

a = ['hello','morning'][bool('')]
print(a)
b = ['f','t'][bool('msg')]
print(b)

print(not(3>4))
print(not(1&1))

def writer():
    title= 'sir'
    name = (lambda x:title+' '+ x)
    return name
who = writer()
print(who('Arthur'))
writer()
