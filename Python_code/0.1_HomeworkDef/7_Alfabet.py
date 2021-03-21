import string

alphabet = string.ascii_lowercase
enter_string = input("Enter frase ")


def alfa(enter_string, alphabet):
    del_spase = enter_string.replace(' ', '')
    low_register = del_spase.lower()
    trans_to_list = [i for i in low_register]
    tarns_alph_to_list = [i for i in alphabet]
    set_trans = set(trans_to_list)
    if len(set_trans) == len(tarns_alph_to_list):
        return True
    else:
        return False


print(alfa(enter_string, alphabet))
