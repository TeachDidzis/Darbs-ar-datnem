with open("Sagatave_reverss.txt", "r", encoding="utf-8") as datne:
    rindas = datne.readlines()

with open("Sagatave_reverss.txt", "w", encoding="utf-8") as datne:
    for rinda in reversed(rindas):
        datne.write(rinda)
        print(rinda)

datne.close()



