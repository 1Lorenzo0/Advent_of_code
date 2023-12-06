from functools import reduce

def get_game_number(input):
    game_number = int(input.split(':')[0].split()[-1]) # Gioco 1 : ... -> Gioco 1 -> 1
    return game_number


def get_sets(input):
    sets = input.split(':')[-1]
    return sets

def get_power(input): # input -> set1 ; set2 ; set3
    set_list = input.split(';') # set1 ; set2 ; set3 -> [set1, set2, set3]
    type_of_dices = { "red" : 0, "green" : 0, "blue" : 0}
    for set in set_list:
        color_list = set.split(',') # set1 : n1 blue, n2 red -> [n1 blue, n2 red]
        for color_and_num in color_list: #n color
            num, color = color_and_num.split() # n color -> num = n , color = color
            type_of_dices[color] = max(type_of_dices[color], int(num))
    power = reduce(lambda x, y: x * y, type_of_dices.values(), 1)
    return power

with open("./text", "r") as file:
    power = 0
    for line in file:
        game_number = get_game_number(line)
        sets = get_sets(line)
        power += get_power(sets)
    print(power)
