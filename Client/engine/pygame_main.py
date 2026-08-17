import pygame 
import asyncio
from pathlib import Path

import engine.assetLoader as assetLoader
import engine.areaLoader as areaLoader
from loggingFolder.loggerModule import MAIN_LOGGER

class GameState:
    #init
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    pygame.display.set_caption("APG: The Archipelago role Playing game")
    running = True
    
    #Settings
    fps = 144
    player_icon = None
    
    #player-movement
    player_x = 100
    player_y = 100
    
    player_x_limits = [0, 1888]
    player_y_limits = [0, 1048]
    speed = 5
    
    #Area
    current_area: str
    area_background = None
    back_fill = None
    
    
    
    def change_player_icon(self, nameOfIcon: str):
        image = pygame.image.load(assetLoader.getAsset(nameOfIcon)).convert_alpha()
        scaled = pygame.transform.scale(image, (64, 64))
        
        self.player_icon = scaled
    
    def get_player_pos(self) -> list[int]:
        return [self.player_x, self.player_y]

GAME = GameState()
GAME.change_player_icon("Player_placeholder.png")


#Helper functions
def walking(keys):
    if keys[pygame.K_w]:
        GAME.player_y = max(GAME.player_y - GAME.speed, GAME.player_y_limits[0])
    if keys[pygame.K_s]:
        GAME.player_y = min(GAME.player_y + GAME.speed, GAME.player_y_limits[1])
    if keys[pygame.K_a]:
        GAME.player_x = max(GAME.player_x - GAME.speed, GAME.player_x_limits[0])
    if keys[pygame.K_d]:
        GAME.player_x = min(GAME.player_x + GAME.speed, GAME.player_x_limits[1])

def doorColide():
    player = GAME.player_icon.get_rect()
    player.topleft = (GAME.player_x, GAME.player_y)
    for door in areaLoader.AREA_TO_DOORS[GAME.current_area]:
        _, doorFrame =  door.get_draw_info()
        if player.colliderect(doorFrame):
            print(f"Collision with {door.leads_to.name}")
            GAME.current_area = door.get_area().get_area_name()
            GAME.area_background = door.get_area().get_area_pic()
            GAME.player_x, GAME.player_y = door.get_player_exit_pos()

def drawAllDoors():
    for door in areaLoader.AREA_TO_DOORS[GAME.current_area]:
        color, rect = door.get_draw_info()
        pygame.draw.rect(GAME.screen, color, rect)

#Main func
async def run_game():
    GAME.back_fill = (77, 77, 77)
    while GAME.running:
        #used for FPS limit
        frameTime = asyncio.create_task(
            asyncio.sleep(1/GAME.fps)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME.running = False
        

        keys = pygame.key.get_pressed()
        #Checks
        walking(keys)
        doorColide()
        
        #debug options (quit, get pos)
        if keys[pygame.K_q]:
            GAME.running = False
        if keys[pygame.K_p]:
            MAIN_LOGGER.debug(f"Current Pos: {GAME.get_player_pos()}")
        
        #drawing
        GAME.screen.fill(GAME.back_fill)
        drawAllDoors()
        GAME.screen.blit(GAME.player_icon, (GAME.player_x, GAME.player_y))
        
        
        pygame.display.flip()
        
        await frameTime