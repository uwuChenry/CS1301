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
        pass

    def is_adoptable(self):
        if self.adopted or self.happiness <= 10:
            return False
        return True
        pass

    def update_happiness(self, boost):
        self.happiness += boost
        if self.happiness > 100:
            self.happiness = 100
        pass

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
        pass

    def checkup(self):
        if self.happiness >= 100:
            return f"{self.name}: Happiness - {self.happiness}"
        self.happiness = 100
        self.isVaccinated = True
        pass

    def up_for_adoption(self, owner, afee):
        if self.adopted:
            self.adopted = False
            self.checkup()
            self.owner = None
            self.fee = afee
            owner.pets.remove(self)
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
    def __init__(self, iname, ipets = [], iowners = [], irevenue = 0):
        self.name = iname
        self.pets = ipets
        self.owners = iowners
        self.revenue = irevenue
        pass

    def add_pet(self, pet):
        self.pets.append(pet)
        return f"{pet.name} has been added to the adoption center."
        pass

    def remove_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)
        
        pass
    
    def log_adoption(self, pet, owner):
        if not pet.adopted and owner.budget >= pet.fee:
            self.owners.append(owner)
            self.revenue += pet.fee
            owner.adopt_pet(pet)
            self.remove_pet(pet)
            return f"{owner.name} has adopted {pet.name}!"
        pass
    
    def find_pet_by_species(self, species):
        temp = []
        for pets in self.pets:
            if pets.species == species:
                temp.append(pets)
        return temp
        pass

    def adopted_pets_dict(self):
        out = {}
        for owner in self.owners:
            out[owner.name] = owner.pets
        return out
        pass

    def happiness_of_adopted_pets(self):
        s = 0
        for owner in self.owners:
            for pets in owner:
                s += pets.happiness
        return s
        pass

    def __eq__(self, other):
        if self.name == other.name and self.revenue == other.revenue:
            return True
        return False
        pass

    def __str__(self):
        return f"{self.name} has {len(self.pets)} pets available for adoption."
        pass
