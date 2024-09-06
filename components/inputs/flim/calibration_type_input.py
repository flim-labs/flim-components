from typing import Callable, List, Literal, Optional
from PyQt6.QtWidgets import QWidget

from components.inputs.input_select import InputSelect


class CalibrationTypeSelector(InputSelect):
    """
    A specific Flim implementation of InputSelect for calibration type selection.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        label: str = "Calibration:",
        selected_value: int = 0,
        options: List[str] =  ["None", "Phasors Ref."],
        event_callback: Callable[[int], None] = None,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        stylesheet: str | None = None,
        width: Optional[int] = None,
        parent: Optional[QWidget] = None
    ):
        # Initialize with optional parameters, using defaults if not provided
        super().__init__(
            label=label,
            selected_value=selected_value,
            options=options,
            event_callback=event_callback if event_callback is not None else self.default_callback,
            layout_type=layout_type,
            stylesheet=stylesheet,
            width=width,
            parent=parent
        )
    
    def default_callback(self, index: int):
        """
        A default callback function when no custom callback is provided.
        
        Parameters
        ----------
        index : int
            The index of the selected option.
        """
        print(f"Selected index: {index}")