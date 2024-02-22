def NULL_not_found(object: any) -> int:
    if (object != object):
        print("Cheese :", object, object.__class__)
        return (0)
    elif (not object):
        if (object.__class__.__name__ == "NoneType"):
            print("Nothing :", object, object.__class__)
            return (0)
        elif (object.__class__.__name__ == "int"):
            print("Zero :", object, object.__class__)
            return (0)
        elif (object.__class__.__name__ == "str"):
            print("Empty :", object, object.__class__)
            return (0)
        elif (object.__class__.__name__ == "bool"):
            print("Fake :", object, object.__class__)
            return (0)
    else:
        print("Type not found")
        return (1)
