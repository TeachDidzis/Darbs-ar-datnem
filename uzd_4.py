with open("Jauns fails.txt", "w", encoding="utf-8") as datne:
    datne.write("Šis ir jauns fails")

datne.close()
"""
Atver izveidoto datni un izvada konsolē tās saturu

with open("Jauns fails.txt", "r", encoding="utf-8") as datne:
    saturs = datne.readlines()
    print(saturs)

datne.close()
"""