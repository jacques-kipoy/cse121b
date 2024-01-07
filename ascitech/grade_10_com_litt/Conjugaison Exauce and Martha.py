#ON VAS CONJUGUER LES VERBES LATIN AU TEMPS PRESENT DE L'INDICATIF

verbe=str(input('entrez un verbe '))
print("verbe")
verbe1= verbe +''
n=(len(verbe1))
print(n)

terminaison = verbe [n-3: n+0]
print(terminaison)
radical=verbe [0 : n-3]
print(radical)

if terminaison == 'are':
    print('Verbe regulier première conjugaison')

if terminaison == 'are':
    print(radical+'o')
    print(radical+'as')
    print(radical+'at')
    print(radical+'atis')
    print(radical+'amus')
    print(radical+'ant')

if terminaison == 'ere':
    print('Verbe regulier deuxième conjugaison')

if terminaison == 'ere':
    print(radical+'eo')
    print(radical+'es')
    print(radical+'et')
    print(radical+'etis')
    print(radical+'emus')
    print(radical+'ent')

if terminaison == 'ère':
    print('Verbe regulier troisième conjugaison')

if terminaison == 'ère':
    print(radical+'o')
    print(radical+'is')
    print(radical+'it')
    print(radical+'imis')
    print(radical+'itis')
    print(radical+'int')

if terminaison == 'ire':
    print('Verbe regulier quatrième conjugaison')

if terminaison == 'ire':
    print(radical+'io')
    print(radical+'is')
    print(radical+'it')
    print(radical+'imus')
    print(radical+'itis')
    print(radical+'iunt')

if terminaison == 'ére':
    print('Verbe regulier quatrième conjugaison bis')

if terminaison == 'ére':
    print(radical+'io')
    print(radical+'is')
    print(radical+'it')
    print(radical+'imus')
    print(radical+'itis')
    print(radical+'iunt')

 

    






    







    
    


