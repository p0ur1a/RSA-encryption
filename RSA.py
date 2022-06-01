from sympy import randprime, gcd
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def variables():
    p, q = 0, 0

    while q == p:
        p, q = [randprime(100, 200) for x in range(2)]

    z = (p - 1) * (q - 1)
    n = p * q

    d = 2
    while gcd(d, z) != 1:
        d += 1

    i = 1
    while True:
        e = ((z * i) + 1)/d

        if e.is_integer():
            e = int(e)
            break

        i += 1

    # print('q = {}, p = {}, z = {}, n = {}, d = {}, e = {}'.format(q, p, z, n, d, e))

    return n, d, e


def encrypt(public_key: int, n: int):

    message = read_from_file()

    encrypted_message = ''
    for c in message:
        enc = (ord(c) ** public_key) % n
        encrypted_message += (str(enc) + ' ')

    write_to_file(encrypted_message, 'encrypted.txt')


def decrypt(private_key: int, n: int):

    encrypted_message = read_from_file()
    encrypted_message = encrypted_message.split()
    encrypted_message = list(map(int, encrypted_message))

    original_message = ''
    for enc in encrypted_message:
        dec = (enc ** private_key) % n
        original_message += str(chr(dec))

    write_to_file(original_message, 'decrypted.txt')


def read_from_file():

    root = Tk()
    root.attributes('-alpha', 0.01)
    root.attributes('-topmost', True)
    root.tk.eval(f'tk::PlaceWindow {root._w} center')
    root.withdraw()

    filename = askopenfilename()
    root.destroy()

    with open(filename, 'r', encoding='utf-8') as f:
        message = f.read()

    return message


def write_to_file(message: str, filename: str):

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(message)


n, private_key, public_key = variables()

while True:
    command = int(input('enter command\n1-encrypt\n2-decrypt\n'))

    if command == 1:
        encrypt(public_key, n)

    elif command == 2:
        decrypt(private_key, n)
