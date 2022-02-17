#sequencia fibonaci
print('Sequencia  de fibonacci')
n=int(input('digite quantos termos quer mostrar: '))
t1=0
t2=1
cont=3
while cont<=n:
    t3=t2+t1
    cont+=1
    print('fibona {}'.format(t3))
    t1=t2
    t2=t3
print('fim')