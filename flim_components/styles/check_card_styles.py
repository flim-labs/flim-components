class CheckCardStyles:
    
    @staticmethod
    def message_style(color: str, bg_color: str, border_color: str):
        return f"""
            QLabel {{
                color: {color}; 
                background-color: {bg_color};
                border-left: 1px solid {border_color}; 
                border-right: 1px solid {border_color}; 
                border-radius: 0; 
                padding: 0 4px;
                font-weight: 800;
                font-size: 14px;
            }}                
        """          