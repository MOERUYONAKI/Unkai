#  > - <  I P O R T S  > - <  #


import random as rdm 


#  > - <  F O N C T I O N S  > - <  #


def basic_roll(max : int):
    '''Dice roll / probabilities equals for each values
    > Return a number upper than 0 and lower or equal than the "max"'''
    nbr = rdm.randint(0, max)
    return nbr

def Katsu_roll(cmd : str):
    '''100 roll with bonus and malus
    > Return a number upper than 0 and lower or equal than 100 with malus or bonus'''
    command = []
    cmd_size = len(cmd) - 1
    
    # cmd spliting in command
    for elt in cmd:
        if elt.isdigit():
            command.append(int(elt))
            
        else:
            if elt in ["d", "+", "-"]:
                if elt != "d":
                    if "d" not in command:
                        return f'CommandError : "{elt}"'
                    
                    else:
                        command.append(elt)
                    
                else:
                    if "d" not in command:
                        command.append(elt)
                    
                    else:
                        return f'CommandError : "{elt}"'
                
            elif elt == " ":
                break
            
            else:
                return f'CommandError : "{elt}"'
            
    # split assembling
    if "d" not in command:
        return f'CommandError : "d" is required tu use this roll'
    
    else:
        i = command.index("d")
        
        # first assembling (rolls number)
        if i > 0:
            first = ""
            for idx in range(i):
                elt = command[idx]
                if type(elt) is int:
                    first += str(elt)
                    
                else:
                    break
                
            first = int(first)
            
        else:
            first = 1
        
        # roll check (if number after "d" is 100)
        if cmd_size > i:
            size = ""
            for idx in range(i + 1, len(command)):
                elt = command[idx]
                if type(elt) is int:
                    size += str(elt)
                    
                else:
                    break
            
            if int(size) != 100:
                return f'CommandError : invalide dice size, size must be "100"'
                
            if cmd_size > i + 3:
                if type(command[i + 4]) is int:
                    return f'CommandError : invalide dice size, size must be "100"'
                
        else:
            return f'CommandError : cannot find any dice size'
            
        # bonus assembling (with "+" and "-")
        def bonus_check(bns : list, i : int): # return the bonus value (without use "+" or "-")
            bonus = ""
            for idx in range(i + 1, len(command)):
                elt = command[idx]
                if type(elt) is int:
                    bonus += str(elt)
                    
                else:
                    break
                
            return int(bonus)
                
        bonus = 0        
        if len(command) - 1 > i + 4:
            i += 4
            bonus_index = []
            for i in range(len(command)):
                if command[i] in ["+", "-"] and type(command[i + 1]) is int:
                    bonus_index.append(i)
            
            for idx in bonus_index:
                if command[idx] == "+":
                    bonus += bonus_check(command, idx)
                    
            else:
                if command[idx] == "-":
                    bonus -= bonus_check(command, idx)
        
        # final command (assembled)
        command = [first, "d", 100, bonus]
        
        finals = []
        for i in range(first):
            roll = basic_roll(100)
            result = roll + bonus
            finals.append([roll, result])
            
        return [command, finals]
    
def eveil_roll(cmd : str = "base"):
    if cmd == "sup":
        roll = basic_roll(5000)
        return roll

    elif cmd == "base":
        first = basic_roll(10000)
        second = basic_roll(10000)
        rolls = [first, second]

        result = round(((first + second) / 2))
        results = [result, rolls]
        return results
    
    else:
        return 0

def Makai_roll(bonus : int = 0):
    rolls = []
    roll = basic_roll(100)

    if roll == 50 + bonus:
        roll = basic_roll(100)

        if roll == 50 + bonus:
            roll = basic_roll(100)
    
    rolls.append(roll)
    return [rolls, 49 + bonus]