from typing import Callable, Literal
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QDoubleSpinBox, QWidget, QSizePolicy
from layouts.compact_layout import CompactLayout
from styles.inputs_styles import InputStyles
from utils.layout_utils import LayoutUtils


class BaseInputNumber(QWidget):
    """
    A reusable input widget for integer or float numbers with a label, customizable layout, and optional styling.

    Parameters
    ----------
    label : str
        The text to be displayed as the label for the input.
    min_value : int or float
        The minimum value allowed for the input.
    max_value : int or float
        The maximum value allowed for the input.
    default_value : int or float
        The initial value set for the input.
    event_callback : callable [int | float]
        A function that is called whenever the input value changes.
    enabled : bool, optional
        Whether the input is initially enabled (default is True).
    visible : bool, optional
        Whether the widget is initially visible (default is True).               
    layout_type : Literal ["horizontal", "vertical"], optional
        The layout type for the input and label, either "vertical" (default) or "horizontal".
    width : int, optional
        The default fixed input widget width (default is None).          
    stylesheet : str, optional
        An optional stylesheet to customize the appearance of the input widget (default is None).
    parent : QWidget, optional
        The parent widget of this input control, if any (default is None).
    """    
    def __init__(
        self,
        label: str,
        min_value: int | float,
        max_value: int | float,
        default_value: int | float,
        event_callback: Callable[[int | float], None],
        enabled: bool = True,
        visible: bool = True,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        width: int | None = None,
        stylesheet: str | None = None,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.default_value = default_value
        self.q_label = QLabel(label)
        self.control_layout =  (QVBoxLayout() if layout_type == "vertical" else QHBoxLayout())
        self.input = self.create_input(min_value, max_value, default_value)
        self.input.valueChanged.connect(event_callback)
        if width is not None:
            self.setFixedWidth(width)
        self.set_style(stylesheet if stylesheet is not None else InputStyles.input_number_style())
        self.control_layout.addWidget(self.q_label)
        self.control_layout.addWidget(self.input)
        self.setLayout(self.control_layout)
        self.set_enabled(enabled)
        self.set_visible(visible)
        
    def set_style(self, stylesheet: str):
        """
        Apply a custom stylesheet to the input widget.

        Parameters
        ----------
        stylesheet : str
            The stylesheet string to apply to the input widget.
        """        
        self.input.setStyleSheet(stylesheet)    

    def get_value(self) -> int | float:
        """
        Get the current value of the input.

        Returns
        -------
        int or float
            The current value of the input widget.
        """        
        return self.input.value()

    def set_value(self, value: float):
        """
        Set a new value for the input widget.

        Parameters
        ----------
        value : int or float
            The new value to set in the input widget.
        """        
        self.input.setValue(value)

    def reset_value(self):
        """
        Reset the input to its default value.
        """        
        self.input.setValue(self.default_value)
    
    def set_enabled(self, state):
        """
        Enable or disable the input widget.

        Parameters
        ----------
        state : bool
            If True, enables the input widget; if False, disables it.
        """        
        self.input.setEnabled(state) 
        
    def set_visible(self, state):
        """
        Show or hide the control layout and all its child widgets.

        Parameters
        ----------
        state : bool
            If True, makes the control layout visible; if False, hides it.
        """
        if state:
            LayoutUtils.show_layout(self.control_layout)
        else:
            LayoutUtils.hide_layout(self.control_layout)    
                  

    def is_enabled(self) -> bool:
        """
        Check if the input widget is enabled.

        Returns
        -------
        bool
            True if the input widget is enabled, False otherwise.
        """        
        return self.input.isEnabled()

    def set_label_text(self, text: str):
        """
        Set the text for the label associated with the input widget.

        Parameters
        ----------
        text : str
            The text to display on the label.
        """        
        self.q_label.setText(text)

    def set_tooltip(self, text: str):
        """
        Set a tooltip for the input widget.

        Parameters
        ----------
        text : str
            The text to display as a tooltip when the user hovers over the input widget.
        """        
        self.input.setToolTip(text)

    def set_range(self, min_value: int | float, max_value: int | float):
        """
        Set the minimum and maximum values allowed for the input widget.

        Parameters
        ----------
        min_value : int or float
            The minimum value that the input widget can accept.
        max_value : int or float
            The maximum value that the input widget can accept.
        """        
        self.input.setRange(min_value, max_value)
  
    def connect_value_changed(self, callback):
        """
        Connect a custom callback function to the input widget's valueChanged signal.

        Parameters
        ----------
        callback : callable
            The function to call when the value of the input widget changes.
        """        
        self.input.valueChanged.connect(callback)

    def create_input(self, min_value: int | float, max_value: int | float, default_value: int | float):
        raise NotImplementedError(
            "This method should be overridden in subclasses"
        )



class InputInteger(BaseInputNumber):
    """
    A specific implementation of BaseInputNumber for integer values using QSpinBox.
    """    
    def create_input(self, min_value: int, max_value: int, default_value: int):
        input_widget = QSpinBox()
        input_widget.setRange(min_value, max_value)
        input_widget.setValue(default_value)
        return input_widget


class InputFloat(BaseInputNumber):
    """
    A specific implementation of BaseInputNumber for float values using QDoubleSpinBox.
    """    
    def create_input(self, min_value: float, max_value: float, default_value: float):
        input_widget = QDoubleSpinBox()
        input_widget.setRange(min_value, max_value)
        input_widget.setValue(default_value)
        return input_widget