#Project name: Cylindre de Jefferson
#MAHDI Mohamed El Amine
#yanis cavey


import  random

class JeffersonShell():

    #constructeur
    def __init__(self):

        self.file    = "Cylinder.txt"
        # execution
        self.FILEL = self.verifyInteger("Entrer N = La taille du mot :  ")
        mot = input( "Entrer le mot : " )
        self.createCylinder()

        self.cylinder = self.loadCylinder()
        self.key = self.createKey()
        textCipher = self.cipherText( mot)
        print(' Cipher ',textCipher)
        textuncipher  = self.uncipherText( textCipher)
        print(' uncipherText ',textuncipher)
     
    #    Retire de la chaine de caractère "text" tout ce qui est non alpha et return: Chaine dlae caractère convertie.
    def convertLetter(self,text):
        tmp_str = ""

        for letter in text:
            if letter.isalpha() and ord(letter) <= 123:           
                tmp_str += letter
        return (tmp_str.upper())

    #Génère une liste de lettre majuscule de A à Z en choisisant la lettre a seléctionné d'une façon aléatoire à partir un tableau de lettre d'alphabet majuscule .

    def mix(self):
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        chain = ''
        for i in range(len(letters)):
            s = random.randint(0,len(letters)-1)
            chain += letters[s]
            letters.remove(letters[s])
        return chain

    # Créé un fichier texte nommé en fonction de la variable "file" avec "n" nombre de lignes avec la chaine de caractère générée
    def createCylinder(self):
        file_ = open(self.file, "w")

        for i in range(0, self.FILEL):
            myText = self.mix() 
            file_.write(myText+ "\n") 
        file_.close()

    # Calculer nombre de caractere dans une ligne
    def ft_getnewlinesnb(self,str_):
        count = 0

        for i in range(0, len(str_)):
            if (str_[i] == '\n'):
                count += 1
        return (count)

    #Charge un fichier texte nommé et le stocké sous forme de dictionnaire  

    def loadCylinder(self):
        content = open(self.file, "r").read()
        lines_dict = {}
        i = 0
        buf = ""

        for i in range(0, self.ft_getnewlinesnb(content)):
            for j in range(0, 26):
                buf += content[(i * 27) + j]
            lines_dict[i + 1] = buf
            buf = ""

        return (lines_dict)
    #Vérifie la validité d'une clé pour le cryptage ou dé-cryptage du message.
    def keyOk(key, n):
        for i in range(1,n+1):
            if i not in key:
                return False
        return True
    #Génère une clé sous forme d'une liste d'entiers positifs généré aléatoirement  et compris entre 1 et n.
    def createKey(self):
        lst = []
        key = []
        n=self.FILEL
        for num in range(1,n+1):
            lst += [num]
        for i in range(n):
            k = random.randint(0,len(lst)-1)
            key += [lst[k]]
            lst.remove(lst[k])
        print(key)
        return key
    #Renvoi la position d'une lettre dans l'alphabet rentré.
    def find(self,letter, alphabet):
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                return i
    # i est un entier compris entre 0 et 25.
    # La fonction retournera i + 6 modulo de 26.
    def shift(self,i):
        i += 6
        i %= 26
        return i
    # i est un entier compris entre 0 et 25.
    # La fonction retournera i - 6 modulo de 26.
    def unshift(self,i):
        i -= 6
        i %= 26
        return i

    # Chiffre la letre en décalant la lettre choisie de 6 crans.
    def cipherLetter(self,letter, alphabet):
        i = self.find(letter,alphabet)
        i = self.shift(i)
        return i

    #Crypte le texte avec un dictionnaire d'alphabet et la liste avec l'ordre dans lequel mettre les cylindres.
    def cipherText(self,text):
        k = 0
        c = ''
        if len(self.cylinder) != len(self.key):
            return('The key is invalid')
        text = self.convertLetter(text)
        for t in text:
            n = self.cipherLetter(t,self.cylinder.get(self.key[k]))
            c += self.cylinder.get(self.key[k])[n]
            k += 1
        return c

    # déChiffre la letre en reculant la lettre choisie de 6 crans.
    def uncipherLetter(self,letter, alphabet):
        i = self.find(letter, alphabet)
        i = self.unshift(i)
        return i

    #Decrypte le texte avec un dictionnaire d'alphabet et la liste avec l'ordre dans lequel mettre les cylindres.

    def uncipherText(self, text):
        k = 0
        c = ''
        if len(self.cylinder) != len(self.key):
            return ('The key is invalid')
        text = self.convertLetter(text)
        for t in text:
            n = self.uncipherLetter(t, self.cylinder.get(self.key[k]))
            c += self.cylinder.get(self.key[k])[n]
            k += 1
        return c

    # vérifie si le carctère entrer au clavier est bien un entier
    def verifyInteger(self,monText):
        nombreDeLigneEntier = False 
        while nombreDeLigneEntier == False:
            try:
                n = int(input( monText ))
            except ValueError:
                print("\n Erreur, vous avez entrer une chaine de carctère ! Merci de choisir un entier\n")
                continue
            else:
                nombreDeLigneEntier = True
                break
        return n
JeffersonShell()
