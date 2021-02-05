from random import randint
import requests
from datetime import datetime
from datetime import timedelta


def get_time():
    datetime_object = datetime.now()
    print(datetime_object)

    return datetime_object


def day():
    week_day = datetime.today().weekday()

    if week_day < 5:
        print("Weekday")
    else:
        print("Weekend")

    return


def weather_api():

    request = requests.get('https://api.darksky.net/forecast/36cac7f029f2d48dfc60ff57e336dba3/37.8267,-122.4233')
    print(request.text)

    readable_request = request.json()

    current_outdoor_temp = readable_request['currently']['temperature']
    print("Temperature: ", current_outdoor_temp)

    return current_outdoor_temp


def hvac_system():

        minutes = 0
        exterior_door_open = 0.4
        window_open = 0.2
        time = get_time()

        user_set_temp = float(input("Enter your desired temperature: "))
        current_home_temp = 70.0

        # this will come from the weather API
        external_temp = weather_api()

        open_doors = exterior_doors_state()

        for x in exterior_doors_state():
            if x == False:
                current_home_temp = current_home_temp
            elif x == True:
                current_home_temp = current_home_temp + exterior_door_open

        print(current_home_temp)
        print(exterior_doors_state())

        if user_set_temp < external_temp:
            current_home_temp = current_home_temp - 1
        elif user_set_temp > external_temp:
            current_home_temp = current_home_temp + 1


def electricity_consumption():
    electricity_cost = 0.12


def water_usage():
    return


def exterior_doors_simulator():

    closed = 0
    opened = 1
    front_door = randint(closed, opened)
    back_door = randint(closed, opened)
    garage_into_house_door = randint(closed, opened)
    garage_door_one = randint(closed, opened)
    garage_door_two = randint(closed, opened)

    exterior_doors_simulator_states = [front_door, back_door, garage_into_house_door, garage_door_one, garage_door_two]

    return exterior_doors_simulator_states


def exterior_doors_state():
    opened = True
    closed = False

    front_door = input("Front Door: ")
    back_door = input("Back Door: ")
    garage_into_house_door = input("Garage into Home Door: ")
    garage_door_one = input("Garage One Door: ")
    garage_door_two = input("Garage Two Door: ")

    exterior_doors_states1 = [front_door, back_door, garage_into_house_door, garage_door_one, garage_door_two]
    exterior_doors_states2 = []

    for x in exterior_doors_states1:
        if x == '1':
            exterior_doors_states2.append("open")
        elif x == '0':
            exterior_doors_states2.append("closed")

    return exterior_doors_states2


def interior_doors_state():
    opened = True
    closed = False

    master_bedroom_door = input("Master Bedroom Door: ")
    master_bathroom_door = input("Master Bathroom Door:  ")
    child_one_bedroom_door = input("Child One Door:  ")
    child_two_bedroom_door = input("Child Two Door: ")
    children_bathroom_door = input("Children Bathroom Door: ")
    living_room_door = input("Living Room Door: ")
    dining_room_door = input("Dining Room Door: ")
    kitchen_door = input("Kitchen Door: ")
    hallway_door = input("Hallway Door: ")

    interior_doors_states1 = [master_bedroom_door, master_bathroom_door, child_one_bedroom_door, child_two_bedroom_door,
                             children_bathroom_door, living_room_door, dining_room_door, kitchen_door,
                             hallway_door]

    interior_doors_states2 = []

    for x in interior_doors_states1:
        if x == '1':
            interior_doors_states2.append("open")
        elif x == '0':
            interior_doors_states2.append("closed")

    return interior_doors_states2


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

    interior_doors_random_simulator_states = [master_bedroom_door, master_bathroom_door, child_one_bedroom_door,
                                              child_two_bedroom_door, children_bathroom_door, living_room_door,
                                              dining_room_door, kitchen_door, hallway_door]

    return interior_doors_random_simulator_states


def windows_state():
    opened = True
    closed = False

    master_bedroom_window_one = input("Master Bedroom Window One: ")
    master_bedroom_window_two = input("Master Bedroom Window Two: ")
    child_one_bedroom_window = input("Child One Bedroom Window: ")
    child_two_bedroom_window = input("Child Two Bedroom Window: ")
    master_bathroom_window = input("Master Bathroom Window: ")
    children_bathroom_window = input("Children Bathroom Window: ")
    living_room_window = input("Living Room Window: ")
    dining_room_window = input("Dining Room Window: ")
    kitchen_window = input("Kitchen Window: ")
    hallway_window = input("Hallway Window: ")

    windows_states1 = [master_bedroom_window_one, master_bedroom_window_two, child_one_bedroom_window, child_two_bedroom_window,
                      master_bathroom_window, children_bathroom_window, living_room_window, dining_room_window,
                      kitchen_window, hallway_window]

    windows_states2 = []

    for x in windows_states1:
        if x == '1':
            windows_states2.append("open")
        elif x == '0':
            windows_states2.append("closed")

    return windows_states2


    return windows_states


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

    windows_random_simulator_states = [master_bedroom_window_one, master_bedroom_window_two, child_one_bedroom_window,
                                       child_two_bedroom_window, master_bathroom_window, children_bathroom_window,
                                       living_room_window, dining_room_window, kitchen_window, hallway_window]

    return windows_random_simulator_states


def weekday_exterior_door_events():
    for _ in range(16):
        print(exterior_doors_simulator())


def weekend_exterior_door_events():
    for _ in range(32):
        print(exterior_doors_simulator())


y = exterior_doors_state()
print(y)

