print("## Section des functions #### \n-------------------------------- \n")

def carre(i):
    return i**2

def puissance(a,b):
    return a**b

''' x = input("Veuillez saisir un monbre \n")
x= int(x)
print("Le carre de {} est {}".format(x,carre(x))) '''

x = input("Veuillez saisir la base \n")
x= int(x)

y = input('Veuillez saisir l\'exposant \n')
y= int(y)

b = puissance(x,y) 
print("{} a la puissance {} est egale a : {}".format(x,y,b))




    