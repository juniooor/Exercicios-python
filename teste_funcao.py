'''def soma(a, b):
    print(f'A={a} B={b}')
    s = a + b
    print(f'A soma de A+B={s}')

soma(4, 8)
soma(3, 2)
soma(6, 9)

def contador(*num):
    tam=len(num)
    print(f'Recebi os valores de {num} e são {tam} numeros')    


contador(1, 2, 6, 7, 8)
contador(6, 8, 2)
contador(1, 6)'

def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *=2
        pos+=1
        

valores=[6,7,3,5,7]
dobra(valores)
print(valores)'''
