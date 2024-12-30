import re

DEBUG = not True
def read_from_file(file_path: str) -> str:
    if DEBUG:
        return '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''
    with open(file_path, 'r') as file:
        return file.read()

def clean_string(input_string: str) -> str:
    return re.findall(r'mul\(\d*,\d*\)', input_string) 

def execute_mul(mul: str) -> int:
    mul = mul[4:-1].split(',')
    return int(mul[0]) * int(mul[1])

def main(input_str):
    DEBUG and print(input_str)
    cleaned = clean_string(input_str)
    DEBUG and print(cleaned)
    cleaned = [execute_mul(mul) for mul in cleaned]
    DEBUG and print(cleaned)
    cleaned = sum(cleaned)
    return str(cleaned)

if __name__ == '__main__':
    my_input = read_from_file('d3.txt')
    print(main(my_input))
