import hashlib

def key_generation(seed:str) -> list[int]:
    """
    Function responsible for create a binary key, based on a seed received as parameter.
    This key generation has two rules:
        1 - The binary key generate, has to be created, based on the seed.
        2 - The binary key has to be 4 times bigger than the seed length.
    :param seed: message that will be used for create a binary key
    :return: a list of integer that contain the binary key based on the seed message.
    """
    # First we transform the seed message in bytes 'seed.encode()', after that sha256 generate a unique fingerprint
    # for the message of 256 bites and in the end we use digest() because will return the final result in bytes read for
    # be convert in binary.
    hash_obj = hashlib.sha256(seed.encode()).digest()
    key_len = 4 * len(seed)

    bits = []
    for bit in hash_obj:
        for i in range(7, -1, -1):
            bits.append(bit & (1 << i))

    return bits[:key_len] if len(bits) >= key_len else (bits * (key_len // len(bits) + 1))[:key_len]

if __name__ == '__main__':
    seed_example = 'teste'
    print(key_generation(seed_example))
