# Dataset with mapping numbers

class DatasetNumber(object):

    static_unity_mapping = {
        0: '',
        1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis',
        7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze',
        13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis',
        17: 'dezessete', 18: 'dezoito', 19: 'dezenove'
    }

    static_ten_mapping = {
        0: '', 1: '',
        2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta',
        7: 'setenta', 8: 'oitenta', 9: 'noventa'
    }

    static_hundred_mapping = {
        0: '',
        1: 'cem', 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos', 5: 'quinhentos',
        6: 'seiscentos', 7: 'setecentos', 8: 'oitocentos', 9: 'novezentos'
    }


def special_join(*args):
    '''
    When there is text, the function joins the text and adds the letter "e".

    :param args: list with snippets text
    :return: a string with join array text
    '''
    return ' e '.join(filter(bool, args))