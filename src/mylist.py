from typing import Optional, Any, List, Union
from src.add_inherent import ListAdder


class MyList:
    
    def __init__(self, data = []) -> None:
        self.data = data

        self.current = 0
        self.high = 0

    # indexing / slicing
    def __getitem__(self, key: Union[int, slice]) -> Union[int, "MyList"]:
        if type(key) == int:
            return self.data[key]
        elif type(key) == slice:
            return MyList(self.data[key])
        else:
            raise TypeError("Only int and slice type are allowed.")

    # append
    def append(self, *aditionals: Any) -> List[Any]:
        self.high += len(aditionals)
        self.data.extend(aditionals)

    # sort
    def sort(self):
        self.data.sort()

    # iter
    def __iter__(self):
        return self

    def __next__(self) -> Any:
        if self.current > self.high:
            self.current = 0
            raise StopIteration
        else:
            self.current += 1
            return self.data[self.current-1]

    def __add__(self, other_list: "MyList") -> Any:
        if type(other_list) == MyList:
            return MyList(ListAdder().add(self.data, other_list.data))
        elif type(other_list) == list:
            return MyList(ListAdder().add(self.data, other_list))
        else:
            raise TypeError("Only list and MyList type are allowed.")