from abc import ABC, abstractmethod
from typing import Union


class Adder(ABC):

    @abstractmethod
    def add(self, x: Union[list, dict], y: Union[list, dict]) -> Union[list, dict]:
        raise NotImplementedError("Subclasses should implement this!")

    def __add__(self, other: "Adder") -> Union[list, dict]:
        # check allowed type
        if type(self) == type(other):
            return self.add(self.data, other.data)
        else:
            raise TypeError("Must be the same class type.")