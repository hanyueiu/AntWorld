import re
import sys
from cryptography.fernet import Fernet
import base64
import os

def map_table():
    table = [
        ('A', '01'),
        ('B', '1000'), 
        ('C', '1010'), 
        ('D', '100'), 
        ('E', '0'), 
        ('F', '0010'), 
        ('G', '110'), 
        ('H', '0000'), 
        ('I', '00'), 
        ('J', '0111'), 
        ('K', '101'), 
        ('L', '0100'), 
        ('M', '11'), 
        ('N', '10'), 
        ('O', '111'), 
        ('P', '0110'), 
        ('Q', '1101'), 
        ('R', '010'), 
        ('S', '000'), 
        ('T', '1'), 
        ('U', '001'), 
        ('V', '0001'), 
        ('W', '011'), 
        ('X', '1001'), 
        ('Y', '1011'), 
        ('Z', '1100'), 

        ('0', '11111'), 
        ('1', '01111'), 
        ('2', '00111'), 
        ('3', '00011'), 
        ('4', '00001'), 
        ('5', '00000'), 
        ('6', '10000'), 
        ('7', '11000'), 
        ('8', '11100'), 
        ('9', '11110'), 

        ('.', '010101'), 
        (':', '111000'), 
        (',', '110011'), 
        (';', '101010'), 
        ('?', '001100'), 
        ('=', '10001'), 
        ("'", '011110'),
        ('/', '10010'), 
        ('!', '101011'), 
        ('-', '100001'), 
        ('_ ', '001101'), 
        ('"', '010010'), 
        ('(', '10110'), 
        (')', '101101'), 
        ('$', '0001001'), 
        ('&', '0000'), 
        ('@', '011010')
        ]
    return table


def get_salt(salt):
    if type(salt) == str:
        salt = salt + "".join(["yyh"]*11)
        salt = salt[:32]
        salt = base64.urlsafe_b64encode(salt.encode())
        return salt
    else:
        return salt
    

def encode(salt, pwd):
    password = Fernet(salt).encrypt(pwd.encode()).decode()
    return password


def decode(salt, pwd):
    password = Fernet(salt).decrypt(pwd.encode()).decode()
    return password


def get_file_data(file_path):
    with open(file_path, 'r') as f:
        file_data = f.read()
    return file_data


def set_file_data(file_path, data, mode='w'):
    with open(file_path, 'a') as f:
        f.write(data)


def file_to_encode(data, salt):
    data_list = data.split("\n")
    data_list = [_ for rl in data_list for _ in rl.split(" ") if _]
    table_dict = dict(map_table()[:-2])
    salt = get_salt(salt)
    new_infos = []
    for info in map(lambda info:encode(salt, info), data_list):
        ms = []
        for c in info:
            tmp = ''
            for _ in str(ord(c)):
                if _ in table_dict:
                    tmp += table_dict[_]
                else:
                    raise ValueError("value error")
            ms.append(tmp)
        new_infos.append(" ".join(ms) + " 0001100111")
    return " ".join(new_infos)


def file_to_decode(data, salt):
    data_list = [d for d in data.split(" ") if d]
    table_dict = [[t[1], t[0]] for t in map_table()[:-2]]
    table_dict = dict(table_dict)
    salt = get_salt(salt)
    infos = []
    tmp = []
    for info in data_list:
        if info != "0001100111":
            tmp.append(info)
        else:
            infos.append(tmp)
            tmp =[]
    new_infos = []
    for info in infos:
        tmp_list = []
        for cs in info:
            c_list = re.findall('.{5}', cs)
            tmp = ''
            for c in c_list:
                if len(c) != 5:
                    raise ValueError("value error")
                if c in table_dict:
                    tmp += table_dict[c]
            tmp_list.append(chr(int(tmp)))
        new_infos.append(decode(salt, ''.join(tmp_list)))
    name = new_infos[::3]
    user = new_infos[1:][::3]
    acc = new_infos[2:][::3]
    for n, u, a in zip(name, user, acc):
        print(n, u, a)


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        try:
            salt = input("input salt:")
            salt2 = input("input salt:")
            if salt2 != salt:
                print("Inconsistent ~")
                return
            data = get_file_data(path)

            if len(set(data)) == 3:
                file_to_decode(data, salt)
            else:
                new_path = os.path.join(os.path.dirname(path), 'out.txt')

                if os.path.exists(new_path):
                    print(new_path)
                    raise FileExistsError('file exist!')

                set_file_data(new_path, file_to_encode(data, salt))
            return 0
        except Exception as err:
            return  print(err)

sys.argv.append(r"D:\Amakers\II\out.txt")

main()