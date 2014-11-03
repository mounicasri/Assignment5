class Animal:
    def __init__(self,name,query1,query2,query3):
        self.name=name
        self.query1=query1
        self.query2=query2
        self.query3=query3
    def guess_who_am_I(self):
        print("I will give you three hints, guess who am I?")
        i=1
               
        while(i<=3):
            if(i==1):
                animal=input(self.query1)
            if(i==2):
                animal=input(self.query2)
            if(i==3):
                animal=input(self.query3)
            if(animal==self.name):
                print("You got it! I'm ",self.name)
                break
            else:
                print("Nope!! try again")
                i=i+1
                
e=Animal("Elephant","I am the largest land-living mammal in the world","I have exceptional memory","I prefer to stay near water")
t=Animal("Tiger","I come in black and white or orange and black","I am the biggest cat","I'm a carnivorous")
b=Animal("Bat","I use echo-location","I can fly","I see well in dark")


b.guess_who_am_I()
t.guess_who_am_I()
e.guess_who_am_I()


##I will give you three hints, guess who am I?
##I use echo-locationEagle
##Nope!! try again
##I can flyBat
##You got it! I'm  Bat
##I will give you three hints, guess who am I?
##I come in black and white or orange and blackLion
##Nope!! try again
##I am the biggest catCat
##Nope!! try again
##I'm a carnivorousTiger
##You got it! I'm  Tiger
##I will give you three hints, guess who am I?
##I am the largest land-living mammal in the worldCow
##Nope!! try again
##I have exceptional memoryElephant
##You got it! I'm  Elephant
