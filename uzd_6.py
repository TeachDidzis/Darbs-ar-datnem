with open("Sagatave_vardu_skaits.txt", "r", encoding="utf-8") as datne:
    teksts = datne.read()
    print(teksts)

vardi = teksts.split()
print(vardi)
skaits = len(vardi)
print(f"Vārdu skaits failā: {skaits}")

datne.close()