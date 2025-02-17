from country import Country
from international_provider import InternationalProvider


def main():
    country = Country.ENGLAND
    factory = InternationalProvider.create(country)
    language = factory.create_language()
    capital_city = factory.create_capital_city()

    print(f"Country: {country.name}")

    print(f"Language: {language.__class__.__name__}")
    print(f"Greet: {language.greet()}")

    print(f"Capital City: {capital_city.__class__.__name__}")
    print(f"Total population: {capital_city.get_population()}.")
    print(f"Top attractions: {capital_city.list_top_attractions()}")


# Client
if __name__ == '__main__':
    main()
