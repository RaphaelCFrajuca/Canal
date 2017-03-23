#!/usr/bin/python3

# Obs: Temque ser em python3 porque o BadManager usa o Python3.

# Vamos importar todos os modulos que o BadManager usa.

# Os modulos que ele importa sao usados com o comando "import MODULO-A-IMPORTAR".
try:
# Lembrando: em todos os blocos com ":" no final as linhas correspondentes devem ter um espaco para separar elas das linhas principais.
	import os
	import platform
	import sys
	import subprocess
# Explicando um pouco melhor o bloco try:, ele vai tentar fazer os comandos que mandamos dentro do bloco, e caso ele nao consiga, ele vai fazer outra acao, e para isso entra o bloco expect: que e um complemento do try:
except Exception:
# Agora aqui colocamos a mensagem de erro:
	print("Erro ao importar modulos!")
# Caso isto seja executado, o script deve sair imediatamente com o comando exit()
	exit()

# Pronto, fizemos o primeiro bloco, agora caso ele nao consiga importar os modulos principais, ele ira mostrar este erro.


# Agora que importamos todos os modulos, vamos usar o path do BadManager.
# É só copiar a linha 27 e colar aqui.

sys.path.insert(0, "/etc/BadManager/")

# Agora ja podemos importar os modulos do BadManager.
# Só copiar as linhas 28 a 33.

# Agora vamos usar o bloco try: aqui para que o script tente importar os scripts do BadManager, e caso nao consiga emita um erro.
try:
	from criarusuario import criarusuario
	from deletarusuario import deletarusuario
	from limite import limite
	from backupusuario import backupusuario
	from debbackup import deb
	from servidor import configurar
except Exception:
	print("Erro ao importar modulos do BadManager, certeza que tem ele instalado?")
	exit()

# Pronto, o modulo do BadManager ja esta dentro do bloco try, agora eu vou tirar o BadManager para que aconteca um erro, e voces irao ver o bloco try: em acao.
# Esqueci de colocar uma coisa no bloco except:
# Voces devem executar ele assim:
# except Exception:



# Certo, agora vamos executar o script, se ele estiver sem saida é porque ele importou todos os modulos com sucesso.

# Vamos primeiro fazer um menu aonde o usuario seleciona a opçao que quer executar.

# Para exibir coisas na tela com o Python, devemos usar o "print("CONTEUDO")"

print("1 - Criar um usuario")
print("2 - Deletar um usuario")

# Agora vamos fazer com que o script salve a entrada do usuario, com o "input"
# Vamos colocar o valor doque o usuario selecionar dentro de uma string

# Como criar strings:
# nomedastring = "valor"

# Neste caso o nome da string vai ser "entrada"

entrada = input("Digite o numero da opçao: ")

# Agora que sabemos oque o usuario vai selecionar, vamos transformar o valor da string para numeros, que vamos usar para saber qual funçao executar. para isso usamos o "int(string)"

# Vamos manter isto dentro da string "entrada"

# Aqui pode acontecer um erro caso o usuario digite letras ao inves de numeros, vamos usar o try:
try:
	entrada = int(entrada)
except Exception:
	print("Por favor digite um numero valido!")
	exit()

# Vamos testar!

# Como podem ver, eu repeti o valor da string "entrada" dentro do int, porque a entrada ja tinha sido atribuida um valor, entao nao tem problema fazer deste modo.

# Agora que temos o valor em numero doque o usuario digitou, vamos criar as opçoes.
# Vamos usar comparaçoes para saber qual a opçao certa a executar

# Para isso usamos o "if" do python3, ele serve para (basicamente falando) comparar objetos e caso a comparaçao seja verdadeira (ou nao) executar uma açao.

# O modo de uso é bem simples, vou usar a primeira comparaçao.

if entrada == 1:
# Obs: Sempre quando usamos blocos que terminam com ":", devemos dar um espaço para separar o texto do main para dentro do bloco.
	# Agora finalmente vamos chamar a primeira funçao do BadManager, que é a de criar usuarios no sistema, para chamar ela devemos fazer desta forma:
	criarusuario.criarusuario()

# E pronto, a primeira opçao esta definida, agora o resto fica com o BadManager, agora vamos fazer o mesmo com a segunda opçao (deletar usuario), mas desta vez nao vou usar exemplos.

if entrada == 2:
	deletarusuario.deletarusuario()

# Pronto, agora vamos testar como ficou.

# Hoje vamos usar algumas coisas para se assegurar que caso venha a acontecer erros no script, seja mostrado de uma forma mais amigavel ao usuario, para isso iremos usar o bloco try:

# Vamos colocar ele nos imports, desta maneira como vou fazer agora:


# Entao e isso pessoal, muito obrigado por assistir o video, deixe o like caso gostou, e se inscreva no canal caso nao for inscrito, compartilhe o video com amigos que precisem, bye :P
