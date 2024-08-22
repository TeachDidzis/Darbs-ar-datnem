with open("Sagatave_apvienosana_1.txt", "r", encoding="utf-8") as datne, open("Sagatave_apvienosana_2.txt", "r", encoding="utf-8") as datne2, open("Apvienotais_fails.txt", "w", encoding="utf-8") as kopa:
    kopa.write(datne.read())
    kopa.write("\n")
    kopa.write(datne2.read())

datne.close(), datne2.close(), kopa.close()