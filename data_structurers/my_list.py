"""_summary_

Returns:
    _type_: _description_
"""
from typing import Union


class MyList():
    """_summary_
    """

    def __init__(self, data: Union[list, any]):
        """_summary_

        Args:
            data (list): _description_
        """
        if isinstance(data, list):
            self._data = data.copy()
            self._i = 0
        else:
            self._data = list(*data)

    @property
    def data(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._data

    def __add__(self, data: Union[list, 'MyList']) -> 'MyList':
        """_summary_

        Args:
            data (list): _description_

        Returns:
            list: _description_
        """

        if isinstance(data, list):
            return MyList(self.data + data)
        return self + data

    def __mul__(self, data: Union[list, 'MyList']) -> 'MyList':
        """_summary_

        Args:
            data (list): _description_

        Returns:
            list: _description_
        """

        if isinstance(data, list):
            return MyList(self.data * data)
        return self * data

    def __getitem__(self, key: int) -> any:
        """_summary_

        Args:
            key (int): _description_

        Returns:
            any: _description_
        """
        return self._data[key]

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._data.__str__()

    def __len__(self):
        return len(self._data)

    def next(self):
        """_summary_

        Raises:
            StopIteration: _description_

        Returns:
            _type_: _description_
        """
        if self._i == len(self._data):
            return
        value = self._data[self._i]
        self._i += 1
        yield value

    def append(self, item: any) -> None:
        """_summary_

        Args:
            item (any): _description_
        """
        self._data.append(item)

    def sort(self) -> None:
        """_summary_
        """
        self._data.sort()
