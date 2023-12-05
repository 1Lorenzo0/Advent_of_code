def numConcat(num1, num2):
  return eval(f"{num1}{num2}")

def main():
    word_number = { "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9 }
    with open('./text') as file:
        sum = 0
        for line in file:
            first = -1
            last = 0
            for index, char in enumerate(line):
                if char.isdigit():
                    if first == -1:
                        first = char
                    last = char
            print(line)
            print(str(first) + str(last))
            sum += numConcat(first, last)
    return sum

if __name__ == "__main__":
    sum = main()
    print(sum)
