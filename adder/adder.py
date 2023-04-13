"""Module that store Adder class

Raises:
    NotImplementedError: Template class
    NotImplementedError: Template class
"""
from abc import abstractmethod
from typing import Any


class Adder():
    """Abstract class to use as a template for add 2 objects

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """
        self.data = data

    @abstractmethod
    def __add__(self, data: Any) -> Any:
        """_summary_

        Args:
            y (Any): _description_

        Raises:
            NotImplementedError: _description_

        Returns:
            Any: _description_
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__class__.__name__
