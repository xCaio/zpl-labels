import socket
from produtos import etiquetas
from produtos import ribbons

IP = "10.79.1.141"
PORTA = 9100

darkness = 16
speed = 6

zpl_total = ""

"""
    AQUI NO FOR ALTERE PARA "etiquetas" para imprimir todas as etiquetas
    AQUI NO FOR ALTERE PARA "ribbons" para imprimir todos os ribbons
"""
for p in ribbons:
    print(p.get("code"))

    codigo = p.get("code")
    produto = "ETIQUETA"
    if produto == "ETIQUETA":

        estoque = "VERIFICAR SITE"

        url = f"https://stock-frontend-dun-eight.vercel.app/produtos/{codigo}"

        zpl = f"""
        ^XA
        ^MD{darkness}
        ^PR{speed}
        ^PW800
        ^LL560
        ^LH0,0

        ^FO20,20
        ^GB760,520,3^FS

        ^CF0,38
        ^FO50,45
        ^FDESTOQUE VALLOUREC^FS

        ^FO50,95
        ^GB700,3,3^FS

        ^CF0,28

        ^FO50,125
        ^FDCODIGO:^FS

        ^CF0,38
        ^FO190,118
        ^FD{codigo}^FS

        ^CF0,25
        ^FO50,175
        ^FDPRODUTO:^FS

        ^CF0,30
        ^FO50,205
        ^FD{produto}^FS

        ^FO50,255
        ^GB700,2,2^FS

        ^CF0,28
        ^FO50,285
        ^FDESTOQUE ATUAL:^FS

        ^CF0,40
        ^FO300,275
        ^FD{estoque}^FS

        ^CF0,25
        ^FO50,345
        ^FDESCANEIE PARA ACESSAR^FS

        ^FO550,330
        ^BQN,2,5
        ^FDLA,{url}^FS

        ^CF0,20
        ^FO50,510
        ^FDEntrada e saida de estoque^FS
        ^XZ
        """
        zpl_total += zpl
try:
    with socket.create_connection((IP, PORTA), timeout=5) as impressora:
        impressora.sendall(zpl_total.encode("ascii"))


    print("Etiqueta enviada!")

except Exception as e:
    print(f"Erro na etiqueta {codigo}: {e}")