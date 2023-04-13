"""_summary_

Returns:
    _type_: _description_
"""
from adder import adder


class ListAdder(adder.Adder):
    """_summary_

    Args:
        adder (_type_): _description_
    """
    def __add__(self, data: list) -> list:
        """_summary_

        Args:
            data (list): _description_

        Returns:
            list: _description_
        """
        return self.data + data

    def __str__(self) -> str:
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__class__.__name__
    