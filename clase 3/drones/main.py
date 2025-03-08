from src.drones.models.quadcopter import Quadcopter
from src.drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right
import concurrent.futures
import random
import string

def generate_random_name(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_unique_names(count, length=5):
    unique_names = set()
    while len(unique_names) < count:
        unique_names.add(generate_random_name(length))
    return list(unique_names)


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        num_names = 10
        names_vector = generate_unique_names(num_names)
        futures = []
        drones = []
        drones_list = []
        moved=[Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()]
        for name in names_vector:
            futures.append(executor.submit(Quadcopter, name, 0, 0, moved))
        for future in concurrent.futures.as_completed(futures):
            drones = future.result()
            drones_list.append(drones)
        for drone in drones_list:
            drone.follow_commands()


if __name__ == "__main__":

    main()
