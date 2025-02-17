from language import Language


# Concrete Product A1
class English(Language):
    def greet(self) -> str:
        return "Hello!"
