__author__ = 'srd1g10'
from xml.dom import minidom
import pickle

from emspect.lib.register import registerLEC
from emspect.lib.registered_types import RegisteredLECFormats


class LECFactory(object):
    @staticmethod
    def open(f, format_):
        types = RegisteredLECFormats.types
        return types[format_](f)


class LECBase(object):
    def __init__(self, f):
        self.data = f


@registerLEC
class Iwasaki32cLEC(LECBase):
    lec_pos = {0: 'B0', 3: 'F0', 4: 'L64', 5: 'L85', 9: 'L4', 10: 'L5', 12: 'M_K_sq',
               15: 'lam_1', 16: 'lam_2'}  # Positions of LECs within file

    def extract_lec(self, to_search):
        xmldoc = minidom.parse(self.data)
        itemlist = xmldoc.getElementsByTagName('Ensembles')
        to_save = {}
        for i, s in enumerate(itemlist):
            if i not in self.lec_pos.keys():
                continue
            for ss, m in zip(s.getElementsByTagName('values'), s.getElementsByTagName('tag')):
                jl = [float(x) for x in ss.childNodes[0].nodeValue.split()]
                mass = m.childNodes[0].nodeValue
                if mass == to_search:
                    to_save[self.lec_pos[i]] = jl
        return to_save

    def pickle_lec(self, to_search, destination):
        lecs = self.extract_lec(to_search)
        with open(destination, 'wb') as f:
            pickle.dump(lecs, f)