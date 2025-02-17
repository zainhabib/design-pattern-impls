# Implemnts
# Single Responsibility Principal or Sepration of Concern

from journal import Journal
from persistence_manager import PersistenceManager

if __name__ == '__main__':
    j = Journal()
    j.add_entry("I cried today")
    j.add_entry("I age a bug")
    print(f"Journal entries:\n{j}")

    file = r"/tmp/journal.txt"

    PersistenceManager.save_to_file(j, file)

    with open(file) as fh:
        print(fh.read())
