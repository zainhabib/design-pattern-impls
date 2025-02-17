class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier: CreatureModifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you")


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}'s defense")
            self.creature.defense += 1

        super().handle()


def main():
    goblin: Creature = Creature("Goblin", 1, 1)
    print(goblin)

    root: CreatureModifier = CreatureModifier(goblin)

    print(f"\n\n\n1 --------------------------")
    # root.add_modifier(NoBonusModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))

    print(f"\n\n\n2 --------------------------")
    root.add_modifier(DoubleAttackModifier(goblin))

    print(f"\n\n\n3 --------------------------")
    root.add_modifier(IncreaseDefenseModifier(goblin))

    root.handle()
    print(goblin)


if __name__ == '__main__':
    main()
