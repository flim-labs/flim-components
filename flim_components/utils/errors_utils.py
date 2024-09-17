from typing import List

from flim_components.components.popups.box_message import WarningMessage


class SpectroscopyExperimentErrors:
    """
    This class handles error checking for spectroscopy experiments.
    
    The static method `throw_error` validates three key parameters:
    1. `bin_width`: Ensures the bin width is not less than 1000μs.
    2. `frequency_mhz`: Checks that the frequency is not zero.
    3. `selected_channels`: Verifies that at least one channel is selected.
    
    If any of these conditions fail, a warning message is displayed and the method returns `True`, 
    indicating an error has occurred. If no errors are found, it returns `False`.
    """    
    @staticmethod
    def throw_error(
        bin_width: int, frequency_mhz: float, selected_channels: List[int]
    ) -> bool:
        """
        Check for errors in spectroscopy experiment parameters.

        Parameters:
        - bin_width (int): The width of the bin in microseconds. Must be >= 1000μs.
        - frequency_mhz (float): The frequency in MHz. Must be greater than 0.
        - selected_channels (List[int]): The list of selected channels. At least one channel must be selected.

        Returns:
        - bool: True if an error is found, False otherwise.
        """        
        bin_width_error = bin_width < 1000
        frequency_mhz_error = frequency_mhz == 0.0
        selected_channels_error = len(selected_channels) == 0
        has_error = bin_width_error or frequency_mhz_error or selected_channels_error
        # Bin width error message
        if bin_width_error:
            WarningMessage.show("Error", "Bin width value cannot be less than 1000μs")
            return has_error
        # Frequency mhz error message
        if frequency_mhz_error:
            WarningMessage.show("Error", "Frequency not detected")
            return has_error
        # Selected channels error message
        if selected_channels_error:
            WarningMessage.show("Error", "No channels selected")
            return has_error
        return has_error


class PhasorExperimentErrors:
    """
    This class handles error checking for phasor experiments.
    
    The static method `throw_error` checks whether a reference file is selected. 
    If the file is not selected, it displays a warning message and returns `True`.
    Otherwise, it returns `False`.
    """    
    @staticmethod
    def throw_error(
        reference_file: str | None,
    ) -> bool:
        """
        Check if a reference file is provided for the phasor experiment.

        Parameters:
        - reference_file (str | None): The path to the reference file. Must not be None.

        Returns:
        - bool: True if no reference file is provided, False otherwise.
        """        
        reference_file_error = not reference_file
        has_error = reference_file_error
        # Reference file error
        if reference_file_error:
            WarningMessage.show("Error", "No reference file selected")
            return has_error
        return has_error


class PhasorReferenceFileErrors:
    """
    This class handles error checking for the phasor reference file.
    
    The static method `throw_error` validates that the reference file contains:
    - A list of channels that matches the selected channels.
    - Harmonic data.
    - Curve data matching the selected channels.
    - Laser period and tau values.
    
    If any of these fields are missing or inconsistent, it displays an appropriate
    warning message and returns `True`. Otherwise, it returns `False`.
    """    
    @staticmethod
    def throw_error(reference_data: any, selected_channels: List[int]) -> bool:
        """
        Validate the contents of the phasor reference file.

        Parameters:
        - reference_data (any): The data from the reference file. Must include 'channels', 'harmonics', 'curves', 'laser_period_ns', and 'tau_ns'.
        - selected_channels (List[int]): The list of selected channels for the experiment.

        Returns:
        - bool: True if an error is found in the reference file, False otherwise.
        """        
        channels_error = "channels" not in reference_data
        channels_mismatch_error = len(reference_data["channels"]) != len(
            selected_channels
        )
        harmonics_error = "harmonics" not in reference_data
        curves_error = "curves" not in reference_data
        curves_mismatch_error = len(reference_data["curves"]) != len(selected_channels)
        laser_period_error = "laser_period_ns" not in reference_data
        tau_error = "tau_ns" not in reference_data
        has_error = (
            channels_error
            or channels_mismatch_error
            or harmonics_error
            or curves_error
            or curves_mismatch_error
            or laser_period_error
            or tau_error
        )
        # Channels error
        if channels_error:
            WarningMessage.show("Error", "Invalid reference file (missing channels)") 
            return has_error
        # Channels mismatch error
        if channels_mismatch_error:
            WarningMessage.show("Error", "Invalid reference file (channels mismatch)")
            return has_error
        # Harmonics error
        if harmonics_error:
            WarningMessage.show("Error", "Invalid reference file (missing harmonics)")    
            return has_error                         
        # Curves error
        if curves_error:
            WarningMessage.show("Error", "Invalid reference file (missing curves)")
            return has_error 
        # Laser period error
        if laser_period_error:
            WarningMessage.show("Error", "Invalid reference file (missing laser period)")  
            return has_error   
        # Tau error
        if tau_error:
            WarningMessage.show("Error", "Invalid reference file (missing tau)")  
            return has_error                                             
        return has_error
