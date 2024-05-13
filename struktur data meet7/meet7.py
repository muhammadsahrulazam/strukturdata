# tabel kebenaran (logika bolean)
# not and or xor

# NOT

print("***logika NOT***")
x = False
y = not x
print('value x =',x)
print('******NOT')
print('value y =',y)

# OR (semua bernilai true asalkan ada truenya)
# hanya untuk perempuan gatau diri

print("***logika OR***")
x = False
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = False
y = True
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = True
z = x or y
print(x, 'OR', y, '=', z)

# AND (hanya bernilai true, ketika keduanya true)
# hanya berlaku untuk laki laki
print("***logika AND***")
x = False
y = False
z = x or y
print(x, 'AND', y, '=', z)
x = False
y = True
z = x or y
print(x, 'AND', y, '=', z)
x = True
y = False
z = x or y
print(x, 'AND', y, '=', z)
x = True
y = True
z = x or y
print(x, 'AND', y, '=', z)

# XOR (jika keduanya sama hasilnya false, ketika ada true hasinya true dan ketika truenya double maka hasilnya false)
print("***logika XOR***")
x = False
y = False
z = x ^ y
print(x, 'XOR', y, '=', z)
x = False
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)
x = True
y = False
z = x or y
print(x, 'XOR', y, '=', z)
x = True
y = True
z = x ^ y
print(x, 'XOR', y, '=', z)