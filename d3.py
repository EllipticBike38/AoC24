import re

DEBUG = not True
def read_from_file(file_path: str) -> str:
    if DEBUG:
        return '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
    with open(file_path, 'r') as file:
        return file.read()

def flatten_list(l: list) -> list:
   return [item for sublist in l for item in sublist if item]

def clean_string(input_string: str) -> str:
    return flatten_list(re.findall(r'(mul\(\d*,\d*\))|(don\'t\(\))|(do\(\))', input_string))

def find_mul(list_mul: list[str]) -> str:
    don_t = False
    muls = []
    for el in list_mul:
        if 'don\'t' in el:
            don_t = True
        elif 'do' in el:
            don_t = False
        elif not don_t:
            muls.append(el)
    return muls
    
    
def execute_mul(mul: str) -> int:    
    mul = mul[4:-1].split(',')
    return int(mul[0]) * int(mul[1])

def main(input_str):
    DEBUG and print('input_str: ' + input_str)
    cleaned = clean_string(input_str)
    DEBUG and print('cleaned: ' + str(cleaned))
    cleaned = find_mul(cleaned)
    DEBUG and print('cleaned: ' + str(cleaned))
    cleaned = [execute_mul(mul) for mul in cleaned]
    DEBUG and print(cleaned)
    cleaned = sum(cleaned)
    return str(cleaned)

if __name__ == '__main__':
    my_input = read_from_file('d3.txt')
    print(main(my_input))
