from typing import Callable, Optional
from PyQt6.QtWidgets import QWidget, QCheckBox, QHBoxLayout
from PyQt6.QtCore import Qt
from styles.inputs_styles import InputStyles


class Checkbox(QCheckBox):
    """
    A customizable checkbox that extends QCheckBox, offering options for
    customizing colors, label text, initial state, and overall appearance.

    Parameters
    ----------
    key : int
        A unique identifier for the checkbox, useful for distinguishing between
        different checkboxes when handling events.
    label : str
        The text displayed next to the checkbox, providing a description or label
        for the checkbox.
    event_callback : callable
        The function to be called whenever the checkbox's state changes.
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
    parent : QWidget, optional
        The parent widget of this checkbox. Defaults to None.
    """

    def __init__(
        self,
        key: int,
        label: str,
        event_callback,
        checked: bool = False,
        enabled: bool = True,
        visible: bool = True,
        checkbox_color: str = "#1E90FF",
        checkbox_color_unchecked: str = "#6b6a6a",
        label_color: str = "#f8f8f8",
        border_color: str = "#252525",
        stylesheet: str | None = None,
        parent: QWidget = None,
    ):
        super().__init__(label, parent)
        self.key = key
        self.label = label
        self.checkbox_color = checkbox_color
        self.checkbox_color_unchecked = checkbox_color_unchecked
        self.label_color = label_color
        self.border_color = border_color
        self.setChecked(checked)
        self.setEnabled(enabled)
        self.setVisible(visible)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.set_style(stylesheet)
        self.stateChanged.connect(event_callback)

    def set_style(self, stylesheet: str | None):
        """
        Apply the provided stylesheet or the default checkbox style.

        Parameters
        ----------
        stylesheet : str, optional
            The stylesheet string to apply to the checkbox. If not provided,
            a default style based on the provided colors will be applied.
        """
        self.setStyleSheet(
            stylesheet
            if stylesheet is not None
            else InputStyles.checkbox_style(
                self.checkbox_color,
                self.checkbox_color_unchecked,
                self.label_color,
                self.border_color,
            )
        )


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
        checked: bool = False,
        enabled: bool = True,
        visible: bool = True,
        checkbox_color: str = "#1E90FF",
        checkbox_color_unchecked: str = "#6b6a6a",
        label_color: str = "#f8f8f8",
        border_color: str = "#252525",
        checkbox_stylesheet: Optional[str] = None,
        checkbox_wrapper_stylesheet: Optional[str] = None,
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.key = key
        self.label = label
        self.event_callback = event_callback
        self.checked = checked
        self.enabled = enabled
        self.visible = visible
        self.checkbox_color = checkbox_color
        self.checkbox_color_unchecked = checkbox_color_unchecked
        self.label_color = label_color
        self.border_color = border_color
        self.checkbox_stylesheet = checkbox_stylesheet
        self.checkbox_wrapper_stylesheet = checkbox_wrapper_stylesheet
        
        if self.checkbox_wrapper_stylesheet:
            self.setStyleSheet(self.checkbox_wrapper_stylesheet)

        self.checkbox = self._create_checkbox()

        row = QHBoxLayout()
        row.addWidget(self.checkbox)
        self.setLayout(row)

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
                self.checkbox_color, 
                self.checkbox_color_unchecked, 
                self.label_color
            )
        )
        return Checkbox(
            key=self.key,
            label=self.label,
            event_callback=self.event_callback,
            checked=self.checked,
            enabled=self.enabled,
            visible=self.visible,
            checkbox_color=self.checkbox_color,
            checkbox_color_unchecked=self.checkbox_color_unchecked,
            label_color=self.label_color,
            border_color=self.border_color,
            stylesheet=checkbox_stylesheet
        )

    def toggle_enable_state(self, state: bool):
        """
        Enable or disable the checkbox.

        Parameters
        ----------
        state : bool
            If True, enables the checkbox; if False, disables it.
        """
        self.checkbox.setEnabled(state)

    def toggle_visible_state(self, state: bool):
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