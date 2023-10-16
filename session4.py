class feline():

    numarm = 4.3
    numleg = 8.9
    numeye = 2
    


    def cat(self):
         print(f"My cats arm length is {self.numarm} inches")    #Float
         print(f"My cats leg length is {self.numleg} inches")    #Float
         print("My cat has", self.numeye, "eyes") #Int
         print("Does it have a tail?", bool('has a tail')) #Bool
         print("Is it furry?", bool(1)) #Bool

animal = feline()
print(animal)
animal.cat()
    
