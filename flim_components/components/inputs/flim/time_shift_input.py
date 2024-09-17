from typing import Literal
from PyQt6.QtWidgets import QWidget

from flim_components.components.inputs.input_number import InputInteger


class TimeShiftInput(InputInteger):
    """
    A specific Flim implementation of InputInteger for handling plot time shift.
    This class sets default parameters for Time Shift input with predefined min, max, and default values.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        parent: QWidget = None,
        label: str = "Time shift (bin):",
        min_value: int = 0,
        max_value: int = 255,
        default_value: int = 0,  # Default time shift value
        event_callback=None,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
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
        
