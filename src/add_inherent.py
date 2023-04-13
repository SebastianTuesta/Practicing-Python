from src.add import Adder

class ListAdder(Adder):
    def add(self, x: list, y: list) -> list:
        return x + y

class DictAdder(Adder):
    def add(self, x: dict, y: dict) -> dict:
        return {**x, **y}