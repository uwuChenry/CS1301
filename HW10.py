"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

#########################################

class Pet:
    def __init__(self, iname, ispecies, iweight, ifee, iage = 1, ihappiness = 50, iadopted = False, ivaccinated = False, iowner = None):
        self.name = iname
        self.species = ispecies
        self.weight = iweight
        self.fee = ifee
        self.age = iage
        self.happiness = ihappiness
        self.adopted = iadopted
        self.isVaccinated = ivaccinated
        self.owner = iowner

    def is_adoptable(self):
        if self.adopted or self.happiness <= 10:
            return False
        return True

    def update_happiness(self, boost):
        self.happiness += boost
        if self.happiness > 100:
            self.happiness = 100

    def feed(self, food):
        if self.happiness >= 100:
            return f"{self.name} is full."
        if food != self.species:
            self.happiness -= 30
            if self.happiness <= 20:
                print(f"{self.name} needs to go to the vet.")
            return f"{self.species}s don't eat {food} food!"
        self.happiness += 20
        self.weight += 2
        return f"{self.name} is well fed."

    def checkup(self):
        if self.happiness >= 100:
            return f"{self.name}: Happiness - {self.happiness}"
        self.happiness = 100
        self.isVaccinated = True

    def up_for_adoption(self, owner, afee):
        if self.adopted:
            self.adopted = False
            self.checkup()
            self.owner = None
            self.fee = afee
            owner.pets.remove(self)
        
    def __gt__(self, pet):
        if self.age > pet.age and self.weight > pet.weight:
            return True
        return False

    def __str__(self):
        temp = "Available"
        if self.adopted:
            temp = "Adopted"
        return f"{self.name} ({self.species}, {self.age} yrs, {self.happiness} happiness) - {temp}, Fee: ${self.fee}"

#########################################

class Owner:
    def __init__(self, iname, ibudget = 150, ipets = None):
        self.name = iname
        self.budget = ibudget
        if ipets == None:
            self.pets = []

    def can_afford(self, pet):
        if self.budget > pet.fee:
            return True
        return False

    def adopt_pet(self, pet):
        if self.can_afford(pet):
            pet.adopted = True
            self.budget -= pet.fee
            self.pets.append(pet)
            pet.owner = self.name
            return f"{pet.name} has been adopted!"
    
    def __lt__(self, other):
        if self.budget < other.budget and len(self.pets) < len(other.pets):
            return True
        return False
        

    def __str__(self):
        return f"{self.name} has {len(self.pets)} pets and a budget of ${self.budget}."

#########################################


class AdoptionCenter:
    def __init__(self, iname, ipets = None, iowners = None, irevenue = 0):
        self.name = iname
        if ipets == None:
            self.pets = []
        if iowners == None:
            self.owners = []
        self.revenue = irevenue

    def add_pet(self, pet):
        self.pets.append(pet)
        return f"{pet.name} has been added to the adoption center."

    def remove_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)
        
    
    def log_adoption(self, pet, owner):
        temp = pet.name
        if not pet.adopted and owner.budget >= pet.fee:
            if owner not in self.owners:
                self.owners.append(owner)
            self.revenue += pet.fee
            owner.adopt_pet(pet)
            self.remove_pet(pet)
            return f"{owner.name} has adopted {temp}!"

    
    def find_pet_by_species(self, species):
        temp = []
        for pets in self.pets:
            if pets.species.lower() == species.lower():
                temp.append(pets)
        return temp


    def adopted_pets_dict(self):
        out = {}
        for owner in self.owners:
            out[owner.name] = owner.pets
        return out


    def happiness_of_adopted_pets(self):
        s = 0
        for owner in self.owners:
            for pets in owner:
                s += pets.happiness
        return s


    def __eq__(self, other):
        if self.name == other.name and self.revenue == other.revenue:
            return True
        return False


    def __str__(self):
        return f"{self.name} has {len(self.pets)} pets available for adoption."





Homeward = AdoptionCenter("Homeward")
Lauri = Owner('Lauri', 400)
Callie = Pet("Callie", "Cat", 8, 350, 10, 10)
Gracie = Pet("Gracie", "Dog", 15, 175, 6, 100)
Tap = Pet("Tap", "Turtle", 1, 55)
Homeward.add_pet(Callie)
Homeward.add_pet(Gracie)
Homeward.add_pet(Tap)
Homeward.remove_pet(Tap)
print(Homeward.log_adoption(Callie, Lauri))
