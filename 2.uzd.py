# Izveidojiet Python programmu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kubs ir lielāks par 3000.


skaitlis = 1

# Meklējam pirmo skaitli, kura kubs ir lielāks par 3000
while skaitlis**3 <= 3000:
    skaitlis += 1

# Izvadam rezultātu
print(f"Pirmāis skaitlis, kura kubs ir lielāks par 3000, ir: {skaitlis}")
