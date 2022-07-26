import os
from subprocess import check_output


dados = ""
teste = []
for line in os.popen('systeminfo'):
    print(line)
    dados += f'{line.strip().replace("‡","ç").replace("“", "ó").replace("¡", "í").replace("Æ", "ã").replace(":                     "," : "). replace(":         ", " : ").replace(":      ", "")}\n'

# comando para visualizar o uuid no pc    ---- (wmic csproduct get UUID) -----
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = os.open(os.devnull, os.O_RDWR)
uuid = check_output('wmic csproduct get uuid', stdin=DEVNULL, stderr=DEVNULL).decode().split('\n')[1].split(' ')[0]


a = {'Info':dados}


print(dados)
print(uuid)