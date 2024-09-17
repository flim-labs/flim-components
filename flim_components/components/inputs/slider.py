from PyQt6.QtWidgets import QSlider, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from typing import Callable, Literal, Optional

from flim_components.components.inputs.input_number import InputInteger



class Slider(QSlider):
    """
    A reusable and customizable QSlider class.

    Parameters
    ----------
    orientation : Qt.Orientation
        The orientation of the slider (Horizontal or Vertical).
    min_value : int
        The minimum value of the slider.
    max_value : int
        The maximum value of the slider.
    initial_value : int
        The initial value of the slider.
    event_callback : Callable[[int], None]
        Function to be called when the slider value changes.
    visible : bool, optional
        Whether the slider is initially visible (default is True).
    enabled : bool, optional
        Whether the slider is initially enabled (default is True).
    stylesheet : str, optional
        A custom stylesheet for the slider (default is None).
    parent : QWidget, optional
        The parent widget of the slider (default is None).
    """

    def __init__(
        self,
        orientation: Qt.Orientation,
        min_value: int,
        max_value: int,
        initial_value: int,
        event_callback: Callable[[int], None],
        visible: bool = True,
        enabled: bool = True,
        stylesheet: Optional[str] = None,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(orientation, parent)

        # Setup slider parameters
        self.setRange(min_value, max_value)
        self.setValue(initial_value)
        self.valueChanged.connect(event_callback)
        self.setEnabled(enabled)
        self.setVisible(visible)

        # Apply custom style if provided
        if stylesheet is not None:
            self.set_style(stylesheet)

    def get_value(self) -> int:
        """
        Retrieve the current slider value.

        Returns
        -------
        int
            The current value of the slider.
        """
        return self.value()

    def set_value(self, new_value: int) -> None:
        """
        Update the slider value programmatically.

        Parameters
        ----------
        new_value : int
            The new value to set for the slider.
        """
        self.setValue(new_value)

    def set_range(self, min_value: int, max_value: int) -> None:
        """
        Update the slider's range programmatically.

        Parameters
        ----------
        min_value : int
            The minimum value of the slider.
        max_value : int
            The maximum value of the slider.
        """
        self.setRange(min_value, max_value)

    def set_style(self, slider_style: str) -> None:
        """
        Apply a custom stylesheet to the slider.

        Parameters
        ----------
        slider_style : str
            The custom stylesheet to apply to the slider.
        """
        self.setStyleSheet(slider_style)

    def set_enabled(self, state: bool) -> None:
        """
        Enable or disable the slider.

        Parameters
        ----------
        state : bool
            If True, enables the slider; if False, disables it.
        """
        self.setEnabled(state)

    def set_visible(self, state: bool) -> None:
        """
        Show or hide the slider.

        Parameters
        ----------
        state : bool
            If True, makes the slider visible; if False, hides it.
        """
        self.setVisible(state)

    def is_enabled(self) -> bool:
        """
        Check if the slider is enabled.

        Returns
        -------
        bool
            True if the slider is enabled, False otherwise.
        """
        return self.isEnabled()
    
    
    
class SliderWithInput(QWidget):
    """
    A widget that combines a Slider and an InputInteger, with customizable layout options.

    Parameters
    ----------
    slider : Slider
        An instance of the `Slider` class to be displayed.
    input_number : InputInteger
        An instance of the `InputInteger` class, which represents the input number field bound to the slider.
    enabled : bool, optional
        Whether the slider and input number are initially enabled (default is True).
    visible : bool, optional
        Whether the slider and input number are initially visible (default is True).
    layout_type : Literal["horizontal", "vertical"], optional
        The orientation of the layout. If "horizontal", the components are placed side-by-side. 
        If "vertical", they are stacked (default is "horizontal").
    input_position : Literal["top", "right", "bottom", "left"], optional
        The position of the input number relative to the slider. Possible values:
        - "top": Input is above the slider.
        - "right": Input is to the right of the slider (default).
        - "bottom": Input is below the slider.
        - "left": Input is to the left of the slider.
    spacing : int, optional
        The spacing between the slider and input number in the layout, in pixels (default is 10).
    parent : QWidget, optional
        The parent widget of the slider and input number combination (default is None).
    """    
    def __init__(
        self,
        slider: Slider,
        input_number: InputInteger,
        enabled: bool = True,
        visible: bool = True,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        input_position: Literal["top", "right", "bottom", "left"] = "right",
        spacing: int = 10,
        parent: Optional["QWidget"] = None,
    ) -> None:
        super().__init__(parent)
        self.slider = slider
        self.input_number = input_number
        self.set_enabled(enabled)
        self.set_visible(visible)
  
        # Create component layout
        if layout_type == "horizontal":
            layout = QHBoxLayout()
        else:
            layout = QVBoxLayout()
        
        layout.setSpacing(spacing)

        if input_position == "right":
            layout.addWidget(self.slider)
            layout.addWidget(self.input_number)
        elif input_position == "left":
            layout.addWidget(self.input_number)
            layout.addWidget(self.slider)
        elif input_position == "top":
            layout.addWidget(self.input_number)
            layout.addWidget(self.slider)
        elif input_position == "bottom":
            layout.addWidget(self.slider)
            layout.addWidget(self.input_number)
        
        self.setLayout(layout)

        # Sync slider and input number values on changes
        self.slider.valueChanged.connect(self.input_number.set_value)
        self.input_number.input.valueChanged.connect(self.slider.set_value)
        
        
    def set_enabled(self, state: bool) -> None:
        """
        Enable or disable both slider and input number widgets.

        Parameters
        ----------
        state : bool
            If True, enables the slider and the input number; if False, disables them.
        """
        self.setEnabled(state)
        self.input_number.set_enabled(state)
        self.slider.set_enabled(state)
        

    def set_visible(self, state: bool) -> None:
        """
        Show or hide the slider and the input number.

        Parameters
        ----------
        state : bool
            If True, makes the slider and the input number visible; if False, hides them.
        """
        self.setVisible(state)
        self.input_number.set_visible(state)
        self.slider.set_visible(state)

    def is_enabled(self) -> bool:
        """
        Check if the slider and the input number are enabled.

        Returns
        -------
        bool
            True if the slider and the input number are enabled, False otherwise.
        """
        return self.isEnabled()        
    
    def get_value(self) -> int:
        """
        Retrieve the current inputs value.

        Returns
        -------
        int
            The current inputs value.
        """
        return self.slider.value()

    def set_value(self, new_value: int) -> None:
        """
        Update the slider and the input number value programmatically.

        Parameters
        ----------
        new_value : int
            The new value to set for the slider and the input number.
        """
        self.slider.set_value(new_value)  
        self.input_number.set_value(new_value)  


 
    
    
class SliderWithInputFactory:
    """
    A factory for creating a SliderWithInput widget with default configurations and optional callbacks.

    Methods
    -------
    create_slider_with_input(
        slider_params: dict,
        input_params: dict,
        enabled: bool = True,
        visible: bool = True,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        input_position: Literal["top", "right", "bottom", "left"] = "right",
        spacing: int = 10,
        parent: Optional[QWidget] = None
    ) -> SliderWithInput
        Create a SliderWithInput widget with the specified parameters.
    """

    @staticmethod
    def create_slider_with_input(
        slider_params: dict,
        input_params: dict,
        enabled: bool = True,
        visible: bool = True,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        input_position: Literal["top", "right", "bottom", "left"] = "right",
        spacing: int = 10,
        parent: Optional[QWidget] = None
    ) -> SliderWithInput:
        """
        Create a SliderWithInput widget with the specified parameters.

        Parameters
        ----------
        slider_params : SliderParams
            A dictionary containing parameters for creating the Slider instance.
        input_params : InputIntegerParams
            A dictionary containing parameters for creating the InputInteger instance.
        enabled : bool, optional
            Whether the slider and input number are initially enabled (default is True).
        visible : bool, optional
            Whether the slider and input number are initially visible (default is True).
        layout_type : Literal["horizontal", "vertical"], optional
            The orientation of the layout (default is "horizontal").
        input_position : Literal["top", "right", "bottom", "left"], optional
            The position of the input number relative to the slider (default is "right").
        spacing : int, optional
            The spacing between the slider and input number (default is 10).
        parent : QWidget, optional
            The parent widget of the SliderWithInput (default is None).

        Returns
        -------
        SliderWithInput
            An instance of SliderWithInput initialized with the given parameters.
        """
        # Create Slider instance
        slider = Slider(
            orientation=slider_params.get('orientation', Qt.Orientation.Horizontal),
            min_value=slider_params.get('min_value', 0),
            max_value=slider_params.get('max_value', 255),
            initial_value=slider_params.get('initial_value', 0),
            event_callback=slider_params.get('event_callback', lambda x: None),
            visible=slider_params.get('visible', True),
            enabled=slider_params.get('enabled', True),          
            stylesheet=slider_params.get('stylesheet', None),
            parent=slider_params.get('parent', None),
        )

        # Create InputInteger instance
        input_number = InputInteger(
            label=input_params.get('label', "Time shift (bin):"),
            min_value=input_params.get('min_value', 0),
            max_value=input_params.get('max_value', 255),
            default_value=input_params.get('default_value', 0),
            event_callback=input_params.get('event_callback', lambda x: None),
            visible=slider_params.get('visible', True),
            enabled=slider_params.get('enabled', True),               
            layout_type=input_params.get('layout_type', "horizontal"),
            width=input_params.get('width', None),
            stylesheet=input_params.get('stylesheet', None),
            parent=input_params.get('parent', None),
        )

        # Create and return SliderWithInput instance
        return SliderWithInput(
            slider=slider,
            input_number=input_number,
            enabled=enabled,
            visible=visible,
            layout_type=layout_type,
            input_position=input_position,
            spacing=spacing,
            parent=parent
        )    