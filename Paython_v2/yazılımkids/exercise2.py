x = 5
y = "Barış"
z = 3.14

print(type(x))
print(type(y))
print(type(z))

a = "GALATASARAY"
b = "BARIŞ YAVUZDİLER"
c = 1905


print(x, y, z)
print(a, b, c)

v = "fantastic"

def merhaba():
    global v
    v = "harika"
    merhaba()
print("Python " + v)

def merhabal():
    global m
    m = "harika"
merhabal()
print("Python " + m)