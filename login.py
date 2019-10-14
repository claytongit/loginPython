import time

nome = str(input('Informe seu nome: ')).lower().capitalize()
print()
password = str(input('Informe uma senha: '))
print()

print('//////////////////////////////////////////////////////')
print('Ola {} sua conta foi criada com sucesso!'.format(nome))
print()
print('Informe seu nome de usuario e senha ')
print('//////////////////////////////////////////////////////')

print()
usuario = str(input('Usuario: '))
print()
senha = str(input('Senha: '))

print()
print('Fazendo login aguarde....')
time.sleep(3)
print()

if password == senha:
    print('Login feito com sucesso! usuario {}, senha {}'.format(nome, password))
else:
    print('Senha ou usuario incorreto. Tente novamente')
