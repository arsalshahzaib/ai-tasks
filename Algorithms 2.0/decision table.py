# Implementation of Decision Table


def open_door():

    print("Door opened")


def go_to_floor(floor):

    print(f"Going to floor {floor}")


def decide(floor, button):
    if floor == "first" and button == "first":
        open_door()
    elif floor == "first" and button == "second":
        go_to_floor(2)
    elif floor == "first" and button == "third":
        go_to_floor(3)
    elif floor == "second" and button == "first":
        go_to_floor(1)
    elif floor == "third" and button == "first":
        go_to_floor(1)
    else:
        print("Invalid input")


decide("first", "first")
decide("first", "second")
decide("first", "third")
decide("second", "first")
decide("third", "first")
