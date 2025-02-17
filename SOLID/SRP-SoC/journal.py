class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


    ## The following functions work but breaks the
    ## SOLID SRP/SoC Principles
    # def save(self, filename):
    #     file = open(file=filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


if __name__ == '__main__':
    j = Journal()
    j.add_entry("I cried today")
    j.add_entry("I age a bug")
    print(f"Journal entries:\n{j}")
