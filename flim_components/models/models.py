from typing import Callable, Literal, Optional, Tuple, TypedDict
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt


class Toggleable(TypedDict):
    text: str
    key: str
    active: bool


class InputIntegerParams(TypedDict, total=False):
    label: str
    min_value: int | float
    max_value: int | float
    default_value: int | float
    event_callback: Callable[[int | float], None]
    layout_type: Literal["horizontal", "vertical"]
    width: int | None
    stylesheet: str | None
    parent: QWidget | None


class SliderParams(TypedDict, total=False):
    orientation: Qt.Orientation
    min_value: int
    max_value: int
    initial_value: int
    event_callback: Callable[[int], None]
    visible: bool = True
    enabled: bool = True
    stylesheet: Optional[str] = None
    parent: Optional["QWidget"] = None


class PlotAxisParams(TypedDict):
    label: str
    label_color: str
    axis_color: str
    units: str
    
    
class PlotGridParams(TypedDict):
    show_x: bool
    show_y: bool
    alpha: float    
    

class PlotDimensionsParams(TypedDict):
    width: int | None
    height: int | None
    min_width: int | None
    min_height: int | None
    max_width: int | None
    max_height: int | None    
    

class PenParams(TypedDict):
    color: str | Tuple[int, int, int]
    width: int
    
class PlotScatterStyleParams(TypedDict):
    size: int
    pen: PenParams | None
    brush: str | None
    symbol: str
        
        
class PlotTextItemParams(TypedDict):
    text: str
    is_html: bool
    color: str | Tuple[int, int, int]
    anchor: Tuple[float, float] 
    position: Tuple[float, float] | None  
    pixel_size: int
     