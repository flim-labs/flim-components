from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar,
    QApplication,
    QHBoxLayout,
)
from PyQt6.QtCore import pyqtSignal
from typing import Literal, Optional

from styles.progress_bar_styles import ProgressBarStyles


class ProgressBar(QWidget):
    """
    A customizable progress bar widget.

    Parameters
    ----------
    label_text : str | None
        The initial text for the label displayed above or beside the progress bar. If None, no label is displayed.
    color : str
        The color of the active portion of the progress bar (default is "#31c914").
    visible : bool
        Whether the progress bar is initially visible (default is True).
    enabled : bool
        Whether the progress bar is initially enabled (default is True).
    stylesheet : str | None
        Custom stylesheet for the progress bar (default is None). If provided, this will override the default styles.
    layout_type : Literal["horizontal", "vertical"]
        The orientation of the layout. If "horizontal", the label and progress bar are side-by-side. 
        If "vertical", the label is positioned above the progress bar (default is "vertical").
    spacing : int
        The spacing between the label and progress bar in pixels (default is 10). Only relevant if both label and progress bar are present.
    progress_bar_height : int | None
        The height of the progress bar in pixels (default is 15). If None, the default height is used.
    progress_bar_width : int | None
        The width of the progress bar in pixels. If None, the width adjusts to fit the content.
    indeterminate : bool
        Whether the progress bar is in indeterminate mode (default is False).
    parent : Optional[QWidget]
        The parent widget of this progress bar (default is None).
    """
    
    complete = pyqtSignal() 

    def __init__(
        self,
        label_text: str | None = None,
        color: str = "#31c914",
        visible: bool = True,
        enabled: bool = True,
        stylesheet: str | None = None,
        layout_type: Literal["horizontal", "vertical"] = "vertical",
        spacing: int = 10,
        progress_bar_height: int | None = 15,
        progress_bar_width: int | None = None,
        indeterminate: bool = False,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.color = color
        self.indeterminate = indeterminate

        # Initialize layout based on layout_type
        if layout_type == "horizontal":
            self.layout = QHBoxLayout()
        else:
            self.layout = QVBoxLayout()

        self.layout.setContentsMargins(0, 0, 0, 0)

        # Set the spacing between widgets in the layout if label_text is provided
        if label_text is not None:
            self.layout.setSpacing(spacing)

        # Create and configure the label if label_text is provided
        if label_text is not None:
            self.label = QLabel(label_text)

        # Create and configure the progress bar
        self.progress_bar = QProgressBar()
        if progress_bar_height is not None:
            self.progress_bar.setFixedHeight(progress_bar_height)
        if progress_bar_width is not None:
            self.progress_bar.setFixedWidth(progress_bar_width)

        # Add widgets to the layout
        if layout_type == "horizontal":
            self.layout.addWidget(self.progress_bar)
            if label_text is not None:
                self.layout.addWidget(self.label)
        else:
            if label_text is not None:
                self.layout.addWidget(self.label)
            self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)
        self.set_visible(visible)
        self.set_enabled(enabled)
        self.set_style(stylesheet)

        # Set the progress bar to indeterminate mode if specified
        if indeterminate:
            self.set_indeterminate_mode(True)

    def set_indeterminate_mode(self, state: bool) -> None:
        """
        Enable or disable the indeterminate mode of the progress bar.

        Parameters
        ----------
        state : bool
            If True, sets the progress bar to indeterminate mode; if False, switches to determinate mode.
        """
        if state:
            self.progress_bar.setRange(0, 0)  # Indeterminate mode
        else:
            self.progress_bar.setRange(0, 100)  # Switch back to determinate mode
        QApplication.processEvents()

    def update_progress(
        self, current_value: int, total_value: int, label_text: Optional[str] = None
    ) -> None:
        """
        Update the progress bar and label text based on the current and total values.

        Parameters
        ----------
        current_value : int
            The current progress value to be reflected on the progress bar.
        total_value : int
            The total value representing 100% progress.
        label_text : Optional[str], optional
            The text to display in the label. If provided, the label's text is updated; otherwise, the label text remains unchanged.
        """
        if not self.indeterminate:
            progress_value = (current_value / float(total_value)) * 100
            self.progress_bar.setValue(int(progress_value))
            if label_text:
                self.label.setText(label_text)
            
            # Emit signal if progress is complete
            if progress_value >= 100:
                self.complete.emit()            
            QApplication.processEvents()

    def clear_progress(self) -> None:
        """
        Clear the progress bar and reset it to zero. This also clears the label text.
        """
        if not self.indeterminate:
            self.progress_bar.setValue(0)
            self.label.clear()
            QApplication.processEvents()
        
    def get_value(self) -> int:
        """
        Retrieve the current value of the progress bar.

        Returns
        -------
        int
            The current value of the progress bar, representing the percentage of completion.
        """
        return self.progress_bar.value()        

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the progress bar and its label.

        Parameters
        ----------
        visible : bool
            If True, makes the progress bar and label visible; if False, hides them.
        """
        self.setVisible(visible)
        QApplication.processEvents()

    def set_enabled(self, state: bool) -> None:
        """
        Enable or disable the progress bar.

        Parameters
        ----------
        state : bool
            If True, enables the progress bar; if False, disables it.
        """
        self.progress_bar.setEnabled(state)
        QApplication.processEvents()

    def set_style(self, stylesheet: str | None) -> None:
        """
        Apply a custom stylesheet to the progress bar.

        Parameters
        ----------
        stylesheet : str | None
            A custom stylesheet to apply. If None, the default stylesheet is used.
        """
        self.setStyleSheet(
            stylesheet
            if stylesheet is not None
            else ProgressBarStyles.progress_bar_style(self.color)
        )