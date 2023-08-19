# https://py.checkio.org/en/mission/remove-accents/

import unicodedata

def checkio(s):
    nfkd_form = unicodedata.normalize('NFKD', s)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio(u"loài trăn lớn"))
    print(checkio(u"préfèrent"))
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
