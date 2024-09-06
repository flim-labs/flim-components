import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from components.inputs.flim.acquisition_time_input import AcquisitionTimeInput
from components.inputs.flim.acquisitions_averages_input import AcquisitionsAveragesSelector
from components.inputs.flim.bin_width_input import BinWidthInput
from components.inputs.flim.calibration_type_input import CalibrationTypeSelector
from components.inputs.flim.connection_type_input import ConnectionTypeSelector
from components.inputs.flim.cps_threshold_input import CPSThresholdInput
from components.inputs.flim.harmonic_input import HarmonicSelector
from components.inputs.flim.phasors_resolution_input import PhasorsResolutionSelector
from components.inputs.flim.tau_input import TauInput
from components.inputs.flim.time_span_input import TimeSpanInput
from components.inputs.flim.acquisition_mode_input import AcquisitionModeSwitch
from components.inputs.flim.export_data_input import ExportDataSwitch
from components.inputs.flim.quantize_input import QuantizeSwitch
from components.inputs.flim.time_shift_input import TimeShiftInput
from components.inputs.slider import SliderWithInputFactory


class FlimInputsExampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Flim Inputs Example")
        self.setStyleSheet("background-color: #121212; color: white;")  
        
        # Acquisition time input
        self.acquisition_time = AcquisitionTimeInput(event_callback=self.on_acquisition_time_changed)
        # Acquisitions Averages input
        self.acquisitions_averages = AcquisitionsAveragesSelector(event_callback=self.on_averages_changed)
        # Bin width input
        self.bin_width = BinWidthInput(event_callback=self.on_bin_width_changed)
        # Calibration type input
        self.calibration_type = CalibrationTypeSelector(event_callback=self.on_calibration_type_changed)
        # Connection type input
        self.connection_type = ConnectionTypeSelector(event_callback=self.on_connection_type_changed)
        # CPS threshold input
        self.cps_threshold = CPSThresholdInput(event_callback=self.on_cps_threshold_changed)
        # Harmonics input
        self.harmonics = HarmonicSelector(event_callback=self.on_harmonic_changed)
        # Phasors resolution input
        self.phasors_resolution = PhasorsResolutionSelector(event_callback=self.on_phasors_resolution_changed)
        # Tau input
        self.tau = TauInput(event_callback=self.on_tau_changed)
        # Time span input
        self.time_span = TimeSpanInput(event_callback=self.on_time_shift_changed)
        # Time shift input
        self.time_shift = TimeShiftInput(event_callback=self.on_time_span_changed, layout_type="vertical")        
        # Acquisition mode input
        self.acquisition_mode = AcquisitionModeSwitch(event_callback=self.on_acquisition_mode_changed)
        # Export data input
        self.export_data = ExportDataSwitch(event_callback=self.on_export_data_changed, layout_type="vertical")
        # Quantize input
        self.quantize_input = QuantizeSwitch(event_callback=self.on_quantize_changed)
        # Time shift binded slider
        self.time_shift_slider = SliderWithInputFactory.create_slider_with_input(
            input_params={
                "event_callback": self.on_time_shift_slider_value_changed,
            },
            slider_params={"event_callback": self.on_time_shift_slider_value_changed},
            layout_type="horizontal",
            input_position="right",
            spacing=20,
        )

        layout = QGridLayout()

        layout.addWidget(self.acquisition_time, 0, 0)
        layout.addWidget(self.acquisitions_averages, 0, 1)
        layout.addWidget(self.bin_width, 0, 2)
        layout.addWidget(self.calibration_type, 0, 3)
        
        layout.addWidget(self.connection_type, 1, 0)
        layout.addWidget(self.cps_threshold, 1, 1)
        layout.addWidget(self.harmonics, 1, 2)
        layout.addWidget(self.phasors_resolution, 1, 3)
        
        layout.addWidget(self.tau, 2, 0)
        layout.addWidget(self.time_shift, 2, 1)
        layout.addWidget(self.time_span, 2, 2)
        layout.addWidget(self.acquisition_mode, 2, 3)
        
        layout.addWidget(self.export_data, 3, 0) 
        layout.addWidget(self.quantize_input, 3, 1)
        layout.addWidget(self.time_shift_slider, 3, 2)

        self.setLayout(layout)
        
        
    def on_acquisition_time_changed(self, value: int):
        print(f"Acquisition time set to: {value}")    
        
    def on_averages_changed(self, value: int):
        print(f"Acquisitions averages set to: {self.acquisitions_averages.get_selected_text()}")   
        
    def on_bin_width_changed(self, value: int):
        print(f"Bin width set to: {value}")      
        
    def on_calibration_type_changed(self, value: int):
        print(f"Calibration type set to: {self.calibration_type.get_selected_text()}")             
        
    def on_connection_type_changed(self, value: int):
        print(f"Connection type set to: {self.connection_type.get_selected_text()}")         
        
    def on_cps_threshold_changed(self, value: int):
        print(f"CPS threshold set to: {value}")     
        
    def on_harmonic_changed(self, value: int):
        print(f"Harmonic set to: {self.harmonics.get_selected_text()}")        
        
    def on_phasors_resolution_changed(self, value: int):
        print(f"Phasors resolution set to: {self.phasors_resolution.get_selected_text()}")    
        
    def on_tau_changed(self, value: float):
        print(f"Tau set to: {value}")   
        
    def on_time_span_changed(self, value: int):
        print(f"Time span set to: {value}")         
        
    def on_time_shift_changed(self, value: int):
        print(f"Time shift set to: {value}")                     
        
    def on_acquisition_mode_changed(self, state: bool):
        print(f"Free running mode set to: {state}")                                         
                                   
    def on_export_data_changed(self, state: bool):
        print(f"Export data set to: {state}")        
        
    def on_quantize_changed(self, state: bool):
        print(f"Quantize set to: {state}")   
                                                  
    def on_time_shift_slider_value_changed (self, value: int):
        print(f"Time shift slider set to: {value}")                               


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlimInputsExampleWindow()
    window.show()
    app.exec()
