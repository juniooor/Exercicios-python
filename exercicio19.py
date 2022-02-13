from msilib.schema import Binary


num=int(input('digite um numero inteiro: '))
op=str(input('Digite 1 para binario 2 para hexadecimal e 3 para octal : '))
if op == 1:
    Binary=bin(num)
    print(Binary)
elif op == 2: 
    hexa=hex(num)
    print(hexa)
else:
    octal=oct(num)
    print(octal)
    