# 1. Izveido programmu, kas nolasa teksta failu un izdrukā tā saturu terminālī.
"""
    1. atver datni
    2. veic darbības 
    3. aizver datni
"""
with open("new 1.txt", "r", encoding="utf-8") as datne:
    saturs = datne.readlines()
    print(saturs)

    for x in saturs:
        rinda = x.split(",")
        print(*rinda)

datne.close()