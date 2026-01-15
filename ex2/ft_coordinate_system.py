import math


def distance_between_points(p1: tuple, p2: tuple):
    dist = round(
        math.sqrt((p2[0] - p1[0])**2 +
                  (p2[1] - p1[1])**2 +
                  (p2[2] - p1[2])**2), 2
        )
    print(f"Distance between {p1} and {p2}: {dist}")


def unpacking_coordinates(point: tuple) -> str:
    x, y, z, = point
    return f"x: {x}, y: {y}, z: {z}"


def parsing_coordinates(coordinates: str) -> tuple:
    try:
        tup = tuple(int(n) for n in coordinates.split())
        return tup
    except (IndexError, ValueError) as e:
        print("Error: Please provide three numeric arguments for coordinates.")
        print(f"Error details - Type: {type(e)}, Message: {e}")
        return None


def main():
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    p1 = (10, 20, 5)
    print(f"\nPosition created {p1}")
    distance_between_points(origin, p1)

    coordinate_str = "3,4,0"
    print(f"\nParsing coordinates: {coordinate_str}")
    p2 = parsing_coordinates(coordinate_str)
    distance_between_points(origin, p2)

    invalid_coordinates = "abc,def,ghi"
    try:
        p3 = parsing_coordinates(invalid_coordinates)
        distance_between_points(origin, p3)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    print("\nUnpacking demonstration:")
    (x, y, z) = p2
    print(f"Coordinates: {x}, {y}, {z}")


if __name__ == "__main__":
    main()
