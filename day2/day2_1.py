def get_game_number(input):
    game_number = int(input.split(':')[0].split()[-1]) # Gioco 1 : ... -> Gioco 1 -> 1
    return game_number


def get_sets(input):
    sets = input.split(':')[-1]
    return sets

def is_possible(input, max_colors): # input -> set1 ; set2 ; set3
    set_list = input.split(';') # set1 ; set2 ; set3 -> [set1, set2, set3]
    for set in set_list:
        color_list = set.split(',') # set1 : n1 blue, n2 red -> [n1 blue, n2 red]
        for color_and_num in color_list: #n color
            num, color = color_and_num.split() # n color -> num = n , color = color 
            if max_colors[color] < int(num): 
                return False
    return True
  

with open("./text", "r") as file:
    max_colors = {"red" : 12, "green" : 13, "blue" : 14}
    sum = 0
    for line in file:
        game_number = get_game_number(line)
        sets = get_sets(line)
        possible = is_possible(sets, max_colors)
        if possible:
            sum += int(game_number)

    print(sum)
