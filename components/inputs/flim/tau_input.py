from typing import Literal
from PyQt6.QtWidgets import QWidget

from components.inputs.input_number import InputFloat

class TauInput(InputFloat):
    """
    A specific Flim implementation of InputFloat for handling tau values.
    This class sets default parameters for tau with predefined min, max, and default values.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        parent: QWidget = None,
        label: str = "TAU (ns):",
        min_value: float = 0,
        max_value: float = 1000,
        default_value: float = 0,  # Default tau value
        event_callback=None,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        width: int | None = None,
        stylesheet: str | None = None
    ):
        # Initialize with optional parameters, using defaults if not provided
        super().__init__(
            label=label,
            min_value=min_value,
            max_value=max_value,
            default_value=default_value,
            event_callback=event_callback,
            layout_type=layout_type,
            width=width,
            stylesheet=stylesheet,
            parent=parent
        )