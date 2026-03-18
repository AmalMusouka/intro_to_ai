import math


def grid_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return dx + dy


def grid_diagonal_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return max(dx, dy)


def grid_3D_heuristic(current, destination):
    dx, dy, dz = distance_in_each_coordinate(current, destination)
    return dx + dy + dz


def grid_face_diagonal_3D_heuristic(current, destination):
    dx, dy, dz = sorted(distance_in_each_coordinate(current, destination))
    # use face diagonals first
    return dz


def grid_all_diagonal_3D_heuristic(current, destination):
    dx, dy, dz = distance_in_each_coordinate(current, destination)
    return max(dx, dy, dz)


def grid_great_king_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)
    return max(math.ceil(dx / 8), math.ceil(dy / 8))


def grid_rook_2D_heuristic(current, destination):
    dx, dy = distance_in_each_coordinate(current, destination)

    if dx == 0:
        return math.ceil(dy / 8)
    if dy == 0:
        return math.ceil(dx / 8)

    return math.ceil(dx / 8) + math.ceil(dy / 8)


def grid_jumper_2D_heuristic(current, destination):
    dx, dy = sorted(distance_in_each_coordinate(current, destination), reverse=True)

    # each move changes |dx|+|dy| by at most 5
    return max(
        math.ceil(dx / 3),
        math.ceil((dx + dy) / 5)
    )