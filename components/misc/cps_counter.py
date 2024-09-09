from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from typing import Dict, Optional
from components.animations.vibrant_animation import VibrantLabel
from layouts.compact_layout import CompactLayout
from styles.cps_counter_styles import CPSCounterStyles
from utils.data_converter import DataConverter


class CPSCounter(QWidget):
    """
    A widget to display CPS (Clicks Per Second) with optional vibrant animation
    when CPS exceeds a specified threshold.

    Parameters
    ----------
    label_text : str, optional
        The initial text displayed on the CPS label (default is "No CPS").
    cps_threshold_animation : bool, optional
        If True, enables vibrant animation when CPS exceeds the threshold (default is True).
    visible : bool, optional
        If True, makes the CPS counter visible; if False, hides it (default is True).
    label_stylesheet : str | None, optional
        A custom stylesheet for the CPS label. If None, the default stylesheet is used (default is None).
    animation_start_stylesheet : str | None, optional
        A custom stylesheet applied to the CPS label when the animation starts (default is None).
    animation_stop_stylesheet : str | None, optional
        A custom stylesheet applied to the CPS label when the animation stops (default is None).
    parent : Optional[QWidget], optional
        The parent widget for this CPSCounter (default is None).
    """

    def __init__(
        self,
        label_text: str = "No CPS",
        cps_threshold_animation: bool = True,
        visible: bool = True,
        label_stylesheet: str | None = None,
        animation_start_stylesheet: str | None = None,
        animation_stop_stylesheet: str | None = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self.layout = CompactLayout(QVBoxLayout())
        self.label_text = label_text
        self.cps_threshold_animation = cps_threshold_animation
        self.animation = None

        # CPS Label
        self.cps_label = QLabel(label_text)
        self.set_style(label_stylesheet)
        # Vibrant animation (CPS threshold warning)
        if cps_threshold_animation:
            self.animation = VibrantLabel(
                widget=self.cps_label,
                start_stylesheet=animation_start_stylesheet,
                stop_stylesheet=animation_stop_stylesheet,
            )
        # Add widget to layout
        self.layout.addWidget(self.cps_label)
        self.setLayout(self.layout)
        self.set_visible(visible)

    def update_cps_count(
        self,
        current_time_ns: int | float,
        last_time_ns: int | float,
        interval: int | float,
        cps_curr_count: int,
        cps_last_count: int,
        cps_threshold: int,
    ) -> None:
        """
        Update the CPS count based on the elapsed time and current CPS values.

        Parameters
        ----------
        current_time_ns : int | float
            The current time in nanoseconds.
        last_time_ns : int | float
            The time of the last CPS count in nanoseconds.
        interval : int | float
            The time interval to compute CPS, in nanoseconds.
        cps_curr_count : int
            The current CPS count.
        cps_last_count : int
            The CPS count at the last update.
        cps_threshold : int
            The CPS value threshold for triggering animation.
        """
        time_elapsed = current_time_ns - last_time_ns
        if time_elapsed > interval:
            cps_value = (cps_curr_count - cps_last_count) / (
                time_elapsed / 1_000_000_000
            )
            humanized_number = DataConverter.humanize_number(cps_value)
            self.cps_label.setText(f"{humanized_number} CPS")
            if cps_value > cps_threshold:
                self.start_animation()
            else:
                self.stop_animation()

    def start_animation(self) -> None:
        """
        Start the vibrant animation on the CPS label if enabled.
        """
        if self.animation is not None:
            self.animation.start()

    def stop_animation(self) -> None:
        """
        Stop the vibrant animation on the CPS label if enabled.
        """
        if self.animation is not None:
            self.animation.stop()

    @staticmethod
    def clear_all_animations(animations: Dict[int, VibrantLabel]) -> None:
        """
        Stop all animations in the provided dictionary of VibrantLabel animations.

        Parameters
        ----------
        animations : Dict[int, VibrantLabel]
            A dictionary where keys are identifiers and values are VibrantLabel animations to be stopped.
        """
        for _, animation in animations.items():
            if animation is not None and isinstance(animation, VibrantLabel):
                animation.stop()

    def set_visible(self, visible: bool) -> None:
        """
        Set the visibility of the CPS counter.

        Parameters
        ----------
        visible : bool
            If True, makes the CPS counter visible; if False, hides it.
        """
        self.setVisible(visible)
        QApplication.processEvents()

    def set_style(self, stylesheet: str | None) -> None:
        """
        Apply a custom stylesheet to the CPS counter label.

        Parameters
        ----------
        stylesheet : str | None
            A custom stylesheet to apply. If None, the default stylesheet is used.
        """
        self.setStyleSheet(
            stylesheet if stylesheet is not None else CPSCounterStyles.cps_label_style()
        )
