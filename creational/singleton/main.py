from singleton_database import Database
# from singleton_decorator_database import Database
# from singleton_meta_database import Database

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
