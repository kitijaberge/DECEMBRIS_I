# Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
# ievada skaitli
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

# faktoriāla vērtība
faktorials = 1

# Aprēķina faktoriālu, izmantojot for ciklu
for i in range(1, ievaditais_skaitlis + 1):
    faktorials *= i

# Izvadam rezultātu
print(f"Faktoriāls no {ievaditais_skaitlis} ir {faktorials}")
