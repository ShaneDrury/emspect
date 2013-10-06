__author__ = 'srd1g10'
from emspect.lib.registered_types import RegisteredLECFormats


def registerLEC(f):
    a = RegisteredLECFormats.types
    if f.__name__ not in a:  # Avoid duplicates
        a.update({f.__name__: f})
    return f