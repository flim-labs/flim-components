from typing import Callable, List, Optional
from PyQt6.QtWidgets import QWidget

from components.inputs.input_number import InputInteger
from components.inputs.input_select import InputSelect



class HarmonicsInput(InputInteger):
    """
    A specific Flim implementation of InputInteger for handling harmonics values.
    This class sets default parameters for harmonics input with predefined min, max, and default values.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        parent: QWidget = None,
        label: str = "Harmonics:",
        min_value: int = 1,
        max_value: int = 4,
        default_value: int = 0,  # Default harmonics value
        event_callback=None,
        layout_type: str = "vertical",
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


class HarmonicSelector(InputSelect):
    """
    A specific Flim implementation of InputSelect for harmonic selection.
    All parameters are optional and default values are used if not provided.
    """
    def __init__(
        self,
        label: str = "Harmonic displayed:",
        selected_value: int = 0,
        options: List[str] =  ["1", "2", "3", "4"],
        event_callback: Callable[[int], None] = None,
        layout_type: str = "vertical",
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