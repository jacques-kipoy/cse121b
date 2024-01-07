candidat_1 = input("entrer le nom du premier candidat")
score_1 = int(input("entrer le premier score"))
candidat_2 = input("entrer le nom du deuxieme")
score_2 = int(input("entrer le deuxieme score"))
candidat_3 = input("entrer le nom du troisieme candidat")
score_3 = int(input("entrer le troisieme score"))
candidat_4 = input("entrer le nom du quatrieme candidat")
score_4 = int(input("entrer le quatrieme score"))
somme = score_1 + score_2 + score_3 + score_4
list[score_1,score_2,score_3,score_4]
if somme <= 100 :
    print("les elections peuvent commencer")
    if score_1 < 12.5 :
        print(candidat_1,"il est elimine")
    if score_2 < 12.5 :
        print(candidat_2,"il est elimine")
    if score_3 < 12.5 :
        print(candidat_3,"il est elimine")
    if score_4 < 12.5 :
        print(candidat_4,"il est elimine")
    if score_1 > 12.5 or score_2 > 12.5 or score_3 > 12.5 or score_4 > 12.5 :
        a = ("il continue")
        if score_1 > 50 and score_1>list[1] or score_1>list[2] or score_1>list[3] :
            print(candidat_1,"il a gagne","avec{}%".format(score_1))
        if score_2 > 50 and score_2>list[0] or score_2>list[2] or score_2>list[3] :
            print(candidat_2,"il a gagne","avec{}%".format(score_2))
        if score_3 > 50 and score_3>list[0] or score_3>list[1] or score_3>list[3] :
            print(candidat_3,"il a gagne","avec{}%".format(score_3))
        if score_4 > 50 and score_4>list[0] or score_4>list[1] or score_4>list[2] :
            print(candidat_4,"il a gagne","avec{}%".format(score_4))
else :
    print("arreter les elections il y a tricherie")