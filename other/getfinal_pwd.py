base = "3717Odoo"
stmnt = "!Odoo - All your applications in one single solution"
ts = "8868341893302397614270"

# Paso 1: Calcular multi
multi = True
for digit in ts[:5]:
    idx = int(digit) + 1
    multi *= ord(stmnt[idx])
multi_str = str(multi)
prefix = multi_str[1:5] + stmnt[2:6]  # debería dar "7173Odoo"

# Paso 2: Encontrar posibles combinaciones donde x * y == 35
candidatos = []
for x in range(10):
    for y in range(10):
        if x * y == 35:
            candidatos.append((x, y))

# Paso 3: Construir posibles contraseñas
for x, y in candidatos:
    pwd = prefix + "1371751875" + str(x)  # x será el último dígito
    if int(y) == int(prefix[1]):
        print("Posible password:", pwd)