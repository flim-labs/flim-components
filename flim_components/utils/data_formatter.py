import re
from typing import Callable, List, Tuple

from flim_components.utils.constants import UNICODE_SUP

class DataFormatter:
    @staticmethod
    def format_power_of_ten(i):
        return "0" if i < 0 else f"10{''.join(UNICODE_SUP[c] for c in str(i))}"    
    
    @staticmethod
    def extract_numbers_from_text(
        text: str,
        transform_func: Callable[[int], int] = lambda x: x
    ) -> List[int]:
        """
        Extracts numbers from a given text and applies a transformation function to each number.

        Parameters:
        ----------
        text : str
            The input text from which numbers are to be extracted.
        transform_func : Callable[[int], int], optional
            A function that takes an integer and returns a transformed integer. Default is the identity function (no transformation).

        Returns:
        -------
        List[int]
            A list of integers obtained by extracting and transforming the numbers from the text.
        """
        numbers = re.findall(r'\d+', text)  # Extract all numbers as strings
        transformed_numbers = [transform_func(int(num)) for num in numbers]
        return transformed_numbers    
    
    @staticmethod
    def extract_index_from_label(text: str) -> int:
        """
        Extracts a number from a label and adjusts it to a zero-based index.

        Parameters:
        ----------
        text : str
            The label text containing the number.

        Returns:
        -------
        int
            The zero-based index of the number extracted from the label.
        """
        numbers = DataFormatter.extract_numbers_from_text(text)
        if not numbers:
            raise ValueError("No number found in the text.")
        ch_num = numbers[0]
        return ch_num - 1
    
    @staticmethod
    def extract_index_pair_from_label(text: str) -> Tuple[int, ...]:
        """
        Extracts numbers pair from a label and adjusts them to zero-based indices.

        Parameters:
        ----------
        text : str
            The label text containing the numbers pair.

        Returns:
        -------
        Tuple[int, ...]
            A tuple of zero-based indices of the numbers pair extracted from the label.
        """
        numbers = DataFormatter.extract_numbers_from_text(text, transform_func=lambda x: x - 1)
        return tuple(numbers)    