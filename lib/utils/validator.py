import sys
from urllib.parse import urlparse


def validate_target(url):
    try:
        u = urlparse(url)
        if u.scheme and u.netloc:
            return u.geturl()
        else:
            raise ValueError('Url no valida, prueba con una Url válida')
    except ValueError as e:
        print(e)
        sys.exit(2)
