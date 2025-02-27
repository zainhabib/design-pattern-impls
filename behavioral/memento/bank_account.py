from typing import Optional


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes: list[Memento] = [Memento(self.balance)]
        self.current: int = 0

    def deposit(self, amount) -> Memento:
        self.balance += amount
        m: Memento = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def withdraw(self, amount) -> Memento:
        self.balance -= amount
        m: Memento = Memento(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento: Memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self) -> Optional[Memento]:
        if self.current > 0:
            self.current -= 1
            m: Memento = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self) -> Optional[Memento]:
        if self.current + 1 < len(self.changes):
            self.current += 1
            m: Memento = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == '__main__':
    ba0 = BankAccount(100)
    m1: Memento = ba0.deposit(50)
    m2: Memento = ba0.deposit(25)
    print(ba0)

    # Restore to m1 memento
    ba0.restore(m1)
    print(ba0)

    # Restore to m2 memento
    ba0.restore(m2)
    print(ba0)

    print("\n\n------------------------------\n\n")

    ba1 = BankAccount(100)
    ba1.deposit(50)
    ba1.deposit(25)
    print(ba1)

    ba1.undo()
    print(f"Undo 1: {ba1}")

    ba1.undo()
    print(f"Undo 2: {ba1}")

    ba1.redo()
    print(f"Redo: {ba1}")