
#Import time, install if not existent
try:
    import asyncio
    from logging.loggerModule import MAIN_LOGGER as log
except ImportError as e:
    from debug_files.install_dep import dependencieInstaller
    dependencieInstaller()


def gameMain():
    #Need to add
    pass



try:
    gameMain()
except Exception as e:
    from debug_files.errorModule import displayError
    displayError(e)