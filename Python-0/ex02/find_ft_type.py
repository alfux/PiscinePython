def all_thing_is_obj(object: any) -> int:
    try:
        if (object.__class__ == str):
            print(object, "is in the kitchen", ":", object.__class__)
        elif (object.__class__ == int or object.__class__ == float):
            print("Type not found")
        else:
            print(object.__class__.__name__.capitalize(), ":", type(object))
    except BaseException:
        print("Type not found")
    return (42)
