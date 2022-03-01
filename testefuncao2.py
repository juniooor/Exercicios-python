'''def somar(a=0,b=0,c=0):
    s=a+b+c
    return s

r1=somar(2,3,5)
r2=somar(3,3)
r3=somar(10)

print(f'resultados {r1}, {r2}, {r3}') 

'''
def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f*=c
    return f


n=int(input("digite um numero: "))
print(f'o fatorial de {n} é {fatorial(n)}')



