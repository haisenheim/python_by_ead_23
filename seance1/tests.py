print("Programme du maximum de deux nombres \n")

a = int(input("Veuillez saisir le premier nombre : \n"))
b = int(input("Veuillez saisir le deuxieme nombre : \n"))

if(a>b):
    c = a
   # print ("Je suis dans le if \n")
else:
    c = b
    #print("Je suis dans le sinon")
print("J'ai fini \n")

print("Le plus grand entre {} et {} est {}".format(a,b,c))
    