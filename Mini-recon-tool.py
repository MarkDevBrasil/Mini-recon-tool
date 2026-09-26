import requests
import socket

print("=== Mini Recon Tool ===")
print("1 - Escanear portas")
print("2 - Verificar headers de segurança")
portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 8080, 8443]
header = ("") 

opcao = input("Escolha uma opção: ")
if opcao == "1":
    site = input("Coloqueo site aqui: ")
    for porta in portas:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultado = conexao.connect_ex((site, porta))
        if resultado == 0:
            print(f"Porta {porta}: ABERTA")
        else:
            print(f"Porta {porta}: fechada")
elif opcao == "2":
    site = input("Coloque o site: ")
    resposta = requests.get(site)
    headers_seguranca = ["Strict-Transport-Security", "X-Frame-Options"]
    for header in headers_seguranca:
        if header in resposta.headers:
            print(f"{header}: presente")
        else:
            print(f"{header}: AUSENTE")
else:
    print("Essa opcao nao e aceita")
    

verificar_de_novo = input("Quer verificar outro site S/N? ").strip().lower()
while verificar_de_novo == "s":
    site = input("Coloque o site: ").strip()

    if opcao == "1":
        for porta in portas:
            conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            resultado = conexao.connect_ex((site, porta))
            conexao.close()
            if resultado == 0:
                print(f"Porta {porta}: ABERTA")
            else:
                print(f"Porta {porta}: fechada")
    elif opcao == "2":
        resposta = requests.get(site)
        headers_seguranca = ["Strict-Transport-Security", "X-Frame-Options"]
        for header in headers_seguranca:
            if header in resposta.headers:
                print(f"{header}: presente")
            else:
                print(f"{header}: AUSENTE")

    verificar_de_novo = input("Quer verificar outro site S/N? ").strip().lower()