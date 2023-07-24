#Project name: Cylindre de Jefferson
#MAHDI Mohamed El Amine
#yanis cavey
import  sys
from tkinter import *
#from JeffersonShell import *
import math

class Jefferson(Frame):

    #constructeur
    def __init__(self):
        self.FILEPATH    = "Cylinder.txt"        
        self.cylinder = self.loadCylinder()
        self.LEN =  len(self.cylinder)  
        self.cylinderToBoard()
        self.key = self.initkey()
        self.newBoard = self.initBoard(self.LEN,self.LENTXT)
        app = Tk()
        self.app=app  
        self.app.title("Jefferson's cylinders")  
        self.CAN = Canvas(self.app, width = 650, height =600, bg ='black')           
        self.CAN.bind("<Button-1>", self.selectAction)  
        self.CAN.pack(side =TOP, padx =3, pady =3)  
        self.displayBoard(self.board,'RED')
        b2 = Button(self.app, text ='Close', command = quit)
        b2.pack(side =BOTTOM, padx =3, pady =3)
        self.app.mainloop()

    #lire le fichier txt     
    def loadCylinder(self):
        content = open(self.FILEPATH, "r").read()
        lines_dict = {}
        i = 0
        buf = ""

        for i in range(0, self.ft_getnewlinesnb(content)):
            for j in range(0, 26):
                buf += content[(i * 27) + j]
            lines_dict[i + 1] = buf
            buf = ""

        return (lines_dict)

    # lire une ligne
    def ft_getnewlinesnb(self,str_):
        count = 0

        for i in range(0, len(str_)):
            if (str_[i] == '\n'):
                count += 1
        return (count)

    #initialiser un tableau de ligne et  colonne avec des 0
    def initBoard(self,n,m):
        board = []
        for i in range(m):
            ligne = []
            for j in range(n):
                ligne += [0]
            board += [ligne]
        return board

    # initialiser un t  ble u key
    def initkey(self):
        key = []
        for i in range(self.LEN):
            key += [-1]
        return key
    # convertir le txt en tableau 
    def cylinderToBoard(self):
        n = len(self.cylinder) 
        m = len(self.cylinder.get(1))  
        self.LENTXT = m
        board = self.initBoard(n,m)
        for i in range( n):  #10
            for j in range(m): #26            
                board[j][i] = self.cylinder.get(i+1)[j] 

        self.board = board
        #return board,m 
   
    # le nouveau cylindre   prés key en t   ble u
    def newCylinderToBoard(self):
        n = self.LEN #self.LEN(cylinder) 
        m = self.LENTXT#26#self.LEN(cylinder.get(1))     
       
        for i in range( n):  #10
            for j in range(m): #26
            #print('i : ',i)
            #print('j : ',j)
            # print('cyl : ',cylinder.get(i+1))
                lettre = self.newCylinder.get(i+1)[j] 
                #print('lettre : ',lettre)
                self.newBoard[j][i]=lettre
            #print('newBoard : ',newBoard)
        
    #afficher le tableau cylindre
    def displayBoard(self,board,COLOR):
        # changement de plan, calcul des x et Y, les paramètre du canvas 500X500 alors que le Tableau reel Ligne X Colonne 
        x = 400/self.LENTXT
        y = 500/self.LEN

        for i in range( self.LENTXT):  #26
            for j in range(self.LEN): #10
                x1 = ((j*y)+y/2) 
                y1 = ((i*x)+x/2) 
                #can.create_rectangle( j*y,i*x, (j*y)+y,(i*x)+x , fill='black',outline = 'red')
            
                self.CAN.create_text((x1,y1),text=board[i][j], fill=COLOR )

        for nb in range(self.LEN):  
            x1 = ((nb*y)+y/2)   
            y1 = ((self.LEN*x)+x/2) +20      
            self.CAN.create_text((x1,450),text=nb+1, fill='red')
        
        x1 = ((nb*y)+3*y)   +20  
        self.CAN.create_text((x1,450),text='ENTER KEY', fill='red')

    # afficher le ableau key
    def displayKey(self,nb,y):
        POS = self.misKey(nb)    
        if(POS != -1):
            x1 = ((POS*y)+y/2)     
            xOld = ((nb*y)+y/2)  
            self.CAN.create_text((xOld,450),text=nb+1, fill='green')
            self.CAN.create_text((x1,470),text=nb+1, fill='red')
        
    # mis à jour du tableau key aprés sélction
    def misKey(self,nb):
        for i in range(self.LEN):
            if(self.key[i]==nb+1):
                return -1
            if(self.key[i]==-1):
                self.key[i] = nb+1
                return i
        return -2

    # verifier si la selction de la clé est fini
    def definekey(self):
        for i in range(self.LEN):
            if(self.key[i]==-1):
                return 0
        return 1
    
    #declaration d'un nouveau tableau pour les fleche
    def defineNewBoard(self):
        for i in range(self.LENTXT):
            for j in range(self.LEN):
                if(self.newBoard[i][j]==0):
                    return 0    
        return 1
    
    #afficher le nouveau tableau cylindre
    def displayNewCylinder(self,COLOR):
        # changement de plan, calcul des x et Y, les paramètre du canvas 500X500 alors que le Tableau reel Ligne X Colonne 
        x = 400/self.LENTXT
        y = 500/self.LEN

        for i in range( self.LENTXT):  #26
            for j in range(self.LEN): #10
                x1 = ((j*y)+y/2) 
                y1 = ((i*x)+x/2) 
                
                self.CAN.create_text((x1,y1),text=self.newBoard[i][j], fill=COLOR )

    #calcule du nouveau cylindre
    def NewCylinders(self):
        newCylinder = {}
        #print('cylinder,',cylinder)
        #print('key,',key)
        for i in range(1,len(self.cylinder)+1):
            pos = self.key[i-1]
            newCylinder[i] = self.cylinder.get(pos)
        
        return newCylinder  
    
    #afficher les ligne clear et cipher
    def displayLine(self,pos,myText):
        x = 400/self.LENTXT
        y = 500/self.LEN
        
        y1 = ((pos*x)+x/4) -3
        x1 = ((self.LEN*y)+y/4) -10 
        y2 =  (((pos+1)*x)+x/4) -3
        y3 = y1+ (y2-y1)/2
        self.CAN.create_line(10,y1, x1,y1 , fill="red", width=1)
        self.CAN.create_line(10,y2, x1,y2 , fill="red", width=1)  
        self.CAN.create_text((x1+50,y3),text=myText, fill='red' )

    #afficher les fleches
    def displayflesh(self):
        y = 500/self.LEN
        for j in range(self.LEN): #10
            x1 = ((j*y)+y/2)          
            self.CAN.create_text((x1,480),text='↑', fill='red')
            self.CAN.create_text((x1,500),text='↓', fill='red')
        
        
    # cipher
    def newCylinderBoard(self,pos,sens):
        m =self.LENTXT
        if(sens == 'bas'):
            
            for i in range(m): #26
                posX= i+1
                if(posX == m):
                    posX = 0
                #print('new pos ',posX);    
                lettre = self.newBoard[posX][pos] 
                self.newBoard[posX][pos]   = self.newBoard[0][pos] 
                self.newBoard[0][pos]  = lettre
    
        else:
            if(sens == 'haut'):
                
                for i in range(m-1,0,-1): #26
                    posX= i-1
                    if(posX == -1):
                        posX = m-1                    
                    lettre = self.newBoard[posX][pos] 
                    self.newBoard[posX][pos]   = self.newBoard[m-1][pos] 
                    self.newBoard[m-1][pos]  = lettre
        
    #affichage
    def display(self):
        
            self.CAN.delete(ALL)
            self.displayNewCylinder('red')
            self. displayflesh()
            self.displayLine(6,'CLEAR')
            self.displayLine(12,'CIPHER')
            self.CAN.create_text((520,520),text='FINISH', fill='red')
            

    # selection d'une case sur le jeu, event click
    def selectAction(self,event):       
        # on détermine la case ou s'est passé la selection 
        
        x = 500/self.LEN 
        nb = math.floor(event.x/x)
        posY = math.floor(event.y)
    # #print('posY : ' , posY)
    # print('nb : ' , nb)
        if(posY < 500 and nb < self.LEN):
            self.displayKey(nb,x)  
        
        if(self.definekey() == 1):
            if( nb>self.LEN and posY >= 520 and posY < 540 ):
                print('close')
                self.app.quit
            if(self.defineNewBoard() == 0):
                #print ('no definenewBoard')
                self.newCylinder  = self.NewCylinders()
                #print('newCylinder:', newCylinder)
                self.newCylinderToBoard()
                self.display()
            else: 
                posFlech =    math.floor(event.x/x)
                
                if(posY >= 480 and posY < 500):
                    #print('flesh haut : ' , posFlech)
                    self.newCylinderBoard (posFlech,'haut')                    
                    self.display()
                else:
                    if(posY >= 500 and posY < 520):
                        #print('flesh bas : ' , posFlech)
                        self.newCylinderBoard (posFlech,'bas')                        
                        self.display()
            


Jefferson()    