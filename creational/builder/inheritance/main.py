from person import PersonBirthDateBuilder

if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    d = pb.called("Dmitri").works_as_a("Quant").born("1990-09-12").build()
    print(d)