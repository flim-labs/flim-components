from typing import Optional

from components.inputs.switch import SwitchBox


class QuantizeSwitch(SwitchBox):
    """
    A specific Flim implementation of SwitchBox for quantize toggle.
    All parameters are optional and default values are used if not provided.
    """

    def __init__(
        self,
        label: str = "Quantize Phasors:",
        layout_type: str = "vertical",
        width: Optional[int] = 80,
        height: Optional[int] = 28,
        spacing: Optional[int] = 8,
        checked: bool = False,
        active_color="#11468F",
    ):
        # Initialize with optional parameters, using defaults if not provided
        super().__init__(
            label=label,
            layout_type=layout_type,
            width=width,
            height=height,
            spacing=spacing,
            checked=checked,
            active_color=active_color,
        )
