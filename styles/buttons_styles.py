def base_button_style(
    fg_color: str,
    bg_color_base: str,
    border_color: str,
    bg_color_hover: str,
    bg_color_pressed: str,
    bg_color_disabled: str,
    border_color_disabled: str,
    fg_color_disabled: str
):
    return f"""
        QPushButton {{
            background-color: {bg_color_base};
            border: 1px solid {border_color};
            font-family: "Montserrat";
            color: {fg_color};
            letter-spacing: 0.1em;
            padding: 8px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {bg_color_hover};
            border: 2px solid {bg_color_hover};
        }}
        QPushButton:focus {{
            background-color: {bg_color_pressed};
            border: 2px solid {bg_color_pressed};
        }}
        QPushButton:pressed {{
            background-color: {bg_color_pressed};
            border: 2px solid {bg_color_pressed};
        }}
        QPushButton:disabled {{
            background-color: {bg_color_disabled};
            border: 2px solid {border_color_disabled};
            color: {fg_color_disabled};
        }}
    """
