from typing import Literal, Optional

from components.inputs.switch import SwitchBox


class ExportDataSwitch(SwitchBox):
    """
    A specific Flim implementation of SwitchBox for export data toggle.
    All parameters are optional and default values are used if not provided.
    """

    def __init__(
        self,
        label: str = "Export data:",
        event_callback=None,
        layout_type: Literal["horizontal", "vertical"] = "horizontal",
        width: Optional[int] = 70,
        height: Optional[int] = 30,
        spacing: Optional[int] = 8,
        checked: bool = False,
        active_color="#11468F",
    ):
        # Initialize with optional parameters, using defaults if not provided
        super().__init__(
            label=label,
            layout_type=layout_type,
            event_callback=event_callback,
            width=width,
            height=height,
            spacing=spacing,
            checked=checked,
            active_color=active_color,
        )
