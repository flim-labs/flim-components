class InputStyles:
    
    @staticmethod
    def input_number_style():
        return f"""
            QDoubleSpinBox, QSpinBox {{
                color: #f8f8f8;
                font-family: "Montserrat";
                font-size: 14px;
                padding: 8px;
                min-width: 60px;
                border: 1px solid #3b3b3b;
                border-radius: 5px;
                background-color: transparent;
            }}
            QDoubleSpinBox:disabled, QSpinBox:disabled {{
            color: #404040;  
            border-color: #3c3c3c;
            }}        
        """
