from typing import Callable, Optional, TypedDict
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
    layout_type: str
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
