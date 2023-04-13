from src.mylist import *

class MyListSub(MyList):
    def __init__(self, data = []) -> None:
        super().__init__(data)
        self.i = 0
        
    def __add__(self, otherList: MyList) -> MyList:
        self.i += 1
        print(f"Count calls: {self.i}")
        return super().__add__(otherList)