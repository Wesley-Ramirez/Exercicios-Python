numero = ('zero','um','dois','trez','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','Vinte')
n1 = int(input('Digite um numero de 0 a 20 '))
while n1 < 0:
    n1 = int(input('Valor incorreto , Digite um numero de 0 a 20 '))
    while n1 >= 21:
        n1 = int(input('Valor incorreto , digite um numero de 0 a 20'))
        if n1 <= 20 and n1 >= 0:
            break

print(numero[n1])



