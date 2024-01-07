#Ce code permet à l'utilisateur de calculer la tension du générateur, de l'intensité et des résistances de son choix
print("bonjour,Assistance Wisconsin à l'écoute")
print("je suis une calculatice qui vous permet d'inventer votre propre circuit à l'aide de résistance, de générateur et des intensités de votre choix")
print("que cherchez vous ?")
print("tapez: \n1 pour tension,\n2 pour la résitance et \n3 pour l'intensité\n")
first_choice = int(input("Que désirez vous calculez : "))

if first_choice == 1 :
    print("vous cherchez la tension de quoi?")
    print("tapez \n1 pour le circuit,\n2 pour le genérateur,\n3 pour résistance")
    second_choice = int(input("Que désirez vous calculez : "))
    if second_choice == 1 :
        print("Quel sont vos données")
        nb_résistance = int(input("entrer le nombre de r : "))
        if nb_résistance == 1 :
            résistance_u = float(input("entrer la valeur de l'unique r :"))
            intensité_u = float(input("entrer l'intensité : "))
            tension_g = résistance_u * intensité_u
            print("la tension du générateur est ",tension_g, "volt")
        elif nb_résistance < 1 :
            print("cette dimension n'est pas dans mes cordes")
        else : 
            
           
            print("tapez 1 pour résistances en serie, 2 pour en parallèle")
            third_choice = int(input("choisi : "))
                
            if third_choice == 1:
                resistance= [] 
                for i in range(nb_résistance):
                    resistance.append(float(input("entrez les valeurs des résistances" + str(i +1))))

                intensité_s = float(input("entre l'intensité de ce circuit"))
                tensio_alim = sum(resistance)*intensité_s 
                print("la tension de ce circuit est de ",tensio_alim, "volt")
            else :
               resistances = []
                for i in range(nb_résistance):
                    resistances.append(float(input("entrez les valeurs des résistances" + str(i +1))))
                    nb_courants = int(input("entrer le nombre de courant"))
                    if nb_courants !=
                    courant = []
                    for i in range(nb_courants):
                        courant.append(float(input("entrez les valeurs des résistances" + str(i +1))))
                    print
    elif second_choice==2:


if first_choice==2 or first_choice==3: 
    u=0
    ic=0
    r=0
    print("Combien de résistances avez-vous dans votre circuit")
    answer_acc=int(input())
    if answer_acc==1:
        print("Que cherchez vous précisément")
        print("Tapez 1 pour tension du générateur")
        print("Tapez 2 pour la résistance")
        print("Tapez 3 pour l'intensité du courant")
        answer_one=int(input())
        
        
        if  answer_one ==2:
            print("Donnez moi la valeur de l'intensité du courant, en virgule et en milli-ampères")
            ic=float(input())
            exp=1/(10*10*10)
            print("Donnez moi la valeur de la tension")
            u=float(input())
            r=u/(ic*exp)
            print("Voila sa valeur: ",r," Ohms")
        elif  answer_one ==3:
             print("Donnez moi la valeur de la résistance, en virgule et en ohms")
             r=float(input())
             print("Donnez moi la valeur de la tension, en virgule et en volts")
             u=float(input())
             exp=10*10*10
             ic=(u/r)*exp
             print("Voila sa valeur: ",ic," mAmpères")

    elif answer_acc<1:
        print("'Racontez pas de bêtises !'")
        print("Veuillez relancer le programme")
    else:
        print("Vos résistances sont-elles:")
        print("1  Toutes sont en série entre elles")
        print("2  Toutes sont en parrallèles entre elles")
    
        answer_two=int(input())
        if answer_two==1:
            print("Que cherchez vous précisément")
            print("Tapez 1 pour tension du générateur")
            print("Tapez 2 pour la résistance")
            print("Tapez 3 pour l'intensité du courant")
            choice=int(input())
        
            if choice==2:
                print(" '1' La résistance équivalente ou '2' une en particulié ?")
                req_pas=int(input())
                if req_pas==1:
                    print("Donnez les valeurs de toutes vos résistances une à une, en virgule et en ohms")
                    b=float(0)
                    for i in range(1,answer_acc+1):
                        i=i+1
                        a=float(input())
                        b=b+a
                
                        print("Voila la valeur de la résistance total: ",b,"Ohms")
                elif req_pas==2:
                        print("Donner la valeur du courant du générateur, en virgule et en milliampères")
                        ic=float(input())
                        print("Donner les tensions de vos résistances une à une, en virgules et en volts")
                
                        e=float(0)
                        for i in range(1,answer_acc):
                            i=i+1
                            d=float(input())
                            e=e+d

                            exp=1/(10*10*10)
                            reqtot=e/ic*exp
                            print("Voila la valeur de la résistance: ",reqtot," Ohms")
            
            elif choice==3: 
                print("Voulez vous me donner 1: la tension du générateur ou 2: de toutes les résistances")   
                sub=int(input())  
                if sub==1:
                    print("Quel est sa valeur, en virgule et en volts")
                    gen=float(input())
                    h=gen
                elif sub==2:
                    print("Donner leurs valeurs une à une, en virgule et en volts")   
                    neg=0
                    for i in range(1,answer_acc+1):
                        i=i+1
                        gen=float(input())
                        neg=neg+gen
                    h=neg  
              
                print("Connaissez vous la valeur de la résistance totale :oui")
                print(",ou en manque-t-il ?: non")
                stick=input()
                if stick=="oui":
                    print("Donner moi sa valeur, en virgule et en ohms")
                    dina=float(input())
                    reponse=h/dina
                    exp=1/(10*10*10)
                    print("Voila la valeur de votre courant: ",reponse/exp," mA")
                elif stick=="non":
                    print("Donner les données que vous connaissez d'une de vos résistances")
                    print('Sa tension, en virgule et en volts')
                    dina=float(input())
                    print("Et sa résistance, en virgule et en ohms")
                    anid=float(input())
                    reponse=dina/anid
                    exp=1/(10*10*10)
                    print("Voila la valeur de votre courant: ",reponse/exp," mA")
        elif answer_two==2:
            print("Que cherchez vous précisément")
            print("Tapez 1 pour tension du générateur")
            print("Tapez 2 pour la résistance")
            print("Tapez 3 pour l'intensité du courant")
            poilu=int(input())
            if poilu==2:
                print("Connaissez vous la valeur de la tension :oui")
                print(",ou en manque-t-il ?: non")
                watermelon=input()
                if watermelon=="oui":
                    print("Donner moi sa valeur, en virgule et en volts")
                    fine=float(input())  
                elif watermelon=="non":
                    print("Donner moi la valeur d'une résistance et celle de son courant")
                    print("D'abord son courant, en virgule et en milliampères")
                    bad=float(input())
                    exp=1/(10**3)
                    print("Maintenant sa résistance, en virgule et en ohms")
                    enif=float(input())
                    fine=enif*bad*exp
                print("Connaissez vous la valeur du courant du générateur: 1,ou de chacun des courants du circuit: 2")
                dakota=int(input())
                if dakota==1:
                    print("Donnez moi sa valeur, en virgule et en milliampères")
                    hub=float(input())
                

                elif dakota==2:
                    print("Donnez moi les valeurs de tout les courants traversant les résistances un à un, en virgule et en millampères")
                    print("(sauf celui du générateur)")
                    quota=2+answer_acc
                    combo=0
                    for i in range (1,quota):
                        gombo=float(input())
                        combo=gombo+combo
                    hub=combo
            
                exp=1/(10**3)
                jungle=fine/(hub*exp)
                print("Voila la valeur de votre résistance équivalente: ",jungle," Ohms")

            elif poilu==3:
                print("Donner moi la tension du générateur, en virgule et en volts")
                pantin=float(input())
                print("Connaissez vous 1 la résistance équivalente ou 2 voulez la calculer d'abord?")
                quintal=int(input())
        
                if quintal==1:
                    print("Donner la valeur en virgule et en ohms")
                    pinky=float(input())
                elif quintal==2:
                    print("Donner moi leurs valeurs de toutes vos résistances une à une, en virgules et en ohms")
                    i=0
                    banana=[]
                    for i in range(i,answer_acc):
                        banana.append(((float(input("Entrez la valeur de la résistance"+str(i+1)+": "))))) 
                    j=1
                    trak=banana[0]
                    for j in range(j,answer_acc):
                        kart=banana[j]
                        trak=((1/kart+(1/trak))**-1)
                    pinky=trak
                exp=1/(10**3)
                woosup=(pantin/pinky)/exp
                print("Voila la valeur du courant: ",woosup," en mA")
    
        
    
        

