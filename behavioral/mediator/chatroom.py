class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat sesion] {s}")
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joines the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


def main():
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("Hi room")
    jane.say("Oh, hey John")

    simon = Person("Simon")
    room.join(simon)
    simon.say("Hi everyone")

    jane.private_message("Simon", "Glad you could join us")


if __name__ == "__main__":
    main()
