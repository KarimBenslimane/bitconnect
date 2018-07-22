from simplecrypt import encrypt, decrypt
import os


# @TODO Check if possible to use BCrypt with salts
# @TODO Check if possible to use MySQL instead of files > Future use of webinterface etc
def crypt_key(password, key):
    return encrypt(password, key.encode('utf8'))


def get_user_file_name(filename):
    return 'database/users/' + filename


def get_full_path_user(filename):
    return os.getcwd() + '/' + get_user_file_name(filename)


def get_full_path_bot(filename):
    return os.getcwd() + '/' + get_bot_file_name(filename)


def get_bot_file_name(filename):
    return 'database/bots/' + filename


def add_bot_to_file(filename, values):
    file_w = open(get_bot_file_name(filename), "a+")
    # TODO: format values to column like
    file_w.write(values)
    file_w.close()


def read_bot_file(filename):
    file_path = get_full_path_bot(filename)
    if os.path.exists(file_path):
        file_r = open(file_path, "r")
        lines = file_r.readlines()
        raw_values = lines
        # TODO: format values and return list
        return raw_values
    else:
        return []


def read_user_file(password, filename):
    file_path = get_full_path_user(filename)
    if os.path.exists(file_path):
        file_r = open(file_path, "r")
        lines = file_r.readlines()
        raw_values = dict()
        for line in lines:
            parts = line.split("///")
            exchange = parts[0]
            public = parts[1]
            private = parts[2].rstrip('\n')
            raw_values[exchange] = {}
            raw_values[parts[0]]['public'] = decrypt(password, public)
            raw_values[parts[0]]['private'] = decrypt(password, private)
        return raw_values
    else:
        return []


def add_exchange_to_user_file(password, filename, public_key, private_key, exchange):
    file_w = open(get_user_file_name(filename), "w+")
    message = exchange + "///" + crypt_key(password, public_key) + "///" + crypt_key(password, private_key) + "\n"
    file_w.write(message)
    file_w.close()


def remove_exchange_from_user_file(exchange, filename):
    file_path = get_full_path_user(filename)
    deleted = False
    if os.path.exists(file_path):
        file_r = open(file_path, "r")
        lines = file_r.readlines()
        file_r.close()
        file_w = open(file_path, "w")
        for line in lines:
            parts = line.split("...")
            print(parts[0])
            if parts[0] != exchange:
                file_w.write(line)
            else:
                deleted = True
        file_w.close()
    return deleted
