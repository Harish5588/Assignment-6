#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def bark(self):
        print("Woof! I'm a Jack Russell Terrier.")
    
    def jump(self):
        print("I can jump high!")


class Bulldog(Dog):
    def growl(self):
        print("Grrr! I'm a Bulldog.")
    
    def sit(self):
        print("I can sit like a good dog.")


# Creating objects and implementing functionalities
dog1 = Dog("Max", 5, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Buddy", 3, "White and Brown")
dog2.description()
dog2.get_info()
dog2.bark()
dog2.jump()
print()

dog3 = Bulldog("Rocky", 4, "Brindle")
dog3.description()
dog3.get_info()
dog3.growl()
dog3.sit()


# In[ ]:




