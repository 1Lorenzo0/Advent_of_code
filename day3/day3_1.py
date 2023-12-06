def find_symbol(matrix, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:  
                continue

            new_x, new_y = x + i, y + j
            if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                if not matrix[new_x][new_y].isdigit() and matrix[new_x][new_y] != ".": # i have a symbol
                    return True
    return False

def reset():
    return False, ''

with open("./text", "r") as file:
    cols = 141
    rows = 0
    matrix = []
    sum = 0
    with open('./text', 'r') as file:
        for line in file:
            row = [char for char in line.strip()]  
            matrix.append(row)
    
    for i in range(len(matrix)):
        to_store, num_to_store = reset()
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit(): #if number i need to store it, i can have more than one unit
                num_to_store += str(matrix[i][j])
                if find_symbol(matrix,i,j): #i need to check if there are simbols near
                    to_store = True
            else:
                if to_store: # 123 ... 135 ... ecc.. (i need to sum 123 to other, and prepare to reset)
                    sum += int(num_to_store)
                to_store, num_to_store = reset()
                
        if to_store:  #after the cycle i need to store the number if it is to store. ( ...1235)
            sum += int(num_to_store)

    print("sum: " + str(sum))
    
