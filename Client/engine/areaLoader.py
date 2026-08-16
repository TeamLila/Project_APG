from pygame import Rect
from pathlib import Path
from engine.assetLoader import getAsset

class Door:
    pos: list[int]
    size: list[int]
    leads_to: str
    color: list[int]
    
    def new(
        self,
        in_area: str,
        pos: list[int],
        size: list[int],
        leads_to: str,
        color: list[int] = (0,0,0)
    ):
        self.__init__(in_area, pos, size, leads_to, color)
    def __init__(
        self,
        in_area: str,
        pos: list[int],
        size: list[int],
        leads_to: str,
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
        
        
        AREA_TO_DOORS.setdefault(in_area, []).append(self)
    
    
    def get_draw_info(self) -> tuple[list[int], list[int]]:
        return self.color, Rect(self.pos + self.size)

class Area:
    name: str
    area_background: Path
    
    def __init__(self, name: str, area_background: Path|str):
        if type(area_background) is str:
            area_background = getAsset(area_background)
        self.name = name
        self.area_background = area_background
        
        LIST_OF_AREAS.append(self)



LIST_OF_AREAS: list[Area] = []
AREA_TO_DOORS: dict[str, list[Door]] = {}