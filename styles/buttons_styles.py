class ButtonStyles:
    @staticmethod
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
        
    @staticmethod
    def toggle_button_style(
        fg_color: str,
        bg_color: str,
        is_first: bool = False,
        is_last: bool = False
    ) -> str:
        border_radius_styles = ""
        
        if is_first:
            border_radius_styles += """
            border-top-left-radius: 3px;
            border-bottom-left-radius: 3px;
            """
        if is_last:
            border_radius_styles += """
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
            """

        return f"""
        QPushButton {{
            font-family: "Montserrat";
            letter-spacing: 0.1em;
            padding: 10px 12px;
            font-size: 14px;
            font-weight: bold;
            min-width: 60px;
            color: {fg_color};
            background-color: {bg_color};
            {border_radius_styles}
        }}
        """
        

    @staticmethod            
    def collapse_button_style(
        bg_color: str,
        border_color: str,
        border_radius: str,
        icon_size: str 
    ):
        return f"""
            QPushButton{{
                background-color: {bg_color};
                border-radius: {border_radius};
                qproperty-iconSize: {icon_size};
                border: 1px solid {border_color};
            }}
        """           