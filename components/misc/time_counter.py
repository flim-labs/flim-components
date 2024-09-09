from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
)
from PyQt6.QtCore import pyqtSignal
from typing import Literal, Optional
from styles.time_counter_styles import TimeCounterStyles
from utils.data_converter import DataConverter


class TimeCounter(QLabel):
    """
    A customizable time counter widget that supports both countdown and countup modes, 
    with input and output units for time conversion.

    Parameters
    ----------
    input_unit : Literal["ns", "us", "ms", "s"]
        The unit of the input time value. Can be "ns" (nanoseconds), "us" (microseconds), 
        "ms" (milliseconds), or "s" (seconds). Default is "ns".
    output_unit : Literal["ns", "us", "ms", "s", "m"]
        The unit of the output time value displayed in the label. Can be "ns" (nanoseconds), 
        "us" (microseconds), "ms" (milliseconds), "s" (seconds), or "m" (minutes). Default is "s".
    counter_type : Literal["countdown", "countup"]
        The type of counter. "countdown" will count down from `end_time` to zero, 
        and "countup" will count up from `start_time`. Default is "countdown".
    start_time : int | float | None
        The start time for the countup timer, in the `input_unit`. Must be set if `counter_type` 
        is "countup". Default is None.
    end_time : int | float | None
        The end time for the countdown timer, in the `input_unit`. Must be set if `counter_type` 
        is "countdown". Default is 10.
    label_text : str | None
        The text to display before the time value in the label. Default is "Remaining time: ".
    color : str
        The color of the label text. Default is "#31c914".
    font_size : str
        The font size of the label text. Default is "18px".
    visible : bool
        Whether the time counter is initially visible. Default is True.
    stylesheet : str | None
        A custom stylesheet for the label. If None, the default styles are used. Default is None.
    parent : Optional[QWidget]
        The parent widget of the time counter. Default is None.

    Signals
    -------
    complete
        Emitted when the countdown reaches zero.

    Methods
    -------
    update_count(value)
        Updates the time value on the label based on the input time and conversions.
    set_visible(visible)
        Sets the visibility of the time counter.
    set_style(stylesheet)
        Applies a custom stylesheet to the time counter.
    """

    complete = pyqtSignal()

    def __init__(
        self,
        input_unit: Literal["ns", "us", "ms", "s"] = "ns",
        output_unit: Literal["ns", "us", "ms", "s", "m"] = "s",
        counter_type: Literal["countdown", "countup"] = "countdown",
        start_time: int | float | None = None,
        end_time: int | float | None = 10,
        label_text: str | None = "Remaining time:",
        color: str = "#31c914",
        font_size: str = "18px",
        visible: bool = True,
        stylesheet: str | None = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.color = color
        self.font_size = font_size
        self.input_unit = input_unit
        self.output_unit = output_unit
        self.counter_type = counter_type
        self.start_time = start_time
        self.end_time = end_time
        self.label_text = label_text
        self.setContentsMargins(0,0,0,0)
        self.set_visible(visible)
        self.set_style(stylesheet)

    def update_count(self, value: int | float) -> None:
        """
        Updates the time value displayed in the label. Converts the input time 
        to the appropriate output unit and formats it accordingly.

        Parameters
        ----------
        value : int | float
            The current time value to be converted and displayed. The input value is expected to be 
            in the unit specified by `input_unit`.
        """
        # Convert the input value to seconds first (as reference unit)
        current_value_in_seconds = DataConverter.convert_time(value, self.input_unit, "s")

        if self.counter_type == "countdown":
            if self.end_time is None:
                raise ValueError("end_time must be set for countdown")
            # Calculate remaining time
            end_time_in_seconds = DataConverter.convert_time(self.end_time, self.input_unit, "s")
            remaining_time = end_time_in_seconds - current_value_in_seconds
            if remaining_time <= 0:
                remaining_time = 0
                self.complete.emit()
        else:  # countup
            if self.start_time is None:
                raise ValueError("start_time must be set for countup")
            # Calculate elapsed time
            start_time_in_seconds = DataConverter.convert_time(self.start_time, self.input_unit, "s")
            remaining_time = current_value_in_seconds - start_time_in_seconds

        # Convert remaining or elapsed time to output unit
        remaining_time_in_output = DataConverter.convert_time(remaining_time, "s", self.output_unit)

        # Format and set the label text
        if self.output_unit == "s":
            minutes, seconds = divmod(remaining_time_in_output, 60)
            milliseconds = (remaining_time_in_output * 1000) % 1000
            time_text = f"{int(seconds):02}:{int(milliseconds):02} (s)"
        elif self.output_unit == "m":
            hours, minutes = divmod(remaining_time_in_output / 60, 60)
            time_text = f"{int(hours):02}:{int(minutes):02} (m)"
        elif self.output_unit == "ms":
            seconds, milliseconds = divmod(remaining_time_in_output, 1000)
            time_text = f"{int(seconds):02}:{int(milliseconds):03} (ms)"
        elif self.output_unit == "us":
            seconds, microseconds = divmod(remaining_time_in_output, 1e6)
            time_text = f"{int(seconds):02}:{int(microseconds):06} (us)"
        elif self.output_unit == "ns":
            seconds, nanoseconds = divmod(remaining_time_in_output, 1e9)
            time_text = f"{int(seconds):02}:{int(nanoseconds):09} (ns)"

        # Update the label
        self.setText(f"{self.label_text}{time_text}")
        
        QApplication.processEvents()

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the time counter.

        Parameters
        ----------
        visible : bool
            If True, makes the time counter visible; if False, hides it.
        """
        self.setVisible(visible)
        QApplication.processEvents()

    def set_style(self, stylesheet: str | None) -> None:
        """
        Apply a custom stylesheet to the time counter.

        Parameters
        ----------
        stylesheet : str | None
            A custom stylesheet to apply. If None, the default stylesheet is used.
        """
        self.setStyleSheet(
            stylesheet
            if stylesheet is not None
            else TimeCounterStyles.time_counter_style(self.color, self.font_size)
        )