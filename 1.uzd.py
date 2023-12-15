#Izveidojiet Python programmu, kas saskaita no 13 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

# Lietotājs ievada skaitli
lietotaja_ievade = int(input("Ievadiet skaitli: "))

# Inicializējam summu
summa = 0

# Saskaita no 13 līdz ievadītajam skaitlim
for i in range(13, lietotaja_ievade + 1):
    summa += i

# Izvada rezultātu
print(f"Summa no 13 līdz {lietotaja_ievade} ir {summa}")
