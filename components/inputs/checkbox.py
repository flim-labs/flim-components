from typing import Callable, Optional
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from components.inputs.fancy_checkbox import PaintedCheckbox
from layouts.compact_layout import CompactLayout
from styles.inputs_styles import InputStyles


class Checkbox(QWidget):
    """
    A customizable checkbox that can be either a standard checkbox or a fancy
    checkbox with a label. The appearance and behavior are adjusted based on the
    `fancy` parameter.

    Parameters
    ----------
    key : int
        A unique identifier for the checkbox, useful for distinguishing between
        different checkboxes when handling events.
    label : str
        The text displayed next to the checkbox, providing a description or label
        for the checkbox.
    event_callback : Callable[[bool], None]
        The function to be called whenever the checkbox's state changes. This
        function receives the new checked state as a boolean parameter.
    checked : bool, optional
        The initial checked state of the checkbox. Defaults to False.
    enabled : bool, optional
        Whether the checkbox is enabled (True) or disabled (False). Defaults to True.
    visible : bool, optional
        Whether the checkbox is visible (True) or hidden (False). Defaults to True.
    checkbox_color : str, optional
        The color of the checkbox when it is checked. Defaults to "#1E90FF".
    checkbox_color_unchecked : str, optional
        The color of the checkbox when it is unchecked. Defaults to "#6b6a6a".
    label_color : str, optional
        The color of the label text. Defaults to "#f8f8f8".
    border_color : str, optional
        The color of the checkbox border. Defaults to "#252525".
    stylesheet : str, optional
        An optional stylesheet for further customizing the checkbox's appearance.
        If not provided, a default style will be applied. Defaults to None.
    fancy : bool, optional
        Whether to use a custom fancy checkbox (True) or a standard checkbox (False). Defaults to False.
    parent : QWidget, optional
        The parent widget of this checkbox. Defaults to None.
    """
    
    toggled = pyqtSignal(bool)  # Signal to emit when the checkbox state changes

    def __init__(
        self,
        key: int,
        label: str,
        event_callback: Callable[[bool], None],
        checked: bool = False,
        enabled: bool = True,
        visible: bool = True,
        checkbox_color: str = "#1E90FF",
        checkbox_color_unchecked: str = "#6b6a6a",
        label_color: str = "#f8f8f8",
        border_color: str = "#252525",
        stylesheet: Optional[str] = None,
        fancy: bool = False,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.key = key
        self.label = label
        self.checked = checked
        self.visible = visible
        self.enabled = enabled
        self.event_callback = event_callback
        self.checkbox_color = checkbox_color
        self.checkbox_color_unchecked = checkbox_color_unchecked
        self.label_color = label_color
        self.border_color = border_color
        self.stylesheet = stylesheet
        self.fancy = fancy

        if self.fancy:
            self._init_fancy_checkbox()
        else:
            self._init_standard_checkbox()

        self.set_checked(checked)
        self.setEnabled(enabled)
        self.setVisible(visible)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def _init_standard_checkbox(self):
        """
        Initialize a standard checkbox.
        """
        self.checkbox = QCheckBox(self.label, self)
        self.checkbox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.set_style(self.stylesheet)
        self.checkbox.stateChanged.connect(self._on_state_changed)
        layout = CompactLayout(QHBoxLayout())
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def _init_fancy_checkbox(self):
        """
        Initialize a fancy checkbox with a label.
        """
        self.checkbox = PaintedCheckbox(
            self.checkbox_color,
            self.checkbox_color_unchecked,
            checked=self.checked,
            enabled=self.enabled,
            parent=self
        )
        self.label_widget = QLabel(self.label, self)
        self.label_widget.setCursor(Qt.CursorShape.PointingHandCursor)

        self.checkbox.toggled.connect(self._on_state_changed)
        self.label_widget.mousePressEvent = self.checkbox.mousePressEvent  # Forward mouse press event
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label_widget)
        self.setLayout(layout)

    def _on_state_changed(self, state: bool | int):
        """
        Handle the state change event of the checkbox.

        Parameters
        ----------
        state : int
            The new state of the checkbox, where 0 | False means unchecked and 2 | True means checked.
        """
        checked = state == 2 or state == True
        self.event_callback(checked)
        self.toggled.emit(checked)

    def set_style(self, stylesheet: Optional[str]):
        """
        Apply the provided stylesheet or the default checkbox style.

        Parameters
        ----------
        stylesheet : str, optional
            The stylesheet string to apply to the checkbox. If not provided,
            a default style based on the provided colors will be applied.
        """
        if not self.fancy:
            self.setStyleSheet(
                stylesheet
                if stylesheet is not None
                else InputStyles.checkbox_style(
                    self.checkbox_color,
                    self.checkbox_color_unchecked,
                    self.label_color,
                    self.border_color
                )
            )
        # No styling needed for FancyCheckbox, handled separately

    def set_checked(self, checked: bool):
        """
        Set the checked state of the checkbox.

        Parameters
        ----------
        checked : bool
            If True, check the checkbox; if False, uncheck it.
        """
        if self.fancy:
            self.checkbox.set_checked(checked)
        else:
            self.checkbox.setChecked(checked)

    def is_checked(self) -> bool:
        """
        Check if the checkbox is checked.

        Returns
        -------
        bool
            True if the checkbox is checked, False otherwise.
        """
        if self.fancy:
            return self.checkbox.is_checked()  
        return self.checkbox.isChecked()      
    

    def set_label(self, label: str):
        """
        Set the label text for the checkbox.

        Parameters
        ----------
        label : str
            The new label text to display next to the checkbox.
        """
        if self.fancy:
            self.label_widget.setText(label)
        else:
            self.checkbox.setText(label)

    def set_enabled(self, enabled: bool):
        """
        Enable or disable the checkbox and its label.

        Parameters
        ----------
        enabled : bool
            If True, enable the checkbox; if False, disable it.
        """
        if self.fancy:
            self.checkbox.set_enabled(enabled)
            self.label_widget.setEnabled(enabled)
        else:
            self.checkbox.setEnabled(enabled)

    def set_visible(self, visible: bool):
        """
        Show or hide the checkbox and its label.

        Parameters
        ----------
        visible : bool
            If True, show the checkbox and label; if False, hide them.
        """
        if self.fancy:
            self.checkbox.setVisible(visible)
            self.label_widget.setVisible(visible)
        super().setVisible(visible)



class WrappedCheckbox(QWidget):
    """
    A wrapper for a customizable checkbox, which includes additional styling
    options for the checkbox and its surrounding wrapper.

    Parameters
    ----------
    key : int
        A unique identifier for the checkbox, useful for distinguishing between
        different checkboxes when handling events.
    label : str
        The text displayed next to the checkbox, providing a description or label
        for the checkbox.
    event_callback : Callable[[bool], None]
        The function to be called whenever the checkbox's state changes. This
        function receives the new checked state as a boolean parameter.
    fancy : bool, optional
        Whether to use a custom fancy checkbox (True) or a standard checkbox (False). Defaults to False.        
    checked : bool, optional
        The initial checked state of the checkbox. Defaults to False.
    enabled : bool, optional
        Whether the checkbox is enabled (True) or disabled (False). Defaults to True.
    visible : bool, optional
        Whether the checkbox is visible (True) or hidden (False). Defaults to True.
    checkbox_color : str, optional
        The color of the checkbox when it is checked. Defaults to "#1E90FF".
    checkbox_color_unchecked : str, optional
        The color of the checkbox when it is unchecked. Defaults to "#6b6a6a".
    label_color : str, optional
        The color of the label text. Defaults to "#f8f8f8".
    border_color : str, optional
        The color of the checkbox border. Defaults to "#252525".
    wrapper_style_identifier : str, optional
        The id name used in the custom stylesheet for the checkbox wrapper. Defaults to "wrapper".        
    checkbox_stylesheet : str, optional
        An optional stylesheet for further customizing the appearance of the checkbox itself. Defaults to None.
    checkbox_wrapper_stylesheet : str, optional
        An optional stylesheet for further customizing the appearance of the wrapper widget. Defaults to None.
    parent : QWidget, optional
        The parent widget of this wrapped checkbox. Defaults to None.
    """

    def __init__(
        self,
        key: int,
        label: str,
        event_callback: Callable[[bool], None],
        fancy: bool = False,
        checked: bool = False,
        enabled: bool = True,
        visible: bool = True,
        checkbox_color: str = "#1E90FF",
        checkbox_color_unchecked: str = "#6b6a6a",
        label_color: str = "#f8f8f8",
        border_color: str = "#252525",
        checkbox_stylesheet: Optional[str] = None,
        wrapper_style_identifier: str = "wrapper",
        checkbox_wrapper_stylesheet: Optional[str] = None,
        checkbox_wrapper_height: int | None = None,
        checkbox_wrapper_width: int | None = None,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.key = key
        self.label = label
        self.event_callback = event_callback
        self.fancy = fancy
        self.checked = checked
        self.enabled = enabled
        self.visible = visible
        self.checkbox_color = checkbox_color
        self.checkbox_color_unchecked = checkbox_color_unchecked
        self.label_color = label_color
        self.border_color = border_color
        self.checkbox_stylesheet = checkbox_stylesheet
        self.checkbox_wrapper_stylesheet = checkbox_wrapper_stylesheet
        self.wrapper = QWidget()
        self.wrapper.setObjectName(wrapper_style_identifier)

        if checkbox_wrapper_height:
            self.setFixedHeight(checkbox_wrapper_height)
        if checkbox_wrapper_height:
            self.setFixedWidth(checkbox_wrapper_width)

        self.checkbox = self._create_checkbox()

        row = QHBoxLayout()
        row.addWidget(self.checkbox)
        self.wrapper.setLayout(row)
        vbox = CompactLayout(QVBoxLayout())
        vbox.addWidget(self.wrapper)
        self.setLayout(vbox)
        
        if self.checkbox_wrapper_stylesheet is not None:
            self.wrapper.setStyleSheet(self.checkbox_wrapper_stylesheet)        

    def _create_checkbox(self) -> Checkbox:
        """
        Creates and configures the Checkbox instance with the specified styles and
        properties.

        Returns
        -------
        Checkbox
            The configured Checkbox instance.
        """
        checkbox_stylesheet = (
            self.checkbox_stylesheet
            if self.checkbox_stylesheet
            else InputStyles.wrapped_checkbox_style(
                self.checkbox_color, self.checkbox_color_unchecked, self.label_color
            )
        )
        return Checkbox(
            key=self.key,
            fancy=self.fancy,
            label=self.label,
            event_callback=self.event_callback,
            checked=self.checked,
            enabled=self.enabled,
            visible=self.visible,
            checkbox_color=self.checkbox_color,
            checkbox_color_unchecked=self.checkbox_color_unchecked,
            label_color=self.label_color,
            border_color=self.border_color,
            stylesheet=checkbox_stylesheet,
        )

    def set_enabled(self, state: bool):
        """
        Enable or disable the checkbox.

        Parameters
        ----------
        state : bool
            If True, enables the checkbox; if False, disables it.
        """
        self.checkbox.setEnabled(state)

    def set_visible(self, state: bool):
        """
        Show or hide the checkbox wrapper and its checkbox.

        Parameters
        ----------
        state : bool
            If True, makes the checkbox wrapper and checkbox visible; if False, hides them.
        """
        self.setVisible(state)

    def is_enabled(self) -> bool:
        """
        Check if the checkbox is enabled.

        Returns
        -------
        bool
            True if the checkbox is enabled, False otherwise.
        """
        return self.checkbox.isEnabled()

    def is_checked(self) -> bool:
        """
        Check if the checkbox is checked.

        Returns
        -------
        bool
            True if the checkbox is checked, False otherwise.
        """
        return self.checkbox.isChecked()

    def get_label(self) -> str:
        """
        Get the label text of the checkbox.

        Returns
        -------
        str
            The label text of the checkbox.
        """
        return self.label

    def get_key(self) -> int:
        """
        Get the unique key of the checkbox.

        Returns
        -------
        int
            The unique key of the checkbox.
        """
        return self.key

    def set_checked(self, checked: bool):
        """
        Set the checked state of the checkbox.

        Parameters
        ----------
        checked : bool
            If True, check the checkbox; if False, uncheck it.
        """
        self.checkbox.setChecked(checked)

    def set_label(self, label: str):
        """
        Set the label text for the checkbox.

        Parameters
        ----------
        label : str
            The new label text to display next to the checkbox.
        """
        self.checkbox.setText(label)

    def set_checkbox_stylesheet(self, stylesheet: str):
        """
        Update the stylesheet for the checkbox.

        Parameters
        ----------
        stylesheet : str
            The new stylesheet string to apply to the checkbox.
        """
        self.checkbox_stylesheet = stylesheet
        self.checkbox.setStyleSheet(stylesheet)

    def set_wrapper_stylesheet(self, stylesheet: str):
        """
        Update the stylesheet for the checkbox wrapper.

        Parameters
        ----------
        stylesheet : str
            The new stylesheet string to apply to the checkbox wrapper.
        """
        self.checkbox_wrapper_stylesheet = stylesheet
        self.setStyleSheet(stylesheet)
