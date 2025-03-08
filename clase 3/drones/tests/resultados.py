from src.drones.models.quadcopter import Quadcopter
from src.drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right
import pytest



def test_take_off():
    drone = Quadcopter("raptor", 0, 0, [Take_off()])
    drone.follow_commands()
    print('test_take_off x:', drone.x)
    print('test_take_off y:', drone.y)

def test_forward():
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Forward(5)])
    drone.follow_commands()
    print('test_forward x:', drone.x)
    print('test_forward y:', drone.y)

def test_backward():    
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Backward(5)])
    drone.follow_commands()
    print('test_backward x:', drone.x)
    print('test_backward y:', drone.y)

def test_turn_left():
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Turn_left()])
    drone.follow_commands()
    print('test_turn_left direction:', drone.direction)

def test_turn_right():
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Turn_right()])
    drone.follow_commands()
    print('test_turn_right direction:', drone.direction)

def test_land():
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Land()])
    drone.follow_commands()
    print('test_land flying:', drone.flying)
    print('test_land x:', drone.x)
    print('test_land y:', drone.y)
    print('test_land direction:', drone.direction)

def test_multiple_commands():
    drone = Quadcopter("raptor", 0, 0, [Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()])
    drone.follow_commands()
    print('test_multiple_commands flying:', drone.flying)
    print('test_multiple_commands x:', drone.x)
    print('test_multiple_commands y:', drone.y)
    print('test_multiple_commands direction:', drone.direction)

if __name__ == "__main__":
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off()]))
    for drone in drones:
        drone.follow_commands()
        print('test_take_off:', drone)
        print('test_take_off y:', drone.y)
        break
    