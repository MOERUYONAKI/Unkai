# Classe

class Succes():
    def __init__(self, id = int):
        self.id = id
        self.succes = [
                {
                    'Premier personnage' : 0, 
                    'Premiers pas' : 0, 
                    'Voyageur' : 0, 
                    'Vagabond' : 0,
                    'Proprietaire' : 0,
                    'Chasseur de monstres (novice)' : 0,
                    'Chasseur de monstres (intermédiaire)' : 0,
                    'Chasseur de monstres (expert)' : 0,
                    'Chasseur de boss (novice)' : 0, 
                    'Chasseur de boss (intermédiaire)' : 0,
                    'Chasseur de boss (expert)' : 0,
                    'Hors la loi' : 0, 
                    'Fantome' : 0,
                    'Acteur du destin' : 0,
                    'Compagnon' : 0,
                    'Ame damne' : 0,
                    'Regicide' : 0,
                    'Chasseur née' : 0,
                    'Createur de désastres' : 0,
                    'Experimentateur' : 0,
                    'Indecis' : 0,
                    'Maitre de guilde' : 0
                },
                {
                    'Maitre des succes' : 0,
                    'Assassin' : 0,
                    'Tueur de demons' : 0,
                    'Touche a tout' : 0,
                    "Lanceur d'hostilites" : 0
                }
            ]
        
    def add_succes(self, name : str):
        if name in self.succes[0].keys():
            if self.succes[0][name] == 0:
                self.succes[0][name] = 1
                
            else:
                return f'Already achieved'
                
        elif name in self.succes[1].keys():
            if self.succes[1][name] == 0:
                self.succes[1][name] = 1
                
            else:
                return f'Already achieved'  
            
        else:
            return f'Achievement not found'
    
    def remove_succes(self, name : str):
        if name in self.succes[0].keys():
            if self.succes[0][name] == 1:
                self.succes[0][name] = 0
                
            else:
                return f'Not achieved'
                
        elif name in self.succes[1].keys():
            if self.succes[1][name] == 1:
                self.succes[1][name] = 0
                
            else:
                return f'Not achieved'  
            
        else:
            return f'Achievement not found'
         
    def show_succes(self, status : str = 'base'):
        succes = []
        for s in self.succes[0].keys():
            if self.succes[0][s] == 1:
                succes.append(s)
                
        for s in self.succes[1].keys():
            if self.succes[1][s] == 1:
                succes.append(s)
            
        if len(succes) != 0:
            if status == 'string':
                succes = str(succes)
                return succes[1 : -1]
            
            else:
                return succes
        
        else:
            return 'No succes unlocked'
    
    def succes_nbr(self):
        succes = 0
        for s in self.succes[0].keys():
            if self.succes[0][s] == 1:
                succes += 1
                
        for s in self.succes[1].keys():
            if self.succes[1][s] == 1:
                succes += 1
                
        return succes
        
    def reset(self):
        for name in self.succes[0].keys():
            if self.succes[0][name] == 1:
                self.succes[0][name] = 0
                
        for name in self.succes[1].keys():
            if self.succes[1][name] == 1:
                self.succes[1][name] = 0
        

# Tests

'''
test = Succes(489470853072027685)
test.add_succes('Acteur du destin')
test.add_succes('Assassin')
print(f'{test.succes_nbr()} succès : {test.show_succes()}')
'''