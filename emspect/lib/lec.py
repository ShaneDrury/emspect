__author__ = 'srd1g10'
from emspect.lib.register import registerLEC


class LECBase(object):
    def extract_lec(self, to_search):
        pass


@registerLEC
class Iwasaki32cLEC(LECBase):
    def extract_lec(self, to_search):
        pass