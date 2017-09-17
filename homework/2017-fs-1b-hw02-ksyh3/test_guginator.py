"""Tests for guginator module

"""
import pytest

from guginator import UserInputError, food, walk, mood


class FakeNamespace(object):
    """This is a dummy class used to imitate an argparse.Namespace object.
    Simply assign member variables as necessary.

    """
    pass


def test_invalid_day():
    """Ensure we raise an exception when given a bogus day"""
    # Create a fake namespace and set its "day" to something dumb
    n = FakeNamespace()
    n.day = "Foosday"

    with pytest.raises(UserInputError):
        food(n)


def test_weekday_inputs():
    """Ensure we recieve proper output for each proper weekday"""
    weekdays = {
        "Sunday": "frozen corn",
        "Monday": "one gallon of saurkraut",
        "Tuesday": "hot dog water",
        "Wednesday": "drywall",
        "Thursday": "grass clippings",
        "Friday": "old bananas",
        "Saturday": "dirt",
    }

    for day, food_type in weekdays.items():
        n = FakeNamespace()
        n.day = day
        assert food(n) == "Gug wants {}".format(food_type)


def test_weekday_inputs_with_capitalization():
    """
    Ensure we recieve proper output for each weekday with any captilization
    """
    weekdays = {
        "SuNday": "frozen corn",
        "MONDAY": "one gallon of saurkraut",
        "TUESday": "hot dog water",
        "WednesdAY": "drywall",
        "ThursDAY": "grass clippings",
        "FRIDay": "old bananas",
        "SaTuRdAy": "dirt",
    }

    for day, food_type in weekdays.items():
        n = FakeNamespace()
        n.day = day
        assert food(n) == "Gug wants {}".format(food_type)


def test_valid_walk():
    """Make sure we're computing the example walk correctly"""
    # Create a fake namespace and set its "path"
    n = FakeNamespace()
    n.path = [
        "0,0", "0,3", "2,3", "2,2", "3,2", "3,3",
        "4,3", "4,1", "2,1", "2,0", "0,0"
    ]

    assert walk(n) == (8, 8)


def test_invalid_walks():
    """Make sure we're failing walks with invalid parameters"""
    # Create a fake namespace and set its "path"
    n = FakeNamespace()
    n.path = [
        "0,0", "0,,3", "2,3", "2,2", "3,2", "3,3",
        "4,3", "4,1", "2,1", "2,0", "0,0"
    ]

    with pytest.raises(UserInputError):
        walk(n)

    n.path = [
        "0,0", "0,3.5", "2,3", "2,2", "3,2", "3,3",
        "4,3", "4,1", "2,1", "2,0", "0,0"
    ]

    with pytest.raises(UserInputError):
        walk(n)


def test_valid_mood():
    """Ensure mode returns the proper list with valid combinations"""
    # Create a fake namespace and set its "path"
    n = FakeNamespace()

    n.left = "bluce"
    n.right = "bluce"
    assert (
        mood(n) == ['Db', 'Bb', 'Db', 'F', 'Db', 'F', 'Ab', 'Ab', 'Ab', 'Ab']
    )

    n.left = "aquamablue"
    n.right = "nopaz"
    assert mood(n) == ['Db', 'F', 'Db', 'F', 'Ab']


def test_valid_mood_with_capitalization():
    """Ensure that mood succeeds if the capitalization changes"""
    # Create a fake namespace and set its "path"
    n = FakeNamespace()
    n.left = "AquamaBlue"
    n.right = "NOpaz"
    assert mood(n) == ['Db', 'F', 'Db', 'F', 'Ab']

    n.left = "bLuCe"
    n.right = "BlUcE"
    assert (
        mood(n) == ['Db', 'Bb', 'Db', 'F', 'Db', 'F', 'Ab', 'Ab', 'Ab', 'Ab']
    )


def test_invalid_mood_colors():
    """Ensure that mood returns an error with invalid colors"""
    # Create a fake namespace and set its "path"
    n = FakeNamespace()
    n.left = "test"
    n.right = "test"

    with pytest.raises(UserInputError):
        mood(n)

    n.left = "nopaz"
    n.right = "test"

    with pytest.raises(UserInputError):
        mood(n)

    n.left = "bluce"
    n.right = "test"

    with pytest.raises(UserInputError):
        mood(n)

    n.left = "test"
    n.right = "bluce"

    with pytest.raises(UserInputError):
        mood(n)
