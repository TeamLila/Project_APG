
#Import time, install if not existent
try:
    import asyncio
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    import engine.pygame_main as game
    import engine.areaLoader as areaLoader
except ImportError as e:
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    log.warning("Error importing: " + str(e) + "\nattempting to fix")
    from debug_files.install_dep import dependencieInstaller
    dependencieInstaller()

async def gameStarter():
    await gameMain()


async def gameMain(): #NOSONAR #async without async used. Will be changed
    game.GAME.current_area = "Hub"
    areaLoader.Door("Hub", [1225, 30], [64, 64], "AP Dungeon Entrance", (77,33,33))
    await game.run_game()



try:
    asyncio.run(gameStarter())
except Exception as e:
    from debug_files.errorModule import displayError
    log.exception("FATAL ERROR CRASH, SEE BELOW")
    displayError(e)
    raise