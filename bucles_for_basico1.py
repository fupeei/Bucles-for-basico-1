for num in range (0,151):
    print(num)

print('-----')

for num in range (5,1001,5):
    print(num)

print('-----')

for num in range (1,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

print('-----')

resultado = 0
for num in range (0,500000):
    if num % 2 != 0:
        resultado += num
print(resultado)

print('-----')
    
for num in range (2018,0,-4):
    print(num)

print('-----')

lowNum = 2
highNum = 9
mult = 3
for num in range (2,10):
    if num % 3 == 0:
        print(num)