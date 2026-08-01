import pygame 
import asyncio
from pathlib import Path
import engine.assetLoader as assetLoader

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
    back_fill = None
    doors = {}
    
    
    
    def change_player_icon(self, nameOfIcon: str):
        image = pygame.image.load(assetLoader.getAsset(nameOfIcon)).convert_alpha()
        scaled = pygame.transform.scale(image, (64, 64))
        
        self.player_icon = scaled
    

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
    for name, door in GAME.doors.items():
        if player.colliderect(door):
            print(f"Collision with {name}")

def makeDoor(name: str, location: list[int], size: list[int]):
    combinedList = location + size
    GAME.doors[name] = pygame.Rect(combinedList)
    

def removeDoor(name: str):
    del GAME.doors[name]

def drawAllDoors():
    for _, door in GAME.doors.items():
        pygame.draw.rect(GAME.screen, (0,0,0), door)

#Main func
async def run_game():
    GAME.back_fill = (77, 77, 77)
    makeDoor("AP Dungeon Entrance", [500, 200], [64, 64])
    while GAME.running:
        #used for FPS limit
        frameTime = asyncio.sleep(1/GAME.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME.running = False
        

        keys = pygame.key.get_pressed()
        #Checks
        walking(keys)
        doorColide()
        
        #Quit (debug)
        if keys[pygame.K_q]:
            GAME.running = False
        
        #drawing
        GAME.screen.fill(GAME.back_fill)
        drawAllDoors()
        GAME.screen.blit(GAME.player_icon, (GAME.player_x, GAME.player_y))
        
        
        pygame.display.flip()
        
        await frameTime