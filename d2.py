DEBUG = False
def read_from_file(file_path: str) -> str:
    if DEBUG:
        return '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    with open(file_path, 'r') as file:
        return file.read()
    
def check_safety(report:str) -> bool:
    report = report.split()
    increase = 1 if int(report[0]) < int(report[1]) else -1
    DEBUG and print('increase' if increase == 1 else 'decrease')
    if increase == -1:
        report = report[::-1]
    return all([ 0<int(report[i+1]) - int(report[i])<4 for i in range(len(report)-1)])

def main(input_string: str) -> str:
    DEBUG and print(input_string)
    reports = input_string.split('\n')
    safes = [check_safety(report) for report in reports]
    DEBUG and  print('-'*10)
    DEBUG and print(*[f'{a} - {b}' for a, b in zip(reports, safes)], sep='\n')
    count = sum(safes)
    return str(count)   

if __name__ == '__main__':
    my_input = read_from_file('d2.txt')
    print(main(my_input))