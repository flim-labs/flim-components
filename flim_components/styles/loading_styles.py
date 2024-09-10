from typing import Literal


class LoadingStyles:
    @staticmethod
    def loading_overlay_widget_style(
        background_color: str,
        border_color: str,
        border_position: Literal["top", "left", "bottom", "right"],
    ):
        if border_position not in {"top", "left", "bottom", "right"}:
            raise ValueError(
                "Invalid border position. Must be one of 'top', 'left', 'bottom', 'right'."
            )
        style = f"""
            QWidget#loading_widget {{
                border-{border_position}: 1px solid {border_color};
            }}
            QWidget{{
                background-color: {background_color};
            }}
        """
        return style
