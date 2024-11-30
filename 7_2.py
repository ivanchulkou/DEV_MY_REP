print('Дан список: [-2, 5, 4, 6, 8, -8, -2]')
spis = [-2, 5, 4, 6, 8, -8, -2]


def positive(x):
    if x > 0:
        return True
    return False


filter_pos = list(filter(positive, spis))
print(f'Элемeнты данного списка, значение которых больше 0: {filter_pos}')
"""
# используя оператор continue
i_list = []
for i in spis:
    if i < 0:
        continue   
    i_list.append(i)
print(i_list)
"""
