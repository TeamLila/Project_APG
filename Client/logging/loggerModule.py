import logging
from enum import Enum

MAIN_LOGGER: logging.Logger

class CustomLogger(logging.Logger):
    def __init__(self, name: str, level: int = logging.NOTSET):
        super().__init__(name, level)
    
    
        if not self.handlers:
            handler = logging.StreamHandler()
            
            formatter = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
                datefmt="%H:%M:%S"
            )
            
            handler.setFormatter(formatter)
            self.addHandler(handler)
            
            self.propagate = False
        
    def debugPrint(self, name: str, value):
        """
        Prints the name & Value of a Variable for debugging
        """
        self.debug(f"Variable Debug: {name} == {value}")
    
    def setDebugMode(self):
        """
        Sets the level to debug
        """
        self.level = logging.DEBUG
    
    def seperator(self):
        """
        Prints a seperator
        """
        self.info("-----------------------------------------------------------------")



MAIN_LOGGER = CustomLogger("APG", logging.INFO)