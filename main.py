import json
import random


def file_reader() -> (list,):
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    return data


# getting random commands here
def random_co() -> (list,):
    data = file_reader()
    # getting random commands data
    random_c = random.sample(data, 2)
    return random_c


# getting parse commands here
def parse_co() -> (list,):
    data = file_reader()
    parse_c = [row.copy() for row in data if ('function' in row) and (row['function'] == 'parse')]
    return parse_c


# getting copy commands here
def copy_co() -> (list,):
    data = file_reader()
    copy_c = [row.copy() for row in data if ('function' in row) and (row['function'] == 'copy')]
    return copy_c


# getting bad commands here
def bad_co() -> (list,):
    bad_c = []
    data = file_reader()
    for row in data:
        if ('function' in row and row['function'] == 'bad value') or ('value' in row and row['value'] == 'bad value'):
            bad_c.append(row.copy())
    return bad_c


# getting functional commands here
def functional_co() -> (list,):
    parse_com, copy_com, functional_c = [], [], []
    data = file_reader()
    for row in data:
        if 'function' in row and row['function'] == 'parse':
            parse_com.append(row.copy())
            # appending parse data to functional commands list with count values
            temp = dict({'_list': 'parse', '_counter': len(parse_com)}, **row.copy())
            functional_c.append(temp)
        elif 'function' in row and row['function'] == 'copy':
            copy_com.append(row.copy())
            # appending copy data to functional commands list with count values
            temp = dict({'_list': 'copy', '_counter': len(copy_com)}, **row.copy())
            functional_c.append(temp)
    return functional_c
