with open("Sagatave_rindu_skaits.txt", "r", encoding="utf-8") as datne:
    dati = datne.readlines()

    print(dati)

    for x in dati:
        rindas = x.split("\n")
        skaits = len(dati)

        print(*rindas)
    print(f"Rindu skaits: {skaits}")

datne.close()