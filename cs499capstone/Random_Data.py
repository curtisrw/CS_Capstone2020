from random import randint


def exterior_doors_simulator():

    closed = 0
    opened = 1
    front_door = randint(closed, opened)
    back_door = randint(closed, opened)
    garage_into_house_door = randint(closed, opened)
    garage_door_one = randint(closed, opened)
    garage_door_two = randint(closed, opened)


def interior_doors_state():
    opened = True
    closed = False

    master_bedroom_door = closed
    master_bathroom_door = closed
    child_one_bedroom_door = closed
    child_two_bedroom_door = closed
    children_bathroom_door = closed
    living_room_bathroom_door = closed
    dining_room_door = closed
    kitchen_door = closed
    hallway_door = closed


def interior_doors_random_simulator():

    closed = 0
    opened = 1

    master_bedroom_door = randint(closed, opened)
    master_bathroom_door = randint(closed, opened)
    child_one_bedroom_door = randint(closed, opened)
    child_two_bedroom_door = randint(closed, opened)
    children_bathroom_door = randint(closed, opened)
    living_room_door = randint(closed, opened)
    dining_room_door = randint(closed, opened)
    kitchen_door = randint(closed, opened)
    hallway_door = randint(closed, opened)


def windows_state():
    opened = True
    closed = False

    master_bedroom_window_one = closed
    master_bedroom_window_two = closed
    child_one_bedroom_window = closed
    child_two_bedroom_window = closed
    master_bathroom_window = closed
    children_bathroom_window = closed
    living_room_window = closed
    dining_room_window = closed
    kitchen_window = closed
    hallway_window = closed


def windows_random_simulator():

    closed = 0
    opened = 1

    master_bedroom_window_one = randint(closed, opened)
    master_bedroom_window_two = randint(closed, opened)
    child_one_bedroom_window = randint(closed, opened)
    child_two_bedroom_window = randint(closed, opened)
    master_bathroom_window = randint(closed, opened)
    children_bathroom_window = randint(closed, opened)
    living_room_window = randint(closed, opened)
    dining_room_window = randint(closed, opened)
    kitchen_window = randint(closed, opened)
    hallway_window = randint(closed, opened)
