import csv
# Nolasa csv datnes saturu un izvada formatēti konsolē
with open("Filmas.csv", "r", newline="") as filmas:
    saturs = csv.reader(filmas, delimiter=",", quotechar='"')

    for x in saturs:
        print(*x, sep="\n")
filmas.close()
#pievieno csv datnei jaunu ierakstu
with open("Filmas.csv", "a", newline="") as filmas:
    jaunaRinda = csv.writer(filmas)

    jaunaRinda.writerow("Jauna rinda")
