from pygame import Rect
from pathlib import Path
from enum import Enum

from engine.assetLoader import getAsset


class ValidAreas(Enum):
    HUB_RIGHT = "hub right"
    HUB = "hub"
    HUB_LEFT = "hub left"
    
    AP_DUNGEON = "ap dungeon"
    
    SHOP = "shop"
    
    HOME = "home"

class Area:
    name: ValidAreas
    area_background: Path|None
    
    def __init__(self, name: ValidAreas, area_background: Path|str|None):
        if type(area_background) is str:
            area_background = getAsset(area_background)
        self.name = name
        self.area_background = area_background
        
        LIST_OF_AREAS[self.name] = self
        AREA_TO_DOORS.setdefault(name.value, [])
    
    def get_area_pic(self):
        return self.area_background

    def get_area_name(self):
        return self.name.value

class Door:
    pos: list[int]
    size: list[int]
    leads_to: ValidAreas
    color: list[int]
    
    after_enter_player_pos: list[int]
    
    def new(
        self,
        in_area: str,
        pos: list[int],
        size: list[int],
        leads_to: ValidAreas,
        new_player_pos: list[int],
        color: list[int] = (0,0,0)
    ):
        self.__init__(in_area, pos, size, leads_to, new_player_pos, color)
    def __init__(
        self,
        in_area: str,
        pos: list[int],
        size: list[int],
        leads_to: ValidAreas,
        new_player_pos: list[int],
        color: list[int] = (0,0,0)
    ):
        #test color
        if len(color) != 3:
            raise ValueError(f"INVALID RGB VALUES: expected 3 values, got {len(color)}")
        for rgbVal in color:
            if rgbVal > 255:
                raise ValueError("INVALID RGB VALUES: expected value between 0 and 255, got at least one ot of range")
        
        global AREA_TO_DOORS
        
        self.pos = pos
        self.size = size
        self.color = color
        self.leads_to = leads_to
        self.after_enter_player_pos = new_player_pos
        
        
        AREA_TO_DOORS.setdefault(in_area, []).append(self)
    
    
    def get_draw_info(self) -> tuple[list[int], list[int]]:
        return self.color, Rect(self.pos + self.size)

    def get_area(self) -> Area:
        return LIST_OF_AREAS[self.leads_to]

    def get_player_exit_pos(self) -> tuple[int, int]:
        return self.after_enter_player_pos





LIST_OF_AREAS: dict[ValidAreas, Area] = {}
AREA_TO_DOORS: dict[str, list[Door]] = {}