def escreva(msg):
    print('~~' * len(msg))
    print(msg.center(len(msg) * 2))
    print('~~' * len(msg))


msg = str(input('Digite a mensagem: '))
escreva(msg)