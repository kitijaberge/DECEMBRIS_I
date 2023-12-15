# Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)

import datetime

# Iegūstam pašreizējo stundu
pašreizējā_stunda = datetime.datetime.now().hour

# Izvada atbilstošu sveicienu
if 6 <= pašreizējā_stunda < 12:
    print("Labrīt!")
elif 12 <= pašreizējā_stunda < 18:
    print("Labdien!")
else:
    print("Labvakar!")
