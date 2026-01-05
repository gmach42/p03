import sys
import math


def distance_between_points(p1: tuple, p2: tuple) -> float:
    return round(
        math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 +
                  (p2[2] - p1[2])**2), 2)


def unpacking_coordinates(point: tuple) -> str:
    x, y, z, = point
    return f"x: {x}, y: {y}, z: {z}"


def parsing_coordinates(args: list) -> tuple:
    print(f"Parsing coordinates: {args}")
    try:
        x = int(args[0])
        y = int(args[1])
        z = int(args[2])
        return (x, y, z)
    except (IndexError, ValueError) as e:
        print("Error: Please provide three numeric arguments for coordinates.")
        print(f"Error details - Type: {type(e)}, Message: {e}")
        return None


def main():
    print("=== Game Coordinate System ===")
    args = sys.argv[1:]
    point = parsing_coordinates(args)
    if point:
        print(f"Parsed position: {point}")
        origin = (0, 0, 0)
        distance = distance_between_points(origin, point)
        print(f"Distance from origin to point: {distance}")
        print("\nCoordinates unpacked:", unpacking_coordinates(point))


if __name__ == "__main__":
    main()
