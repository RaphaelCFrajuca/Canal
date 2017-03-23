#!/usr/bin/python3

# Obs: Temque ser em python3 porque o BadManager usa o Python3.

# Vamos importar todos os modulos que o BadManager usa.

# Os modulos que ele importa sao usados com o comando "import MODULO-A-IMPORTAR".
import os
import platform
import sys
import subprocess

# Agora que importamos todos os modulos, vamos usar o path do BadManager.
# É só copiar a linha 27 e colar aqui.

sys.path.insert(0, "/etc/BadManager/")

# Agora ja podemos importar os modulos do BadManager.
# Só copiar as linhas 28 a 33.
from criarusuario import criarusuario
from deletarusuario import deletarusuario
from limite import limite
from backupusuario import backupusuario
from debbackup import deb
from servidor import configurar

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

entrada = int(entrada)

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
