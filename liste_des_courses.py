import json
import os

fichier = "liste_des_courses.json"

# -------- CHARGEMENT DU FICHIER --------
if os.path.exists(fichier):
    with open(fichier, "r", encoding="utf-8") as file:
        try:
            liste_de_course = json.load(file)
        except json.JSONDecodeError:
            liste_de_course = []
else:
    liste_de_course = []

# -------- MENU --------
while True:
    print("\n" + "-" * 30)
    choix = input("""choisissez parmi ces 5 options:
1: ajouter un element a la liste
2: retirer un element de la liste
3: afficher les elements de la liste
4: vider la liste
5: quitter
? votre choix: """)

    if not choix.isdigit():
        print("veuillez entrer un nombre valide !")
        continue

    number_input = int(choix)

    # -------- OPTION 1 --------
    if number_input == 1:
        element = input("donner le nom de l'element a ajouter : ").strip()
        if element:
            liste_de_course.append(element)
            with open(fichier, "w", encoding="utf-8") as file:
                json.dump(liste_de_course, file, indent=4, ensure_ascii=False)
            print(f"l'element {element} a ete ajoute")
        else:
            print("entree invalide")

    # -------- OPTION 2 --------
    elif number_input == 2:
        isaac = input("donner le nom de l'element a retirer : ").strip()
        if isaac in liste_de_course:
            liste_de_course.remove(isaac)
            with open(fichier, "w", encoding="utf-8") as file:
                json.dump(liste_de_course, file, indent=4, ensure_ascii=False)
            print(f"l'element {isaac} a ete retire")
        else:
            print(f"l'element {isaac} n'est pas dans la liste de course")

    # -------- OPTION 3 --------
    elif number_input == 3:
        if len(liste_de_course) == 0:
            print("la liste de course est vide")
        else:
            for i in liste_de_course:
                print(i)

    # -------- OPTION 4 --------
    elif number_input == 4:
        if len(liste_de_course) == 0:
            print("la liste est vide")
        else:
            liste_de_course.clear()
            with open(fichier, "w", encoding="utf-8") as file:
                json.dump(liste_de_course, file, indent=4, ensure_ascii=False)
            print("la liste a ete videe !")

    # -------- OPTION 5 --------
    elif number_input == 5:
        break

    else:
        print("veuillez entrer un nombre entre 1 et 5")

print("merci d'avoir utilise la liste de course !")
print("-" * 50)



























