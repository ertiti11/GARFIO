import os.path
from enum import IntEnum

import yaml


class Risk(IntEnum):
    """
    Enumeración del riesgo de los complementos
    0 NO_DANGER Casi sin riesgo de ser detectado
    1 NOISY Genera muchas solicitudes y patrones que pueden detectarse
    2 PELIGROSO Realiza una etapa de explotación y puede ser potencialmente dañino para el objetivo
    """
    NO_DANGER = 0
    NOISY = 1
    DANGEROUS = 2


class Settings(object):
    cfg = {}

    _setters = ['risk', 'dns_resolver', 'datastore']

    def __getattr__(self, item):
        return Settings.cfg[item]

    def __setattr__(self, key, value):
        if key in Settings._setters:
            Settings.cfg[key] = value
        else:
            raise NameError("No puede redefinir el valor de% s dinámicamente\nPor favor use el archivo de configuración" % key)

    @classmethod
    def from_yaml(cls, filepath):
        """
        
        Genere el diccionario de configuración a partir del archivo yaml
        : param filepath: ruta del archivo de configuración
        : return: Ninguno
        """
        # Check if the filepath provided exists
        if not os.path.isfile(filepath):
            raise FileNotFoundError("Ruta no válida para el archivo de configuración")

        # Parse the configuration and merge it in dict
        with open(filepath, 'r') as yamlfile:
            try:
                # Getting config from the file
                config = yaml.load(yamlfile, Loader=yaml.SafeLoader)
                # Merging the dictionaries and getting result
                cls.cfg = {**cls.cfg, **config}
            except yaml.YAMLError as e:
                print(e)
