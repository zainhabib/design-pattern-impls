from behavioral.observer.person import Person, PersonObservable
from behavioral.observer.traffic_authority import TrafficAuthority


def call_doctor(name, address):
    print(f"{name} needs a doctor at {address}")


if __name__ == '__main__':
    p = Person("Sherlock", "221B Baker St")
    p.falls_ill.append(
        lambda name, address: print(f"{name} is ill")
    )
    p.falls_ill.append(call_doctor)
    p.catch_a_cold()

    p.falls_ill.remove(call_doctor)
    p.catch_a_cold()

    # Observable
    p = PersonObservable()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f"Setting age to {age}")
        p.age = age

    # Indirect property change (age -> vote)
    print("\n\n----------------------------------------\n")


    def person_changed(name, value):
        if name == "can_vote":
            print(f"Voting ability changed to {value}")


    p = PersonObservable()
    p.property_changed.append(
        person_changed
    )

    for age in range(16, 20):
        print(f"Changing age to {age}")
        p.age = age
