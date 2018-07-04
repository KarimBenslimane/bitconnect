from simplecrypt import encrypt, decrypt
import os


def get_file_name(filename):
    return 'database/' + filename


def read_file(password, filename):
    file_path = os.getcwd() + '/' + get_file_name(filename)
    if os.path.exists(file_path):
        file_r = open(file_path, "r")
        lines = file_r.readlines()
        raw_values = {}
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


def crypt_key(password, key):
    return encrypt(password, key.encode('utf8'))


def add_exchange_to_file(password, filename, exchange):
    file_w = open(get_file_name(filename), "w+")
    public_key = str(raw_input(
        "Please insert the public key address of " + exchange + ". Don't worry your keys will be stored encrypted."))
    private_key = str(raw_input("Please insert the private key address of " + exchange + "."))
    message = exchange + "///" + crypt_key(password, public_key) + "///" + crypt_key(password, private_key) + "\n"
    file_w.write(message)
    file_w.close()


def remove_exchange_from_file(exchange, filename):
    file_path = os.getcwd() + '/' + get_file_name(filename)
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
