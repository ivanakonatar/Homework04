#crypt-decrypt

def encrypt(recenica):


    nova_recenica = ''

    for karakter in recenica:
        broj_chr = ord(karakter)

        broj_kriptovanog_slova = broj_chr * 2
        karakter = chr(broj_kriptovanog_slova)

        nova_recenica += karakter

    return nova_recenica


def decrypt(nova_recenica):

    word = ''
    for karakt in nova_recenica:
        broj = chr(ord(karakt) // 2)
        word += broj
    return word


if __name__ == "__main__":

    recenica = encrypt("Ivana KOnatar 17/115")
    print(recenica)

    word = decrypt(recenica)
    print(word)
