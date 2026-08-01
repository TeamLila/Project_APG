
#Import time, install if not existent
try:
    import asyncio
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    import engine.pygame_main as game
except ImportError as e:
    from loggingFolder.loggerModule import MAIN_LOGGER as log
    log.warning("Error importing: " + str(e) + "\nattempting to fix")
    from debug_files.install_dep import dependencieInstaller
    dependencieInstaller()

async def gameStarter():
    await gameMain()


async def gameMain(): #NOSONAR #async without async used. Will be changed
    gamestate = game.GAME
    await game.run_game()



try:
    asyncio.run(gameStarter())
except Exception as e:
    from debug_files.errorModule import displayError
    log.error(e)
    displayError(e)