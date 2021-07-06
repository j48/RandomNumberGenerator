import json
import secrets


def random_choice():
    return ''.join(secrets.choice('0123456789abcdef') for i in range(64))


def random_bits():
    return f'{secrets.randbits(256):064x}'


def random_below():
    return f'{secrets.randbelow(2**256):064x}'


random_functions = [random_choice, random_bits, random_below]

random_uint = secrets.choice(random_functions)()

with open(f'/iexec_out/computed.json', 'w+') as f:
    json.dump({"callback-data": f'0x{random_uint}'}, f)
