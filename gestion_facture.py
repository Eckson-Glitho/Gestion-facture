from pickle import*
eleve=[]
try:
    p=open("saves","rb")
    eleve=load(p)
    p.close()
except:
    inf=[]
    NomE=input("Quel est le nom de votre université?")
    nf=int(input("Combien de fillière compte votre université?"))
    for i in range (1, (nf+1)):
        print("Quelle est le nom de la fillière",i)
        ndf=input()
        print("Combien de classe compte la fillière",i)
        nc=int(input())
        jul=[ndf, nc]
        for j in range (1, (nc+1)):
            print("Quelle est la scolarité pour la classe",j)
            s=int(input())
            jul.append(s)
        inf.append(jul)
    print(inf)

    p=open("saves", "wb")
    dump(eleve,p)
    dump(NomE,p)
    p.close()
    

nc=105000
    


def ajouter_etudiant():
    nom=input("Entrer le nom de l'étudiant:")
    prenom=input("Entrer le prénom de l'étudiant:")
    ID=nc+len(eleve)+1
    classe=input("Entrer la fillière de l'étudiant:")
    niveau=int(input("entrer la classe de l'étudiant:"))
    
    ld=[nom, prenom, ID, classe, niveau]
    eleve.append(ld)
    print(eleve)

    p=open("saves", "wb")
    dump(eleve,p)
    p.close()





def factures():
    idd=int(input("Entrer l'identifiant de l'étudiant  :"))
    sv=int(input("Entrée la somme versée par l'étudiant:"))
    rap=105000-sv
    idf=0
    for i in range (0, len(eleve)):
        if idd in eleve[i]:
            idf=(len(eleve[i])-5)+1
            f=[idf, sv, rap]
            c=i
            eleve[i].append(f)
    print("Quittance N° : 000{}".format(idf)) 
    z=["Nom         : ", "Prénom      : ", "Identifiant : ", "Classe      : ", "Niveau      : "]
    for k in range (0, len(z)):
        print(z[k], end=""); print(eleve[c][k])
    print("Frais à payer: 106000")
    print("Frais payés  : ",sv)
    print("Impayé       : ",rap)
    
            

    p=open("saves", "wb")
    dump(eleve,p)
    p.close()




def toutes_factures():
    idd=int(input("Entrer l'identifiant de l'étudiant  :"))
    for i in range (0, len(eleve)):
        if idd in eleve[i]:
            print



    

def supprimer_etudiant():
    idd=int(input("Entrer l'identifiant de l'étudiant: "))
    for i in range (0, len(eleve)):
        if idd in eleve[i]:
            del eleve[i]
    print("Etudiant supprimé")

    p=open("saves", "wb")
    dump(eleve,p)
    p.close()

    
    
    
print("*-----Gestion des factures de {}-----*".format(NomE))
print("")
print("Taper 1 pour ajouter un étudiant\n\
taper 2 pour procéder a un paiement\n\
Taper 3 pour afficher toutes le factures d'un étudiant\n\
Taper 4 pour rechercher une facture\n\
Taper 5 pour afficher les factures impayées d'un etudiant\n\
taper 6 pour afficher le solde de toutes les factures payées et impayées d'un étudiant\n\
taper 7 pour supprimer un étudiant\n\
Taper 0 pour arreter le programme")
print("")
stop=1
while stop==1:
    choix=int(input("Que désirez vous faire?: "))
    if choix<0 or choix>7:
        print("Choix incorrecte")
        print("")
        print("Taper 1 pour ajouter un étudiant\n\
taper 2 pour procéder a un paiement\n\
Taper 3 pour afficher toutes le factures d'un étudiant\n\
Taper 4 pour rechercher une facture\n\
Taper 5 pour afficher les factures impayées d'un etudiant\n\
taper 6 pour afficher le solde de toutes les factures payées et impayées d'un étudiant\n\
taper 7 pour supprimer un étudiant\n\
Taper 0 pour arreter le programme")
        print("")
        choix=int(input("Que désirez vous faire?: "))
    if choix==1 :
        print(ajouter_etudiant())
    if choix==2:
        print(factures())
    if choix==3:
        print(toutes_factures())
    if choix==4:
        print(chercher_factures())
    if choix==5:
        print(impayées())
    if choix==6:
        print(solde_total())
    if choix==7:
        print(supprimer_etudiant())
    if choix==0:
        stop=0
    























    
    

