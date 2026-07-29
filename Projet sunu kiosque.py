import json
from datetime import datetime
# Déclaration d'une liste vide pour stocker tous les journaux, magazines et revues
kiosque = []

# Cette fonction sert à enregistrer un nouveau journal

def ajouter_titre():
    nom = input("Nom du titre : ")
    prix = float(input("Prix : "))
    while prix <= 0:
        prix = float(input("Le prix doit être positif : "))
    quantite = int(input("Quantité reçue : "))
    while quantite < 0:
        quantite = int(input("La quantité doit être positive : "))

    journal = {
        "nom": nom,
        "prix": prix,
        "stock": quantite,
        "vendus": 0,
        "invendus": 0
    }

    kiosque.append(journal)
    print("Titre ajouté avec succès.")

# Cette fonction sert à montrer les journaux et magazines qui sont encore disponibles dans le kiosque

def afficher_stocks():
    if len(kiosque) == 0:
        print("Aucun titre enregistré.")
    else:
        for j in kiosque:
            print(f"Titre : {j['nom']}")
            print(f"Prix : {j['prix']} FCFA")
            print(f"Stock : {j['stock']}")
            print("-------------------")

# Cette fonction sert à enregistrer le vente d'un journal ou d'un magazine

def enregistrer_vente():
    nom = input("Titre vendu : ")

    for j in kiosque:
        if j["nom"].lower() == nom.lower():
            qte = int(input("Quantité vendue : "))

            if qte <= j["stock"]:
                j["stock"] -= qte
                j["vendus"] += qte
                j["date_derniere_vente"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                montant = qte * j["prix"]

                date_vente = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                print("Date :", date_vente)
                print("Montant :", montant, "FCFA")
            else:
                print("Stock insuffisant.")
            return

    print("Titre introuvable.")

# Cette fonction sert à calculer l'argent total gagné grâce aux ventes de la journée

def calculer_chiffre_affaires():
    total = 0
    for j in kiosque:
        total += j["vendus"] * j["prix"]

    print("Chiffre d'affaires :", total, "FCFA")

# Cette fonction sert à gérer les exemplaires qui n'ont pas été vendus à la fin de la journée

def gerer_invendus():
    nom = input("Titre : ")

    for j in kiosque:
        if j["nom"].lower() == nom.lower():
            j["invendus"] = j["stock"]
            j["stock"] = 0
            print("Invendus enregistrés.")
            return
    print("Titre introuvable.")

# Cette fonction sert à enregistrer les données du kiosque dans un fichier JSON afin de ne pas les perdre lorsque le programme s'arrête

def sauvegarder_json():
    with open("kiosque.json", "w", encoding="utf-8") as f:
        json.dump(kiosque, f, indent=4)

def menu():
    while True:
        print("\n===== SUNU KIOSQUE =====")
        print("1-Ajouter un titre")
        print("2-Enregistrer une vente")
        print("3-Afficher les stocks")
        print("4-Chiffre d'affaires")
        print("5-Gérer les invendus")

        
        print("6-Gérer un abonnement")
        print("7-Afficher les clients")
  
        
        print("8-Sauvegarder")
        print("9-Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_titre()
        elif choix == "2":
            enregistrer_vente()
        elif choix == "3":
            afficher_stocks()
        elif choix == "4":
            calculer_chiffre_affaires()
        elif choix == "5":
            gerer_invendus()

        elif choix == "6":
            gerer_abonnement()
         elif choix == "7":
           afficher_clients()
        
        elif choix == "8":
            sauvegarder_json()
            
        elif choix == "9":
            break
        else:
            print("Choix invalide.")

menu()
