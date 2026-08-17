
#Import time, install if not existent
try:
    import asyncio
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    import engine.pygame_main as game
    import engine.areaLoader as areaLoader
    from engine.areaLoader import ValidAreas as AREA
except ImportError as e:
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    log.warning("Error importing: " + str(e) + "\nattempting to fix")
    from debug_files.install_dep import dependencieInstaller
    dependencieInstaller()

async def gameInitilizer():
    """
    Pre-loads most of the game
    """
    game.GAME.current_area = "hub"
    loadAreas()
    loadDoors()
    await gameMain()


async def gameMain(): #NOSONAR #async without async used. Will be changed
    """
    Runs post-init code and the main game loop
    """
    
    await game.run_game()

def loadAreas():
    """
    loads all areas currently added into the game
    """
    
    areaLoader.Area(AREA.HUB, None)
    areaLoader.Area(AREA.HUB_LEFT, None)
    areaLoader.Area(AREA.AP_DUNGEON, None)

def loadDoors():
    """
    loads all valid doors, including where they are, in which area and where they go
    """
    
    areaLoader.Door("hub", [1225, 30], [64, 64], AREA.AP_DUNGEON, [0,0], (77,33,33))
    areaLoader.Door("hub", [30, 30], [64, 64], AREA.HUB_LEFT, [1800, 30])
    areaLoader.Door("hub left", [1860, 30], [64,64], AREA.HUB, [40, 30])



#Start the Game and catch a big crash
try:
    log.new_start()
    asyncio.run(gameInitilizer())
except Exception as e:
    from debug_files.errorModule import displayError
    log.exception("FATAL ERROR CRASH, SEE BELOW")
    displayError(e + "\nLets hope the error is showing something usefull")
    raise