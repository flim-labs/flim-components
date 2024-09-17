import json
import os
import shutil
from typing import Any, Dict
from PyQt6.QtWidgets import QFileDialog


class FileUtils:
    """
    A utility class providing file-related (and Flim file-related) helper methods,
    such as selecting directories, comparing file timestamps and retrieving files.
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
    

    @staticmethod
    def get_recent_time_tagger_file(root_folder: str) -> str:
        """
        Retrieves the most recent Time Tagger file from the specified root folder.

        Parameters:
        - root_folder (str): The root directory containing the data.

        Returns:
        - str: The path to the most recent Time Tagger file.

        Raises:
        - FileNotFoundError: If no Time Tagger files are found.
        """        
        data_folder = os.path.join(root_folder, ".flim-labs", "data")
        files = [
            f
            for f in os.listdir(data_folder)
            if f.startswith("time_tagger_spectroscopy")
        ]
        if not files:
            raise FileNotFoundError("No Time Tagger files found.")        
        files.sort(
            key=lambda x: os.path.getmtime(os.path.join(data_folder, x)), reverse=True
        )
        return os.path.join(data_folder, files[0])  
    
    
    @staticmethod
    def copy_file(origin_file_path: str, save_name: str, save_dir: str) -> str:
        """
        Copy a file to a new directory with a modified name.

        This function takes the path of a file, appends a custom save name to the original file name, 
        and copies the file to the specified directory with the new name.

        Parameters
        ----------
        origin_file_path : str
            The path to the original file to be copied.
        save_name : str
            A string to be appended to the original file name before saving the copy.
        save_dir : str
            The directory where the copied file will be saved.

        Returns
        -------
        str
            The full path to the newly copied file.
        """
        origin_file_name = os.path.basename(origin_file_path)
        new_file_name = f"{save_name}_{origin_file_name}"
        new_file_path = os.path.join(save_dir, new_file_name)
        shutil.copyfile(origin_file_path, new_file_path)
        return new_file_path
        
        
    @staticmethod
    def extract_file_metadata(file_path: str, magic_number: bytes) -> Dict[str, Any]:
        """
        Extracts metadata from a .bin file given a specific magic number.

        This method reads the file specified by `file_path`, verifies that the first 4 bytes match the `magic_number`,
        reads the length of the metadata header, and then reads and parses the metadata header as JSON.

        Parameters
        ----------
        file_path : str
            The path to the file from which metadata will be extracted.
        magic_number : bytes
            A 4-byte magic number used to verify the file's format.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the metadata extracted from the file. The keys and values depend on the content of the JSON metadata.
        """
        with open(file_path, "rb") as f:
            assert f.read(4) == magic_number
            header_length = int.from_bytes(f.read(4), byteorder="little")
            header = f.read(header_length)
            metadata = json.loads(header)
        return metadata