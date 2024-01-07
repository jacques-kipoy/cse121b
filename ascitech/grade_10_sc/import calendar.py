puberte = str(input("Etes-vous pubert ? Yes or No ? "))
while puberte != "No":
    cycle = str(input("Comment est votre cycle? Regulier or Irregulier "))
    if cycle == "Regulier":
        duree = int(input("De combien de jours est votre cycle ? "))
        if duree <= 26 :
            print("Votre cycle est très court")
        elif duree == 26 or duree == 27 :
            print("Votre cycle est court")
        elif duree == 28 or duree == 29:
            print("Votre cycle est moyen")
        elif duree == 30 or duree == 31:
            print("Votre cycle est long")
        elif duree > 31:
            print("Votre cycle est très long")
    if cycle == "Irregulier":
        print("Un cycle irrégulier n'est très facile à comprendre mais nous pouvons vous aidez à avoir plus d'information pour votre sécurité")
        aide = str(input("Approuvez-vous notre aide ? Yes or No "))
        while aide != "No":
            import webbrowser
            webbrowser.open_new("https://youtu.be/zza4Z9zDiBE")
            webbrowser.open_new ("https://youtu.be/-smBxWMle7g")
        else:
            print("Merci d'avoir utilisé le programme. Au plaisir de vous revoir")
    break
