import json
from typing import Any, Callable, Optional, Tuple
from PyQt6.QtWidgets import QFileDialog

from flim_components.components.popups.box_message import WarningMessage


class ReadFilesUtils:
    @staticmethod
    def read_json(
        window: Any, file_type: str, filter_string: str | None = None
    ) -> Tuple[Optional[str], Optional[dict]]:
        """
        Opens a file dialog to select a JSON file, then reads and parses its content.

        Parameters
        ----------
        window : Any
            The parent window for the QFileDialog.
        file_type : str
            A string representing the type of file to read (e.g. "Spectroscopy metadata")
        filter_string: str | None, optional
            The string which should be use to filter files (default is None).

        Returns
        -------
        Tuple[Optional[str], Optional[dict]]
            A tuple containing the file path and the parsed JSON data. Returns (None, None)
            if the file is invalid or an error occurs.
        """
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        if filter_string:
            filter_pattern = f"JSON files (*{filter_string}*.json)"
        else:
            filter_pattern = "JSON files (*.json)"
        dialog.setNameFilter(filter_pattern)
        file_name, _ = dialog.getOpenFileName(
            window,
            f"Load {file_type} file",
            "",
            filter_pattern,
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not file_name:
            return None, None
        if file_name is not None and not file_name.endswith(".json"):
            WarningMessage.show(
                "Invalid extension", "Invalid extension. File should be a .json"
            )
            return None, None
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                return file_name, data
        except json.JSONDecodeError:
            WarningMessage.show(
                "Invalid JSON", "The file could not be parsed as valid JSON."
            )
            return None, None
        except Exception as e:
            WarningMessage.show(
                "Error reading file", f"Error reading {file_type} file: {str(e)}"
            )
            return None, None

    @staticmethod
    def read_bin(
        window: Any,
        magic_bytes: Optional[bytes],
        file_type: str,
        read_data_cb: Callable[..., Any],
        filter_string: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> Optional[Any]:
        """
        Opens a file dialog to read a .bin file, verifies the magic bytes, and calls
        the provided callback function to process the file data.

        Parameters
        ----------
        window : Any
            The parent window for the QFileDialog.
        magic_bytes : Optional[bytes]
            The expected magic bytes for file validation. Pass None to skip validation.
        file_type : str
            A string representing the file type (e.g. "Spectroscopy").
        filter_string: str | None, optional
            The string which should be use to filter files (default is None).
        read_data_cb : Callable[..., Any]
            The callback function to process the file data. This function must accept
            a file object and any other required arguments passed via *args and **kwargs.
        *args : Any
            Additional positional arguments to be passed to the callback.
        **kwargs : Any
            Additional keyword arguments to be passed to the callback.

        Returns
        -------
        Optional[Any]
            The result of the callback function, or None if the file is invalid or an error occurs.
        """
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        if filter_string:
            filter_pattern = f"Bin files (*{filter_string}*.bin)"
        else:
            filter_pattern = "Bin files (*.bin)"
        dialog.setNameFilter(filter_pattern)
        file_name, _ = dialog.getOpenFileName(
            window,
            f"Load {file_type} file",
            "",
            filter_pattern,
            options=QFileDialog.Option.DontUseNativeDialog,
        )
        if not file_name:
            return None
        if file_name is not None and not file_name.endswith(".bin"):
            WarningMessage.show(
                "Invalid extension", "Invalid extension. File should be a .bin"
            )
            return None
        try:
            with open(file_name, "rb") as f:
                if magic_bytes is not None and f.read(4) != magic_bytes:
                    WarningMessage.show(
                        "Invalid file",
                        f"Invalid file. The file is not a valid {file_type} file.",
                    )
                    return None

                # Call the callback function with the file object and additional args/kwargs
                return read_data_cb(f, file_name, *args, **kwargs)

        except Exception as e:
            WarningMessage.show(
                "Error reading file", f"Error reading {file_type} file: {str(e)}"
            )
            return None
