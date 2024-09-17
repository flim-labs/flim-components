from PyQt6.QtCore import QEasingCurve

from flim_components.components.inputs.switch import DualLabelSwitchBox
from flim_components.styles.inputs_styles import InputStyles

class LinLogSwitch(DualLabelSwitchBox):
    """
    A specific Flim implementation of DualLabelSwitchBox for LIN/LOG (linear/logarithmic) scale toggle.
    All parameters are optional and default values are used if not provided.
    """

    def __init__(
        self,
        event_callback=None,
        label_off="LOG",
        label_on="LIN",
        widget_rotation="vertical",
        bg_color="#777777",
        circle_color="#222222",
        active_color="#f72828",
        unchecked_color="#f72828",
        width=80,
        height=28,
        animation_curve: QEasingCurve.Type = QEasingCurve.Type.OutBounce,
        animation_duration: int = 300,
        checked=False,
        enabled=True,
        visible=True,
        change_cursor=True,
        labels_stylesheet=InputStyles.dual_labels_switch_style(),
    ):
        # Initialize with optional parameters, using defaults if not provided
        super().__init__(
            event_callback=event_callback,
            label_off=label_off,
            label_on=label_on,
            widget_rotation=widget_rotation,
            bg_color=bg_color,
            circle_color=circle_color,
            active_color=active_color,
            unchecked_color=unchecked_color,
            width=width,
            height=height,
            animation_curve=animation_curve,
            animation_duration=animation_duration,
            checked=checked,
            enabled=enabled,
            visible=visible,
            change_cursor=change_cursor,
            labels_stylesheet=labels_stylesheet,
        )
