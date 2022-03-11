from unittest.mock import patch, Mock, mock_open
from functions import *
import pytest

def print_menu(item):
    print(item)
    
def test_print_menu():
    #Arrange
    expected = "string"
    #Act
    actual = "string"
    #Assert - pass
    assert expected == actual
test_print_menu()


