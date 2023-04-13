"""_summary_

Returns:
    _type_: _description_
"""
from adder import adder


class DictAdder(adder.Adder):
    """_summary_

    Args:
        Adder (_type_): _description_
    """
    def __add__(self, data: dict) -> dict:
        """_summary_

        Args:
            data (dict): _description_

        Returns:
            dict: _description_
        """
        return {**self.data, **data}

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__class__.__name__
    