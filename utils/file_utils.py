import os
from PyQt6.QtWidgets import QFileDialog


class FileUtils:
    """
    A utility class providing file-related (and Flim file-related) helper methods,
    such as selecting directories, comparing file timestamps,
    and retrieving recent files based on modification times.
    """

    @staticmethod
    def directory_selector(window) -> str:
        """
        Opens a dialog to select a directory.

        Parameters:
        - window (QWidget): The parent window for the QFileDialog.

        Returns:
        - str: The selected directory path, or an empty string if no directory is selected.
        """
        folder_path = QFileDialog.getExistingDirectory(window, "Select Directory")
        return folder_path

    @staticmethod
    def compare_file_timestamps(file_path1, file_path2) -> float:
        """
        Compares the creation timestamps of two files.

        Parameters:
        - file_path1 (str): Path to the first file.
        - file_path2 (str): Path to the second file.

        Returns:
        - float: The absolute difference between the two file creation times, in seconds.
        """
        ctime1 = os.path.getctime(file_path1)
        ctime2 = os.path.getctime(file_path2)
        time_diff = abs(ctime1 - ctime2)
        return time_diff

    @staticmethod
    def get_recent_spectroscopy_file(root_folder: str) -> str:
        """
        Retrieves the most recent spectroscopy data file from the
        specified root folder.

        Parameters:
        - root_folder (str): The root directory containing the data.

        Returns:
        - str: The path to the most recent spectroscopy file.

        Raises:
        - FileNotFoundError: If no spectroscopy files are found.
        """
        data_folder = os.path.join(root_folder, ".flim-labs", "data")
        files = [
            f
            for f in os.listdir(data_folder)
            if f.startswith("spectroscopy")
            and not ("calibration" in f)
            and not ("phasors" in f)
        ]
        if not files:
            raise FileNotFoundError("No spectroscopy files found.")
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return os.path.join(data_folder, files[0])

    @staticmethod
    def get_recent_phasors_file(root_folder: str) -> str:
        """
        Retrieves the most recent spectroscopy-phasors file
        from the specified root folder.

        Parameters:
        - root_folder (str): The root directory containing the data.

        Returns:
        - str: The path to the most recent phasors file.

        Raises:
        - FileNotFoundError: If no phasors files are found.
        """
        data_folder = os.path.join(root_folder, ".flim-labs", "data")
        files = [
            f
            for f in os.listdir(data_folder)
            if f.startswith("spectroscopy-phasors") and not ("calibration" in f)
        ]
        if not files:
            raise FileNotFoundError("No suitable phasors file found.")
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return os.path.join(data_folder, files[0])

    @staticmethod
    def get_recent_intensity_tracing_file(root_folder: str) -> str:
        """
        Retrieves the most recent intensity tracing file from the
        specified root folder.

        Parameters:
        - root_folder (str): The root directory containing the data.

        Returns:
        - str: The path to the most recent intensity tracing file.

        Raises:
        - FileNotFoundError: If no intensity tracing files are found.
        """
        data_folder = os.path.join(root_folder, ".flim-labs", "data")
        files = [
            f for f in os.listdir(data_folder) if f.startswith("intensity-tracing")
        ]
        if not files:
            raise FileNotFoundError("No intensity tracing files found.")
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return os.path.join(data_folder, files[0])

    @staticmethod
    def get_recent_n_intensity_tracing_files(num: int, root_folder: str) -> str:
        """
        Retrieves the most recent 'n' intensity tracing files from
        the specified root folder.

        Parameters:
        - num (int): The number of recent files to retrieve.
        - root_folder (str): The root directory containing the data.

        Returns:
        - List[str]: A list of paths to the 'n' most recent intensity tracing files.
        """
        data_folder = os.path.join(root_folder, ".flim-labs", "data", "fcs-intensity")
        files = [
            f for f in os.listdir(data_folder) if f.startswith("intensity-tracing")
        ]
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return [os.path.join(data_folder, f) for f in files[:num]]

    @staticmethod
    def get_recent_fcs_file(root_folder: str) -> str:
        """
        Retrieves the most recent FCS (Fluorescence Correlation Spectroscopy)
        file from the specified root folder.

        Parameters:
        - root_folder (str): The root directory containing the data.

        Returns:
        - str: The path to the most recent FCS file.

        Raises:
        - FileNotFoundError: If no FCS files are found.
        """
        data_folder = os.path.join(root_folder, ".flim-labs", "data")
        files = [
            f
            for f in os.listdir(data_folder)
            if f.startswith("fcs") and not ("calc" in f) and not ("intensity" in f)
        ]
        if not files:
            raise FileNotFoundError("No FCS files found.")
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return os.path.join(data_folder, files[0])
