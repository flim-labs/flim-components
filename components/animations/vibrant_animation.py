from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QAbstractAnimation
from PyQt6.QtWidgets import QLabel
from typing import Optional

from styles.animations_styles import AnimationsStyles

class VibrantLabel:
    """
    A class to create a vibrant animation effect on a QLabel widget.

    Parameters
    ----------
    widget : QLabel
        The QLabel widget to which the animation will be applied.
    start_stylesheet : str, optional
        The stylesheet to be applied to the widget at the start of the animation. 
        If not provided, a default stylesheet will be used (default is None).
    stop_stylesheet : str, optional
        The stylesheet to be applied to the widget at the end of the animation. 
        If not provided, a default stylesheet will be used (default is None).
    """

    def __init__(
        self,
        widget: QLabel,
        start_stylesheet: Optional[str] = None,
        stop_stylesheet: Optional[str] = None,
    ) -> None:
        """
        Initializes the VibrantLabel with the specified widget and stylesheets.

        Parameters
        ----------
        widget : QLabel
            The QLabel widget to which the animation will be applied.
        start_stylesheet : str, optional
            The stylesheet to be applied to the widget at the start of the animation. 
            If not provided, a default stylesheet will be used (default is None).
        stop_stylesheet : str, optional
            The stylesheet to be applied to the widget at the end of the animation. 
            If not provided, a default stylesheet will be used (default is None).
        """
        self.widget = widget
        self.start_stylesheet = start_stylesheet
        self.stop_stylesheet = stop_stylesheet
        self.animation = QPropertyAnimation(widget, b"pos")
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.animation.setLoopCount(-1)
        self.original_pos = widget.pos()

    def start(self, amplitude: int = 10, duration: int = 50) -> None:
        """
        Start the vibrant animation on the widget.

        Parameters
        ----------
        amplitude : int, optional
            The amplitude of the animation's movement in pixels (default is 10).
        duration : int, optional
            The duration of the animation in milliseconds (default is 50).
        """
        if self.animation.state() == QAbstractAnimation.State.Running:
            return

        self.original_pos = self.widget.pos()
        self._update_stylesheet(
            self.start_stylesheet
            if self.start_stylesheet is not None
            else AnimationsStyles.vibrant_label_start_style()
        )

        self.animation.setDuration(duration)
        self.animation.setStartValue(self.original_pos)
        self.animation.setKeyValueAt(
            0.5, QPoint(self.original_pos.x() + amplitude, self.original_pos.y())
        )
        self.animation.setEndValue(self.original_pos)
        self.animation.start()

    def stop(self) -> None:
        """
        Stop the vibrant animation and reset the widget's position and style.
        """
        if self.animation.state() == QAbstractAnimation.State.Running:
            self._update_stylesheet(
                self.stop_stylesheet
                if self.stop_stylesheet is not None
                else AnimationsStyles.vibrant_label_stop_style()
            )
            self.animation.stop()
            self.widget.move(self.original_pos)

    def _update_stylesheet(self, stylesheet: str) -> None:
        """
        Update the widget's stylesheet.

        Parameters
        ----------
        stylesheet : str, optional
            The stylesheet to be applied to the widget. 
        """
        self.widget.setStyleSheet(stylesheet)
