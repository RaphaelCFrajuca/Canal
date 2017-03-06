# imports
try:
    import socket
    import sys
except Exception as e:
    print("Erro ao importar as dependencias!")
    exit()

# Abrir socket
print("Abrindo Socket")
connection = socket.socket()

# Conectar ao socket 
print("Conectando...")
connection.connect(("recargafacil.claro.com.br", 80))

# Enviar request 
print("Enviando request")
connection.send("GET / HTTP/1.1\r\nHost: google.com.br\r\n\r\n".encode(encoding='utf_8', errors='strict'))

# Receber resposta
print("Recebendo Resposta...")
resposta = connection.recv(1024).decode()

print("Resposta:\n" + resposta)
