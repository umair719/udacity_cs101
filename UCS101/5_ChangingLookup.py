__author__ = 'Umair'


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None