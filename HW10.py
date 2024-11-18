"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

#########################################

class Pet:
    name = ""
    species = ""
    weight = 0
    fee = 0
    age = 0
    happiness = 0
    adopted = False
    isVaccinated = False
    owner = ""
    def __init__(self, iname, ispecies, iweight, ifee, iage, ihappiness, iadopted, ivaccinated, iowner):
        self.name = iname
        self.species = ispecies
        self.weight = iweight
        self.fee = ifee
        self.age = iage
        self.happiness = ihappiness
        self.adopted = iadopted
        self.isVaccinated = ivaccinated
        self.owner = iowner
        pass

    def is_adoptable(self):
        if self.adopted or self.happiness >= 10:
            return False
        return True
        pass

    def update_happiness(self, boost):
        self.happiness += boost
        if self.happiness > 100:
            self.happiness = 100
        pass

    def feed(self, food):
        if self.happiness == 100:
            return f"{self.name} is full."
        if food != self.species:
            self.happiness -= 20
            if self.happiness <= 20:
                print(f"{self.name} needs to go to the vet.")
            return f"{self.species}s don't eat {food} food!"
        self.happiness += 20
        self.weight += 2
        return f"{self.name} is well fed."
        pass

    def checkup(self):
        if self.happiness >= 100:
            return f"{self.name}: Happiness - {self.happiness}"
        self.happiness = 100
        self.isVaccinated = True
        pass

    def up_for_adoption():
        pass
        
    def __gt__(self, pet):
        if self.age > pet.age and self.weight > pet.weight:
            return True
        return False
        pass

    def __str__(self):
        temp = "Available"
        if self.adopted:
            temp = "Adopted"
        return f"{self.name} ({self.species}, {self.age} yrs, {self.happiness} happiness) - {temp}, Fee: ${self.fee}"
        pass

#########################################

class Owner:
    name = ""
    budget = 0.0
    pets = []
    def __init__(self, iname, ibudget = 150, ipets = []):
        self.name = iname
        self.budget = ibudget
        self.pets = ipets
        pass

    def can_afford(self, pet):
        if self.budget > pet.fee:
            return True
        return False
        pass

    def adopt_pet(self, pet):
        if self.can_afford(pet):
            pet.adopted = True
            self.budget -= pet.fee
            self.pets.append(pet)
            pet.name = self.name
            return f"{pet.name} has been adopted!"
        pass
    
    def __lt__(self, other):
        if self.budget < other.budget and len(self.pets) < len(other.pets):
            return True
        return False
        

    def __str__(self):
        return f"{self.name} has {len(self.pets)} pets and a budget of ${self.budget}."

#########################################


class AdoptionCenter:

    def __init__():
        pass

    def add_pet():
        pass

    def remove_pet():
        pass
    
    def log_adoption():
        pass
    
    def find_pet_by_species():
        pass

    def adopted_pets_dict():
        pass

    def happiness_of_adopted_pets():
        pass

    def __eq__():
        pass

    def __str__():
        pass

                
