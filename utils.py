import random


def get_new_field(cells_count):
    """Get new list with field and one random element for enemy"""
    field_tmp = [[0 for j in range(cells_count)] for i in range(cells_count)]
    i, j = random.randint(0, cells_count - 1), random.randint(0, cells_count - 1)
    field_tmp[i][j] = 1
    return field_tmp


def get_coords_by_field(field, cell_size):
    """Get x, y coords by field"""
    enemy_coords_in_field = (0, 0)
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                enemy_coords_in_field = (i, j)
    return enemy_coords_in_field[0] * cell_size, enemy_coords_in_field[1] * cell_size + 100
