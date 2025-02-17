from abc import abstractmethod, ABC


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        print(f"printing {document}")

    def fax(self, document):
        print(f"faxing {document}")

    def scan(self, document):
        print(f"scanning {document}")


# BAD Design, forced to implement Machine functions (fax, scan)
class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f"printing {document}")

    def fax(self, document):
        print("I am old, I don't know how to fax")

    def scan(self, document):
        print("I am old, I don't know how to scan")


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print(f"scanning {document}")


# Instead of Machine Abstract Class
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)