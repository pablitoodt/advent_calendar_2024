data = open("day_4/input.txt").read().strip()
lignes = data.split("\n")
liste_finale = [list(ligne) for ligne in lignes]

def verif_h_rtl(data):
    cpt = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i]) - 3):
            if data[i][j] == "X" and data[i][j + 1] == "M" and data[i][j + 2] == "A" and data[i][j + 3] == "S":
                cpt += 1
    return cpt

def verif_h_ltr(data):
    cpt = 0
    for i in range(0, len(data)):
        for j in range(len(data[i]) - 1, 2, -1):
            if data[i][j] == "X" and data[i][j - 1] == "M" and data[i][j - 2] == "A" and data[i][j - 3] == "S":
                cpt += 1
    return cpt

def verif_v_ttb(data):
    cpt = 0
    for i in range(0, len(data) - 3):
        for j in range(0, len(data[i])):
            if data[i][j] == "X" and data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
                cpt += 1
    return cpt

def verif_v_btt(data):
    cpt = 0
    for i in range(len(data) - 1, 2, -1):
        for j in range(0, len(data[i])):
            if data[i][j] == "X" and data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
                cpt += 1
    return cpt

def verif_drb(data):
    cpt = 0
    for i in range(0, len(data) - 3):
        for j in range(0, len(data[i]) - 3):
            if data[i][j] == "X" and data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
                cpt += 1
    return cpt

def verif_drt(data):
    cpt = 0
    for i in range(len(data) - 1, 2, -1):
        for j in range(0, len(data[i]) - 3):
            if data[i][j] == "X" and data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
                cpt += 1
    return cpt

def verif_dlb(data):
    cpt = 0
    for i in range(0, len(data) - 3):
        for j in range(len(data[i]) - 1, 2, -1):
            if data[i][j] == "X" and data[i + 1][j - 1] == "M" and data[i + 2][j - 2] == "A" and data[i + 3][j - 3] == "S":
                cpt += 1
    return cpt

def verif_dlt(data):
    cpt = 0
    for i in range(len(data) - 1, 2, -1):
        for j in range(len(data[i]) - 1, 2, -1):
            if data[i][j] == "X" and data[i - 1][j - 1] == "M" and data[i - 2][j - 2] == "A" and data[i - 3][j - 3] == "S":
                cpt += 1
    return cpt


def day4_part1(liste_finale):
    compteur = 0

    compteur += verif_h_rtl(liste_finale)
    compteur += verif_h_ltr(liste_finale)
    compteur += verif_v_ttb(liste_finale)
    compteur += verif_v_btt(liste_finale)
    compteur += verif_drb(liste_finale)
    compteur += verif_drt(liste_finale)
    compteur += verif_dlb(liste_finale)
    compteur += verif_dlt(liste_finale)

    return compteur

print(day4_part1(liste_finale))



def verif_2_ttb(data):
    cpt = 0
    for i in range(0, len(data) - 2):
        for j in range(0, len(data[i]) - 2):
            if data[i][j] == "M" and data[i + 1][j + 1] == "A" and data[i + 2][j + 2] == "S" and data[i][j + 2] == "M" and data[i + 2][j] == "S":
                cpt += 1
    return cpt

def verif_2_btt(data):
    cpt = 0
    for i in range(len(data) - 1, 1, -1):
        for j in range(0, len(data[i]) - 2):
            if data[i][j] == "M" and data[i - 1][j + 1] == "A" and data[i - 2][j + 2] == "S" and data[i][j + 2] == "M" and data[i - 2][j] == "S":
                cpt += 1
    return cpt

def verif_2_ltr(data):
    cpt = 0
    for i in range(0, len(data) - 2):
        for j in range(0, len(data[i]) - 2):
            if data[i][j] == "M" and data[i + 1][j + 1] == "A" and data[i + 2][j + 2] == "S" and data[i + 2][j] == "M" and data[i][j + 2] == "S":
                cpt += 1
    return cpt

def verif_2_rtl(data):
    cpt = 0
    for i in range(0, len(data) - 2):
        for j in range(len(data[i]) - 1, 1, -1):
            if data[i][j] == "M" and data[i + 1][j - 1] == "A" and data[i + 2][j - 2] == "S" and data[i][j - 2] == "S" and data[i + 2][j] == "M":
                cpt += 1
    return cpt

def day4_part2(liste_finale):
    compteur = 0

    compteur += verif_2_ttb(liste_finale)
    compteur += verif_2_btt(liste_finale)
    compteur += verif_2_ltr(liste_finale)
    compteur += verif_2_rtl(liste_finale)

    return compteur

print(day4_part2(liste_finale))
