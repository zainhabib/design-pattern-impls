from enum import Enum
from abc import abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_off(self, name):
        pass


class Relationships(RelationshipBrowser):   # Low level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child),
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_off(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield {r[2].name}


class Research: # High level module
    # def __init__(self, relationships: Relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f"John has a child named {r[2].name}.")
    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_off("John"):
            print(f"John has a child named {p}.")