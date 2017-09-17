import argparse
import sys


# Implement missing functions and exception classes here
class UserInputError(Exception):
    """
    Raised when input provided by the user is invalid or inappropriately
    formatted, preventing the program from proceeding.
    """


def food(args):
    """
    Determine which food to feed Gug for a given day of the week.

    :param args: A Namespace object. args.day should be a day of the week. It
                 must be a str.
    :type args: argparse.Namespace

    :returns: A message explaining what to feed Gug
    :rtype: str
    :raises UserInputError: if args.day is not a valid day of the week
    """
    weekdays = {
        "sunday": "frozen corn",
        "monday": "one gallon of saurkraut",
        "tuesday": "hot dog water",
        "wednesday": "drywall",
        "thursday": "grass clippings",
        "friday": "old bananas",
        "saturday": "dirt",
    }

    user_input_day = args.day
    # Lower to allow all capitalization
    food = weekdays.get(user_input_day.lower(), None)

    if food is not None:
        return "Gug wants {}".format(food)
    else:
        raise UserInputError(
            "{} is not a valid day of the week".format(user_input_day)
        )


def walk(args):
    """
    Calculates the east-west and north-south Manhattan distances traveled by
    walking Gug through the Downtown section of the Tri-State Area.

    The path provided must be a list of coordinates as strings with format x,y,
    where x and y are integers corresponding to the x- and y-coordinates of a
    map of Downtown.

    :params args: A Namespace object. args.path should be a list of
                  x,y coordinates as str.
    :type args: argparse.Namespace

    :returns:    A tuple of the form (east-west distance, north-south distance)
    :rtype: tuple of int
    :raises UserInputError: if args.path contains invalid coordinates
    """
    path = args.path

    total_x = 0
    total_y = 0
    previous_x = 0
    previous_y = 0

    for coordinate in path:
        new_coords = coordinate.split(",")
        cur_x = None
        cur_y = None

        if len(new_coords) != 2:
            raise UserInputError(
                "{} is an invalid coordinate".format(coordinate)
            )

        try:
            cur_x = int(new_coords[0])
            cur_y = int(new_coords[1])
        except ValueError:
            raise UserInputError(
                "{} is an invalid coordinate".format(coordinate)
            )

        total_x += abs(cur_x - previous_x)
        total_y += abs(cur_y - previous_y)

        previous_x = cur_x
        previous_y = cur_y

    return (total_x, total_y)


def mood(args):
    """
    Computes Gug’s bedtime song based on the color of his eyes.
    Parameters:

    :type args: argparse.Namespace
    :param args: A Namespace object. args.right should be a str: the color of
                 Gug’s right eye. args.left should be a str: the color of Gug’s
                 left eye.

    :returns: The notes to play for Gug
    :rtype: list of str
    :raises UserInputError: if args.right is not a valid color
    :raises UserInputError: if args.left is not a valid color
    """
    bedtime_notes = ['Db', 'Bb', 'Db', 'F', 'Db', 'F', 'Ab', 'Ab', 'Ab', 'Ab']

    offsets = {
        "bluce": 0,
        "turporple": 1,
        "aquamablue": 2,
        "nopaz": 3,
    }
    user_left_input = args.left
    user_right_input = args.right

    left_offset = offsets.get(user_left_input.lower(), None)
    right_offset = offsets.get(user_right_input.lower(), None)

    if left_offset is None:
        raise UserInputError(
            "{} is not a valid color".format(user_left_input)
        )
    elif right_offset is None:
        raise UserInputError(
            "{} is not a valid color".format(user_right_input)
        )

    # Turns the right offset negative and substracts 1
    if right_offset == 0:
        return bedtime_notes[left_offset::]
    else:
        return bedtime_notes[left_offset:-right_offset]


def main():
    """Parses command line arguments and calls helper functions
    accordingly.

    There is no need to change anything in this function. It is
    complete as it is.

    """

    # Set up our command line parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands')
    parser.set_defaults(func=lambda x: parser.format_help())

    # Handle the "food" subcommand
    food_subparser = subparsers.add_parser('food', help='Identify food')
    food_subparser.add_argument('day', help='The day of the week')
    food_subparser.set_defaults(func=food)

    # Handle the "walk" subcommand
    walk_subparser = subparsers.add_parser('walk', help='Calculate walk')
    walk_subparser.add_argument('path', nargs='+', help='The path you walked')
    walk_subparser.set_defaults(func=walk)

    # Handle the "mood" subcommand
    mood_subparser = subparsers.add_parser('mood', help='Handle mood')
    mood_subparser.add_argument('left', help='The color of Gug\'s left eye')
    mood_subparser.add_argument('right', help='The color of Gug\'s right eye')
    mood_subparser.set_defaults(func=mood)

    # Parse the arguments from the command line
    args = parser.parse_args()

    try:
        # Invoke the function the user requested (food, walk, or mood)
        # and print the return value
        print(args.func(args))
    except UserInputError as e:
        # If the invoked function raised a UserInputError, print out
        # the error message and return a non-zero exit code.
        sys.exit("Error! {}".format(e))


if __name__ == '__main__':
    # Don't change this either.
    main()
