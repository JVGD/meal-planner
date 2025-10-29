from datetime import datetime


class Greeter:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}!, today is {datetime.now().strftime('%Y-%m-%d')}."
