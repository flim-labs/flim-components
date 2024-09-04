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

    @staticmethod
    def input_text_style():
        return f"""
           QLineEdit, QPlainTextEdit {{
                color: #f8f8f8;
                font-family: "Montserrat";
                font-size: 14px;
                padding: 8px;
                min-width: 60px;
                border: 1px solid #11468F;
                border-radius: 5px;
                background-color: transparent;
                color: #1E90FF;
            }}
            QLineEdit:disabled,QPlainTextEdit::disabled {{
            color: #404040;  
            border-color: "#3c3c3c";
            }}        
        """

    @staticmethod
    def input_select_style():
        return f"""
            QComboBox {{
                color: #f8f8f8;
                font-family: "Montserrat";
                font-size: 14px;
                padding: 8px;
                border: 1px solid #3b3b3b;
                border-radius: 5px;
                background-color: transparent;
            }}
            QComboBox:disabled {{
                color: darkgrey;  
                border-color: #3c3c3c;
            }} 
            QComboBox:on {{ 
                border-bottom-left-radius: 0;
                border-bottom-right-radius: 0;
            }}

           QComboBox QAbstractItemView {{
            font-family: "Montserrat";
            border: 1px solid #3b3b3b;
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            background-color: #181818;
            color: #f8f8f8;
            selection-background-color: #8d4ef2;
            }} 
        """


    @staticmethod
    def checkbox_style(checkbox_color_checked: str, checkbox_color_unchecked: str, label_color: str, border_color: str):
        return f"""
            QCheckBox {{
                spacing: 5px;
                color: {label_color};
                font-family: "Montserrat";
                font-size: 14px;
                letter-spacing: 0.1em;
                border: 1px solid {border_color};
                border-radius: 5px;
                padding: 10px;
            }}
            QCheckBox::indicator {{
                width: 20px;
                height: 20px;
                border-radius: 10px;  
            }}

            QCheckBox::indicator:unchecked {{
                background-color: {checkbox_color_unchecked};
            }}

            QCheckBox::indicator:checked {{
                background-color: {checkbox_color_checked};
            }}
        """
        
    @staticmethod            
    def wrapped_checkbox_style(checkbox_color_checked: str, checkbox_color_unchecked: str, label_color: str):
        return f"""
            QCheckBox {{
                spacing: 5px;
                color: {label_color};
                font-family: "Montserrat";
                font-size: 14px;
                letter-spacing: 0.1em;
                border-radius: 5px;
            }}
            QCheckBox::indicator {{
                width: 14px;
                height: 14px;
                border-radius: 7px;  
            }}

            QCheckBox::indicator:unchecked {{
                background-color: {checkbox_color_unchecked};
            }}

            QCheckBox::indicator:checked {{
                background-color: {checkbox_color_checked};
            }}
        """  
           