from typing import Literal


class CPSCounterStyles:
    @staticmethod
    def cps_label_style():
        return """
            QLabel{
                font-weight: 700;
                font-family: "Montserrat";
                font-size: 30px;
                color: #FB8C00;
            }
        """

    @staticmethod
    def channel_cps_container_style(background_color: str, border_color: str):
        return f"""
            QWidget#container{{
                padding: 12px;
                border: 1px solid {border_color};
                margin-right: 8px;
                margin-left: 8px;
            }}
            QWidget {{
                background-color: {background_color};   
            }}
        """
        
    @staticmethod
    def channel_cps_label_style(layout: Literal["horizontal", "vertical"]):
        return f"""
            QLabel{{
                color: #cecece;
                margin-left: 8px;
                font-weight: 700;
                font-size: 20px;
            }}    
        """        
