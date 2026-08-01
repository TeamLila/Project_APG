"""
Holds The player-related Classes & Function
"""
from classes import BasicClass
from logging.loggerModule import MAIN_LOGGER as log


class Player:
    def __init__(self, health: int, magicPower: int, strengh: int, rpgClass: BasicClass):
        """
        Initilizes the Player class
        """
        
        #health
        self.health = health
        self.max_health = health
        #magic power
        self.magic_power = magicPower
        self.mana = 0
        self.max_mana = 0
        self.update_max_mana()
        #Strengh
        self.strengh = strengh
        #class
        self.current_class = rpgClass

    def update_max_mana(self):
        """
        Use After modifying magic power.
        updates the mana & Max Mana the player can hold
        """
        maxIncrease = (self.magic_power*10) - self.max_mana
        self.max_mana = maxIncrease
        self.mana += maxIncrease
    
    def take_damage_physical(self, damageTaken: int) -> int:
        """
        Damages the player Physicaly.
        
        @return the Actual damage taken
        """
        realDamage = damageTaken - round(self.strengh/4)
        self.health -= realDamage
        return realDamage
    
    def take_damage_magical(self, damageTaken: int) -> int:
        """
        Damages the player Magicaly
        
        @return the actual damage taken
        """
        realDamage = damageTaken - round(self.magic_power/4)
        self.health -= realDamage
        return realDamage
    
    def heal(self, healing) -> int:
        """
        Heals the player for the given healing or untill max, whichever is less
        
        @return the Actual healing
        """
        
        healingGot = min(self.health + healing, self.max_health)
        self.health = healingGot
        return healingGot
    
    def deal_damage_physical(self) -> int:
        """
        Returns the Players Physical Damage
        """
        return self.current_class.get_damage_physical(self.strengh)
    
    def deal_damage_magical(self) -> int:
        """
        Returns the Players Magical Damage
        """
        return self.current_class.get_damage_magical(self.magic_power)
        