from html import HtmlBuilder, HtmlElement
from person import Person, PersonBuilder

if __name__ == '__main__':
    builder = HtmlBuilder("html")
    builder.add_child("ul", "")
    builder.add_child("li", "Hello")
    builder.add_child("li", "world")
    # print("Ordinary builder")
    # print(builder)

    builder = HtmlBuilder("html")
    (
        builder.add_child_fluent("ul", "")
        .add_child_fluent("li", "Hello")
        .add_child("li", "world")
    )
    print("Fluent builder")
    print(builder)


    ## Alternate
    builder = HtmlElement.create("html")
    (
        builder.add_child_fluent("ul", "")
        .add_child_fluent("li", "Hello")
        .add_child("li", "world")
    )
    print("HtmlElement Create builder")
    print(builder)



    ###### Person
    pb = PersonBuilder()
    person = pb \
        .lives.at("1 Way Street").in_city("Utopia").with_postcode("12345") \
        .works.at("Chocolate Factory").as_a("Umpa Lumpa").earning(120000) \
        .build()

    print(person)
