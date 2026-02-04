import hashlib

def GEN(seed: str) -> list[int]:
    """
    Função responsável por criar uma chave binária baseada em uma semente.
    Regras:
    1. Baseada na seed.
    2. Tamanho deve ser 4 vezes o comprimento da seed.
    """

    hash_obj = hashlib.sha256(seed.encode()).digest()
    key_len = 4 * len(seed)

    bits = []
    for byte in hash_obj:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    return bits[:key_len] if len(bits) >= key_len else (bits * (key_len // len(bits) + 1))[:key_len]


def ENC(K: list[int], M: list[int]) -> list[int]:
    """
    Realiza a criptografia da mensagem M usando a chave K através de XOR.
    """
    if len(K) != len(M):
        raise ValueError("K e M devem ter o mesmo tamanho (4 * len(seed)).")

    return [k ^ m for k, m in zip(K, M)]


def DEC(K: list[int], C: list[int]) -> list[int]:
    """
    Realiza a descriptografia retornando a mensagem original m.
    """
    # O XOR é a sua própria inversa
    return [k ^ c for k, c in zip(K, C)]


def teste_difusao(seed, mensagem_original):
    """Mede quantos bits mudam na cifra ao alterar 1 bit da mensagem."""
    K = key_key_generationeration(seed)
    C1 = ENC(K, mensagem_original)

    mensagem_modificada = mensagem_original.copy()
    mensagem_modificada[0] ^= 1

    C2 = ENC(K, mensagem_modificada)
    bits_alterados = sum(b1 ^ b2 for b1, b2 in zip(C1, C2))
    return bits_alterados


def teste_confusao(seed_original, mensagem):
    """Mede quantos bits mudam na cifra ao alterar 1 bit da seed."""
    K1 = key_key_generationeration(seed_original)
    C1 = ENC(K1, mensagem)

    seed_modificada = seed_original[:-1] + (chr(ord(seed_original[-1]) + 1))
    K2 = key_key_generationeration(seed_modificada)
    C2 = ENC(K2, mensagem)

    bits_alterados = sum(b1 ^ b2 for b1, b2 in zip(C1, C2))
    return bits_alterados


if __name__ == "__main__":
    seed_exemplo = "fadec"
    msg_exemplo = [1, 0, 1, 0, 1] * 4

    chave = GEN(seed_exemplo)
    cifra = ENC(chave, msg_exemplo)
    original = DEC(chave, cifra)

    print(f"Mensagem Original: {msg_exemplo}")
    print(f"Cifra Gerada:      {cifra}")
    print(f"Descriptografado:  {original}")
    print(f"Teste Difusão: {teste_difusao(seed_exemplo, msg_exemplo)} bits alterados")
    print(f"Teste Confusão: {teste_confusao(seed_exemplo, msg_exemplo)} bits alterados")