import os

def add_mail(sender, subject, date):
    if not os.path.exists("archive.txt"):
        with open("archive.txt", "w") as f:
            f.write("Sender,Subject,Date\n")
    with open("archive.txt", "a") as f:
        f.write(f"{sender},{subject},{date}\n")

def search_mail(sender=None, subject=None, date=None):
    mails = []
    with open("archive.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            mail = line.strip().split(",")
            if (sender is None or mail[0] == sender) and (subject is None or mail[1] == subject) and (date is None or mail[2] == date):
                mails.append(mail)
    return mails

def list_mails():
    mails = []
    with open("archive.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            mails.append(line.strip().split(","))
    return mails

def close_program():
    print("Closing program...")
    exit()


if __name__ == "__main__":
    while True:
        print("\n")
        print("---------------------")
        print("Archiveur de courrier")
        print("1. Ajouter une courrier")
        print("2. Rechercher un courrier")
        print("3. Lister les courrier")
        print("4. Fermer le logiciel")
        option = input("Entrer un chiffre d'action: ")
        if option == "1":
            os.system('cls')
            print("Ajout de courrier")
            sender = input("Expediteur: ")
            subject = input("Objet: ")
            date = input("Date au format (jj/mm/yyyy): ")
            add_mail(sender, subject, date)
            print("Courrier ajouter avec succes!")
        elif option == "2":
            os.system('cls')
            print("Recherche de courrier")
            sender = input("Expediteur (optionnel): ") or None
            subject = input("Objet (optionnel): ") or None
            date = input("Date (optionnel): ") or None
            mails = search_mail(sender, subject, date)
            if mails:
                print("Courrier trouve:")
                for mail in mails:
                    print(mail)
            else:
                print("Aucun courrier trouve")
        elif option == "3":
            os.system('cls')
            mails = list_mails()
            if mails:
                print("Liste de courrier:")
                for mail in mails:
                    print(mail)
            else:
                print("Aucun courrier trouve.")
        elif option == "4":
            close_program()
        else:
            print("Option invalide.")
