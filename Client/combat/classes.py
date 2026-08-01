from abc import ABC, abstractmethod

class ClassException(Exception):
    """
    Indicates that Something went wrong with the classes
    """
    pass


class BasicClass(ABC):
    """
    Used as a security check to ensure all classes are created correctly
    DO NOT INITILIZE THIS CLASS, ONLY SUB-CLASSES
    """
    
    @abstractmethod
    def get_damage_physical(self, STR):
        pass
    
    @abstractmethod
    def get_damage_magical(self, MP):
        pass













#END OF DEFINING, DO NOT CREATE NEW CLASSES BELOW HERE
#tests every class to ensure each is properly created
failedClasses = {}
for subclass in BasicClass.__subclasses__():
    try:
        subclass()
    except Exception as e:
        failedClasses[subclass.__name__] = e

if failedClasses:
    strBuilder = "1 or more Classes failed to initilize (see below):\n"
    for name, error in failedClasses.items():
        strBuilder += f"- {name} >> {error}\n"
    raise ClassException(strBuilder)