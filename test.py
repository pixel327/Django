""" TP 1 """
""" Exercice 1"""
def ex1():
    poids = float(input("Saisir un poids en kg"))
    taille = float(input("Saisir une taille en cm"))/100
    imc = poids / taille ** 2
    print("imc : ",imc)
    if imc < 16.5:
        print("famine")
    elif imc >= 16.5 and imc < 18.5:
        print("Maigreur")
    elif imc >= 18.5 and imc < 25 : 
        print("Corpulence normal")
    elif imc >= 25 and imc < 30:
        print("Surpoids")
    elif imc >= 30 and imc < 35:
        print("Obesité modérée")
    elif imc >= 35 and imc < 40:
        print("Obésité sévère")
    elif imc >= 40:
        print("Obésité morbide ou massive")
""" Exercice 2 """
def ex2():
    chaine = input("Saisir une chaine : ")
    print("chaine avant inversion :", chaine)

    # chaine_inverse = ""
    # for c in chaine:
    #     chaine_inverse = c + chaine_inverse
    # return chaine_inverse

    if len(chaine) % 7 == 0:
        chaine = chaine[::-1]

    print("chaine apres inversion :", chaine)
""" Exercice 3 """
def ex3():
    c=input("Saisir un text")
    compt = 0 
    if len(c) >= 4:
        for i in range(len(c)):
            if i > 3:
                break
            if c[i].isupper():
                compt+=1
    if compt >= 2:
        c = c.upper()
""" Exercice 4 """
def ex4():
    vehicule = ["train","bus","voiture","vélo"]
    couleurs = ["rouge","vert","bleu","jaune"]

    lst=[]
    for i in range(len(vehicule)):
        for j in range(len(couleurs)):
            if (vehicule[i] == "voiture" and couleurs[j] != "vert") or vehicule[i] != "voiture":
                lst.append(vehicule[i] + " "+couleurs[j])
    for k in range(len(lst)):
        print(lst[k])
""" Exerice 5 """
def nettoyage(liste1 ,val):
    liste2=[]
    for i in range(len(liste1)):
        if(liste1[i] != val):
            liste2.append(liste1[i])
    return liste2

def carreListe(liste1):
    for i in range(len(liste1)):
        if liste1[i] < 0:
            liste1[i] ** 2
    return liste1 
