from random import randint, choice


# - Version 1 - obsolète

# '''
def create(climat : str, days : int, liste : int): # Création d'une météo
    
    if climat=='desert' or climat=='d':
        type='d'
    elif climat=='temperate' or climat=='t':
        type='t'
    elif climat=='cold' or climat=='c':
        type='c'
    elif climat=='dākurōdo' or climat=='daku':
        type='daku'
    else:
        pass
    rdm=randint(0,100) 
    L_temps = []
    T_temps = []

    def temp(type,rdm):
        if type=='d':
            if rdm<5:
                temps='🌪️ - venté'
            elif rdm>=5 and rdm<=72:
                temps='☀️ - ensoleillé'
            elif rdm>72 and rdm<=87:
                temps='☁️ - nuageux'
            elif rdm>87 and rdm<99:
                temps='🌩️ - orageux'
            elif rdm==99:
                temps='⛈️ - orageux et pluvieux'
            elif rdm==100:
                temps='🌧️ - pluvieux'
        elif type=='t':
            if rdm<5:
                temps='🌪️ - venté'
            elif rdm>=5 and rdm<=28:
                temps='☀️ - ensoleillé'
            elif rdm>28 and rdm<=62:
                temps='☁️ - nuageux'
            elif rdm>62 and rdm<92:
                temps='🌧️ - pluvieux'
            elif rdm>=92 and rdm<=90:
                temps='⛈️ - orageux et pluvieux'
            elif rdm>90:
                temps='🌩️ - orageux'
        elif type=='c':
            if rdm<=25:
                temps='☀️ - ensoleillé'
            elif rdm>25 and rdm<=55:
                temps='☁️ - nuageux'
            elif rdm>55 and rdm<=65:
                temps='🌪️ - venté'
            elif rdm>65 and rdm<=95:
                temps='🌨️ - neigeux' 
            elif rdm>95:
                temps='🌩️ - orageux'
        elif type=='daku':
            if rdm<=35:
                temps='🌑 - voile sombre'
            elif rdm>35 and rdm<=48:
                temps='🌪️ - venté'
            elif rdm>48 and rdm<=62:
                temps='☁️ - nuageux'
            elif rdm>62 and rdm<=80:
                temps='🌩️ - orageux'
            elif rdm>80 and rdm<=86:
                temps='⛈️ - orageux et pluvieux'
            elif rdm>86:
                temps='🌧️ - pluvieux'
        return temps
 
    if days<8 and days>0 and liste==1:
        for i in range(1,days+1): 
            if i==1:
                temps=temp(type,rdm)
                temps_1=temps
                L_temps.append(temps_1)
            elif i==2:
                temps=temp(type,rdm)
                temps_2=temps
                L_temps.append(temps_2)
            elif i==3:
                temps=temp(type,rdm)
                temps_3=temps
                L_temps.append(temps_3)
            elif i==4:
                temps=temp(type,rdm)
                temps_4=temps
                L_temps.append(temps_4)
            elif i==5:
                temps=temp(type,rdm)
                temps_5=temps
                L_temps.append(temps_5)
            elif i==6:
                temps=temp(type,rdm)
                temps_6=temps
                L_temps.append(temps_6)
            elif i==7:
                temps=temp(type,rdm)
                temps_7=temps
                L_temps.append(temps_7)
            change=randint(1,4)
            if change<=4 and change>=1:
                if change==1:
                    rdm-=50
                elif change==2:
                    rdm-=25
                elif change==3:
                    rdm+=25
                elif change==4:
                    rdm+=50
            if rdm<0 or rdm>100:
                if rdm<0:
                    rdm=0
                elif rdm>100:
                    rdm=100
        return L_temps
        
    if days<8 and days>0 and liste==2:
        if type=='d':
            tmp=float(randint(28,40))
        elif type=='t':
            tmp=float(randint(12,25))
        elif type=='c':
            tmp=float(randint(-10,10))
        elif type=='daku':
            tmp=float(randint(-5,12))
        for i in range(1,days+1):
            change=randint(1,9)
            if change==1:
                tmp-=2
                T_temps.append(tmp)
            elif change==2:
                tmp-=1.5
                T_temps.append(tmp)
            elif change==3:
                tmp-=1
                T_temps.append(tmp)
            elif change==4:
                tmp-=0.5
                T_temps.append(tmp)
            elif change==5:
                tmp=tmp
                T_temps.append(tmp)
            elif change==6:
                tmp+=0.5
                T_temps.append(tmp)
            elif change==7:
                tmp+=1
                T_temps.append(tmp)
            elif change==8:
                tmp+=1.5
                T_temps.append(tmp)
            elif change==9:
                tmp+=2
                T_temps.append(tmp)
        return T_temps
# ''' 
        

# - - -  V E R S I O N   2  - - - 
    

def temperature(climate_id : int, season_id : int):
    temp_min, temp_max = 0, 0

    # Définition des températures de base par climat (climate_id)
    if climate_id == 1: # - Climat montagnard
        temp_min, temp_max = -20, -5

    elif climate_id == 2: # - Climat froid
        temp_min, temp_max = -10, 10

    elif climate_id == 3: # - Climat tempéré
        temp_min, temp_max = 5, 25
    
    elif climate_id == 4: # - Climat chaud
        temp_min, temp_max = 20, 40

    elif climate_id == 5: # - Climat aride
        temp_min, temp_max = 35, 45

    else: # - Temérature moyenne (hors climat)
        temp_min, temp_max = 0, 30

    # Adaptation des bornes de base selon la saison (season_id)
    if season_id == 1: # - Hiver
        temp_min -= 0.08 * temp_min
        temp_max  -= 0.15 * temp_max 

    elif season_id == 1: # - Printemps
        temp_min -=  0.02 * temp_min
        temp_max -= -0.02 * temp_max

    elif season_id == 1: # - Été
        temp_min -= -0.05 * temp_min
        temp_max -= -0.12 * temp_max

    elif season_id == 1: # - Automne
        temp_min -= 0.03 * temp_min
        temp_max -= -0.02 * temp_max

    # Renvoie des bornes calculées
    return (temp_min, temp_max)

def temp_update(temp_min : int = 0, temp_max : int = 30, last_temp : float = None):
    temp = 0

    # Cas par défaut
    if temp_min == temp_max: # Bornes identiques
        temp = temp_min

    elif last_temp == None: # Pas de référentiel
        temp = randint(temp_min + 1, temp_max - 1)

    else:
        temp_m = (temp_min + temp_max) / 2
        update_values = [0.1 * randint(2, 24), -0.1 * randint(2, 24)]
        value = choice(update_values)

        # Application de la valeur de changement
        if (last_temp < temp_m and value < 0) or (last_temp > temp_m and value > 0):
            value = round(0.85 * value, 1)

        temp = last_temp + value

    # Renvoie de la nouvelle température 
    return temp

def weather(climate_id : int, season_id : int, temp : float):
    final_weather = 0
    weather_list = ['🌪️ - venté', '☀️ - ensoleillé', '☁️ - nuageux', '🌩️ - orageux', '⛈️ - orageux et pluvieux', '🌧️ - pluvieux', '🌨️ - neigeux', '🌊 - tempête'] # ID - 0 à 8
    base = randint(0, 100)

    # Adaptation des probabilités selon la saison (season_id)
    if season_id == 1: # - Hiver
        # Températures négatives
        if temp <= 0 and base < 20:
            final_weather = 0 # venté

        elif temp <= 0 and 20 <= base < 48:
            final_weather = 6 # neigeux

        elif temp <= 0 and 48 <= base < 60:
            final_weather = 3 # orageux

        elif temp <= 0 and 60 <= base < 78:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 78:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 25:
            final_weather = 0 # venté

        elif temp > 0 and 25 <= base < 42:
            final_weather = 5 # pluvieux

        elif temp <= 0 and 42 <= base < 50:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 50 <= base < 58:
            final_weather = 3 # orageux

        elif temp > 0 and 58 <= base < 82:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 82:
            final_weather = 1 # ensoleillé

    elif season_id == 1: # - Printemps
        # Températures négatives
        if temp <= 0 and base < 20:
            final_weather = 0 # venté

        elif temp <= 0 and 20 <= base < 60:
            final_weather = 6 # neigeux

        elif temp <= 0 and 60 <= base < 65:
            final_weather = 3 # orageux

        elif temp <= 0 and 65 <= base < 80:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 80:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 18:
            final_weather = 0 # venté

        elif temp > 0 and 18 <= base < 38:
            final_weather = 8 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 38 <= base < 46:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 46 <= base < 52:
            final_weather = 3 # orageux

        elif temp > 0 and 52 <= base < 75:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 75:
            final_weather = 1 # ensoleillé

    elif season_id == 1: # - Été
        # Températures négatives
        if temp <= 0 and base < 24:
            final_weather = 0 # venté

        elif temp <= 0 and 24 <= base < 42:
            final_weather = 6 # neigeux

        elif temp <= 0 and 42 <= base < 55:
            final_weather = 3 # orageux

        elif temp <= 0 and 55 <= base < 78:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 78:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 12:
            final_weather = 0 # venté

        elif temp > 0 and 12 <= base < 28:
            final_weather = 8 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 28 <= base < 35:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 35 <= base < 48:
            final_weather = 3 # orageux

        elif temp > 0 and 48 <= base < 70:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 70:
            final_weather = 1 # ensoleillé

    elif season_id == 1: # - Automne
        # Températures négatives
        if temp <= 0 and base < 25:
            final_weather = 0 # venté

        elif temp <= 0 and 25 <= base < 68:
            final_weather = 6 # neigeux

        elif temp <= 0 and 68 <= base < 74:
            final_weather = 3 # orageux

        elif temp <= 0 and 74 <= base < 85:
            final_weather = 2 # nuageux

        elif temp <= 0 and base > 85:
            final_weather = 1 # ensoleillé

        # Températures positives
        if temp > 0 and base < 18:
            final_weather = 0 # venté

        elif temp > 0 and 18 <= base < 40:
            final_weather = 8 if climate_id == 5 else 5 # pluvieux (ou tempête si aride)

        elif temp <= 0 and 40 <= base < 48:
            final_weather = 4 # orageux et pluvieux

        elif temp <= 0 and 48 <= base < 55:
            final_weather = 3 # orageux

        elif temp > 0 and 55 <= base < 78:
            final_weather = 2 # nuageux

        elif temp > 0 and base > 78:
            final_weather = 1 # ensoleillé

    # Renvoie des bornes calculées
    return [weather_list[final_weather], final_weather]