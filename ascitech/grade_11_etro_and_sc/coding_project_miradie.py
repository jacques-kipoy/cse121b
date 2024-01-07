#Créer par 3 éléves de 11SC d'ascitech dans leur cours de coding.  
# c'est logiciel vous permez de calculer imc (indice de masse corporelle) et donner des conseils pour être en bonne corpulance ou santé.

poids=int(input("\nentrer votre poids (en kg )svp:"))
taille=float(input("entrer votre taille (en metres):"))
IMC=poids/(taille*taille)# imc égale poids divise par taille au carré
print("Votre IMC est de",IMC)#afficher le message 
if IMC<16 :#si imc inférieur à 16 
    print ("Vous etes en malnutrition") #afficher le messange etre paranthese 
    print ("ESSAYEZ DE MANGER PLUS ET POUR PLUS D'INFORMATIONS, NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time 
    time.sleep(5) #ceci est un chronomètre de 5 secondes avant que le code se dirige vers un lien
    import webbrowser
    webbrowser .open("https://g.co/kgs/ABFzR8")
    print("voulez vous en savoir plus ? ")
    reponse=str(input())
    reponse=reponse.lower()
    if reponse=="oui" :
       import webbrowser
       webbrowser.open ("https://youtu.be/_hOpiaPw7YI") #ceci est un autre lien au cas où l'utilisateur veut en savoir plus
    elif reponse1=="non" :
        print ("Merci d'avoir consulté notre page.")#afficher le message quand l'utilisateur choisit de s'arrêter là

        
elif 16<=IMC<18.5 :#sinon 16 inférieur ou egale a imc ,imc inferieu a 18 
    print ("Vous etes en maigreur")
    print("ESSAYEZ DE MANGER UN PEU PLUS ET POUR PLUS D'INFORMATIONS, NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://g.co/kgs/FgzVj7")
    print ("Voulez vous en savoir plus?")
    reponse=str(input())
    reponse=reponse.upper()
    if reponse=="OUI" :
       import webbrowser
       webbrowser.open ("https://youtu.be/SL9mj0kpYs4")
    elif reponse=="NON":
        print("Merci d'avoir consulté notre page.")
    
elif 18.5<=IMC<25 :
    print ("Vous etes en corpulance normale")
    print("BRAVO, NE CHANGEZ RIEN DANS VOS HABITUDES ALIMENTAIRES. ET POUR PLUS D'INFORMATIONS NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://www.alptis.org/prevoyance/guide-sante-durable/bonne-sante-les-cles-pour-rester-en-forme-et-en-bonne-sante/#:~:text=%C3%8Atre%20en%20bonne%20sant%C3%A9%20est%20%C2%AB%20un%20%C3%A9tat%20complet%20de%20bien,a%20continu%C3%A9%20%C3%A0%20s'%C3%A9toffer")
    print ("Voulez vous en savoir plus ?")
    reponse=str(input())
    reponse=reponse.lower()
    if reponse=="oui" :
       import webbrowser
       webbrowser.open ("https://youtu.be/57th5WgubGU")
    elif reponse=="non":
        print("Merci d'avoir consulté notre page.")
    
   
elif 25<IMC<=30 :
    print ("Vous etes en surpoids")
    print("ESSAYEZ DE MANGER MOINS ET DE FAIRE UN PEU D'EXERCICE PHYSIQUE. POUR PLUS D'INFORMATIONS NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://g.co/kgs/M1ZT4m")
    print ("Voulez vous en savoir plus ?")
    reponse=str(input())
    reponse=reponse.upper()
    if reponse=="OUI" :
       import webbrowser
       webbrowser.open ("https://youtu.be/HtFDhlUxQ0k")
    elif reponse=="NON":
        print("Merci d'avoir consulté notre page.")
    
    
elif 30<IMC<=35 :#sinon 30 inférieur à imc et imc inférieur ou égale à 35
    print ("Vous etes en obesite moderee") 
    print("FAITES ATTENTION, VOUS METTEZ EN JEU VOTRE SANTE. POUR PLUS D'INFORMATIONS, NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://www.bing.com/search?q=obesite+normale&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=obesite+normale&sc=9-15&sk=&cvid=11793135D1D34D848C7C42BCCBB1A438&ghsh=0&ghacc=0&ghpl= ")
    print ("Voulez vous en savoir plus ?") 
    reponse=str(input())
    reponse=reponse.lower()
    if reponse=="oui" :
       import webbrowser
       webbrowser.open ("https://youtu.be/TtZqgERCE2I")
    elif reponse=="non":
        print("Merci d'avoir consulté notre page.") 
        
    
elif 35<IMC<=40 :
    print(" Vous etes en obesite severe")
    print("FAITES TRÈS ATTENTION, VOUS METTEZ DANGEREUSEMENT VOTRE SANTE EN JEU. POUR PLUS D'INFORMATIONS, NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://www.bing.com/search?q=obesite+severe&form=ANNTH1&refig=8ba5af42e3894de8a8c2044b99aea5c6&sp=2&lq=0&qs=HS&pq=obesite&sk=HS1&sc=10-7&cvid=8ba5af42e3894de8a8c2044b99aea5c6 ")
    print ("Voulez vous en savoir plus ? ")
    reponse=str(input())
    reponse=reponse.upper()
    if reponse=="OUI" :
       import webbrowser
       webbrowser.open ("https://youtu.be/nIvcp0AStdU ")
    elif reponse=="NON":
        print("Merci d'avoir consulté notre page.")

        
elif IMC>40:
    print("Vous etes en obesite morbide")
    print("VOUS ALLEZ MOURIR SI VOUS CONTINUEZ COMME ÇA. POUR D'INFORMATIONS, NOUS VOUS DIRIGEONS VERS LE LIEN SUIVANT")
    import time
    time.sleep(5)
    import webbrowser
    webbrowser.open ("https://sante.journaldesfemmes.fr/fiches-maladies/2620325-obesite-morbide-imc-definition-risques-calcul-operation-que-faire/")
    print ("Voulez vous en savoir plus ?")
    reponse=str(input())
    reponse=reponse.lower()
    if reponse=="oui" :
       import webbrowser
       webbrowser.open ("https://youtu.be/TtZqgERCE2I ")
    elif reponse=="non":
        print("Merci d'avoir consulté notre page.")
