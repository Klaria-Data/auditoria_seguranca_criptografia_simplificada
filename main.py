import hashlib

def GEN(seed: list[int]) -> list[int]:
    """
    Function responsible for generate the binary key.

    :param seed: list of integer that will be used as key.
    :return: a list of integer that will be used as key.
    """
    seed_str = "".join(map(str, seed))
    hash_obj = hashlib.sha256(seed_str.encode()).digest()
    key_len = 4 * len(seed)

    bits = []
    for byte in hash_obj:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    if len(bits) >= key_len:
        result = bits[:key_len]
    else:
        result = (bits * (key_len // len(bits) + 1))[:key_len]

    return result


def ENC(K: list[int], M: list[int]) -> list[int]:
    """
    Function responsible for encrypting the message.

    :param K: list of integer representing the key.
    :param M: list of integer representing the message.
    :return: a list of integer representing the cipher.
    """
    if len(K) != len(M):
        raise ValueError("K e M devem ter o mesmo tamanho (4 * len(seed)).")

    response = [k ^ m for k, m in zip(K, M)]
    return response


def DEC(K: list[int], C: list[int]) -> list[int]:
    """
    Function responsible for decrypting the message.

    :param K: list of integer representing the key.
    :param C: list of integer representing the cipher.
    :return: a list of integer representing the original message.
    """
    return [k ^ c for k, c in zip(K, C)]


def teste_difusao(seed_binaria, mensagem_original):
    K = GEN(seed_binaria)
    C1 = ENC(K, mensagem_original)

    mensagem_modificada = mensagem_original.copy()
    mensagem_modificada[0] ^= 1

    C2 = ENC(K, mensagem_modificada)
    bits_alterados = sum(b1 ^ b2 for b1, b2 in zip(C1, C2))
    return bits_alterados


def teste_confusao(seed_original, mensagem):
    K1 = GEN(seed_original)
    C1 = ENC(K1, mensagem)

    seed_modificada = seed_original.copy()
    seed_modificada[0] ^= 1

    K2 = GEN(seed_modificada)
    C2 = ENC(K2, mensagem)

    bits_alterados = sum(b1 ^ b2 for b1, b2 in zip(C1, C2))
    return bits_alterados


if __name__ == "__main__":
    seed_exemplo = [1, 1, 0, 1, 0]
    msg_exemplo = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

    chave = GEN(seed_exemplo)
    cifra = ENC(chave, msg_exemplo)
    original = DEC(chave, cifra)

    print(f"Seed Utilizada:    {seed_exemplo}")
    print(f"Mensagem Original: {msg_exemplo}")
    print(f"Cifra Gerada:      {cifra}")
    print(f"Descriptografado:  {original}")
    print(f"Teste Difusão: {teste_difusao(seed_exemplo, msg_exemplo)} bits alterados")
    print(f"Teste Confusão: {teste_confusao(seed_exemplo, msg_exemplo)} bits alterados")