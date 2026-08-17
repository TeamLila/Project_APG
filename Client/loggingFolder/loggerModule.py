import logging
# from enum import Enum
import os as OperatingSystem
from pathlib import Path
from datetime import datetime

APPDATA_PATH = OperatingSystem.getenv("APPDATA")
LOG_DIR = Path(APPDATA_PATH, "APG")
LOG_DIR.mkdir(exist_ok=True)

class CustomLogger(logging.Logger):
    def __init__(self, name: str):
        super().__init__(name, logging.DEBUG)

        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")

        # Console output
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        # File output
        file = logging.FileHandler(LOG_DIR / "apg.log", encoding="utf-8")
        file.setLevel(logging.DEBUG)
        file.setFormatter(formatter)

        self.addHandler(console)
        self.addHandler(file)

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
    
    def seperator(self, times: int = 1):
        """
        Prints a seperator
        """
        if times <= 0:
            return
        for _ in range(0, times):
            self.info("-----------------------------------------------------------------")

    def new_start(self):
        self.seperator(3)
        self.info(f"NEW LOGGING SESS, FROM: \"{datetime.today().strftime("%Y-%m-%d @ %H:%M:%S")}")
        self.seperator(3)


MAIN_LOGGER = CustomLogger("APG General Logger")