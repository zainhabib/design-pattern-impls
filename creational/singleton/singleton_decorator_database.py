def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        print("type: ", type(class_))
        print("class_ : ", class_)
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

        print("instances: ", instances)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Loading Database")

