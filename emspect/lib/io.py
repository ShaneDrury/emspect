__author__ = 'srd1g10'
from emspect.lib.registered_types import RegisteredLECFormats


class LECFactory(object):
    @staticmethod
    def open(f, format_):
        types = RegisteredLECFormats.types
        return types[format_](f)