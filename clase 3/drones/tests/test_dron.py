from src.drones.models.quadcopter import Quadcopter
from src.drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right
import pytest

def test_take_off():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.x == 0
    assert drone.y == 0

def test_forward():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Forward(5),Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.x == 50
    assert drone.y == 0

def test_backward():    
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Backward(5),Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.x == 0
    assert drone.y == -50

def test_turn_left():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Turn_left(),Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.direction == "W"

def test_turn_right():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Turn_right(),Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.direction == "E"

def test_land():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.flying == False
    assert drone.x == 0
    assert drone.y == 0
    assert drone.direction == "N"

def test_multiple_commands():
    drones = []
    drones.append(Quadcopter("raptor", 0, 0, [Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()]))
    for drone in drones:
        drone.follow_commands()
    assert drone.flying == False
    assert drone.x == 0
    assert drone.y == -10
    assert drone.direction == "N"



@pytest.mark.parametrize("n", [Take_off(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Forward(5), Turn_left(), Backward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Forward(5), Turn_right(), Backward(5), Land()])
def test_factorial_benchmark(benchmark, n):
    benchmark.pedantic(Quadcopter, args=("raptor", 0, 0,n,), rounds=100, iterations=1000)