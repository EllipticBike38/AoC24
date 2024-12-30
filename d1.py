DEBUG = False
def read_from_file(file_path: str) -> str:
    if DEBUG:
        return '''3   4
4   3
2   5
1   3
3   9
3   3'''
    with open(file_path, 'r') as file:
        return file.read()

def separate_input(input_string: str) -> tuple:
    input_list = input_string.split('\n')
    lists = [int(i.split()[0]) for i in input_list], [ int(i.split()[1]) for i in input_list]
    return lists

def main(input_string: str) -> str:
    DEBUG and print(input_string)
    x, y = separate_input(input_string)
    DEBUG and print(x, y)
    score =[y.count(x[i])*x[i] for i in range(len(x))]
    DEBUG and print(score)
    sum_score = sum(score)
    return str(sum_score)

if __name__ == '__main__':
    my_input = read_from_file('d1.txt')
    print(main(my_input))