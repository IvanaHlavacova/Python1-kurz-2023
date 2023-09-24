domena = "@czechitas.cz"
jmeno = "Ivana"
email = jmeno + domena

print (email)

""""
BONUS
"""

jmeno = input("Zadejte sve krestni jmeno: ")
prijmeni = input("Zadejte sve prijmeni: ")

print(jmeno.upper() + " " + prijmeni.upper())
print(jmeno.lower() + " " + prijmeni.lower())
print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
print(jmeno[0].upper() + ". " + prijmeni[0].upper() + ".")

delka_jmena = len(jmeno)

if delka_jmena > 5:
    print(jmeno[0].upper() + ". " + prijmeni[0].upper() + prijmeni[1:].lower())
    
else:
    print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())