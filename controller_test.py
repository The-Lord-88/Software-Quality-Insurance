import pytest
from model import Model
from controller import Controller

@pytest.fixture
def model():
    return Model()

@pytest.fixture
def controller():
    return Controller(model)

def test_clear_button(controller):
    controller.button_pressed("4")
    controller.button_pressed("2")
    controller.button_pressed("C")
    assert model.display == "0"

def test_del_button(controller):
    controller.button_pressed("4")
    controller.button_pressed("2")
    controller.button_pressed("Del")
    assert model.display == "4"

def test_digit_press(controller):
    controller.button_pressed("4")
    controller.button_pressed("2")
    controller.button_pressed("+")
    controller.button_pressed("1")
    controller.button_pressed("8")
    assert model.display == "18"

def test_equal_press(controller):
    controller.button_pressed("4")
    controller.button_pressed("2")
    controller.button_pressed("+")
    controller.button_pressed("1")
    controller.button_pressed("8")
    controller.button_pressed("=")
    assert model.display == "60"
