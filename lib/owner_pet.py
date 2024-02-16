class Pet:
    
    all = []
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=""):
        
        PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
        if pet_type not in PET_TYPES:
            raise Exception ("Invalid pet name")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner 
        Pet.all.append(self)
    
class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        pet_list = []
        for pet in Pet.all:
            if pet.owner == self:
                pet_list.append(pet)
                
        return pet_list
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Not a valid pet type")
        

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet:pet.name)
        return sorted_pets
                
        