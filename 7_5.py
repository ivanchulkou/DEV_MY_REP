from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},

]

# room_square = lambda i: i["length"] * i["width"]
all_squares = list(map(lambda i: i["length"] * i["width"], rooms))
total_square = reduce(lambda x, y: x + y, all_squares)
print(f'Общая площадь квартиры: {total_square} кв.м')


