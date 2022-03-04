#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso(n):
    srt=str(n)
    invert=srt[::-1]
    return invert


num=int(input('Digite um numero inteiro: '))
x=reverso(num)
print(x)
