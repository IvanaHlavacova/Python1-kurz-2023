# Vyvíjíš software pro obchod s elektronickými součástkami.
# Firma eviduje informace o počtu součástek na skladě ve slovníku.
# Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
# Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit.
# Obě informace si ulož.

kod = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte požadované množství: "))

# Následně naprogramuj následující varianty:


# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

if kod not in sklad:
    print("Pořadovaná součástka není na skladě.")

# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom,
# že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.

if kod in sklad:
    if mnozstvi > sklad[kod]:
        print(f"Požadoveného zboží máme jen {sklad[kod]} kusů")
        del sklad[kod]

# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši,
# a sniž počet součástek na skladě o množství požadované zákazníkem.
    else:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod] = sklad[kod] - mnozstvi