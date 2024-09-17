from typing import Callable, List, Literal, Optional
from PyQt6.QtWidgets import QWidget

from flim_components.components.inputs.input_number import InputInteger
from flim_components.components.inputs.input_select import InputSelect


class BinWidthInput(InputInteger):
    """
    A specific Flim implementation of InputInteger for bin width values in microseconds.
    This class sets default parameters for bin width input with predefined min, max, and default values.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        parent: QWidget = None,
        label: str = "Bin width (µs):",
        min_value: int = 1,
        max_value: int = 1000000,
        default_value: int = 1000,  # Default bin width value
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
        

class BinWidthSelector(InputSelect):
    """
    A specific Flim implementation of InputSelect for bin width values in microseconds.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        label: str = "Bin width (µs):",
        selected_value: int = 1,
        options: List[str] =  ["1", "10", "100", "1000"],
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