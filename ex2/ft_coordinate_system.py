import math


def distance_between_points(p1: tuple, p2: tuple) -> None:
    """Calculates and prints the Euclidean distance between two 3D points."""
    try:
        dist = round(
            math.sqrt(
                (p2[0] - p1[0]) ** 2
                + (p2[1] - p1[1]) ** 2
                + (p2[2] - p1[2]) ** 2
            ),
            2,
        )
        return f"Distance between {p1} and {p2}: {dist}"
    except (IndexError, TypeError) as e:
        print(f"Error calculating distance: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def parsing_coordinates(coordinates: str) -> tuple:
    """Parses a string of comma-separated coordinates into a tuple"""
    try:
        tup = tuple(int(n) for n in coordinates.split(","))
        return tup
    except (IndexError, ValueError) as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def ft_coordinate_system():
    """Demonstrates uses of coordinate systems in a game context."""
    print("=== Game Coordinate System ===")

    origin: tuple = (0, 0, 0)
    p1: tuple = (10, 20, 5)
    print(f"\nPosition created {p1}")
    print(distance_between_points(origin, p1))

    coordinate_str = "3,4,0"
    print(f'\nParsing coordinates: "{coordinate_str}"')
    p2: tuple = parsing_coordinates(coordinate_str)
    print(f"Parsed position: {p2}")
    print(distance_between_points(origin, p2))

    invalid_coordinates = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_coordinates}"')
    p3: tuple = parsing_coordinates(invalid_coordinates)
    if p3:
        print(distance_between_points(origin, p3))

    print("\nUnpacking demonstration:")
    x, y, z = p2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()
