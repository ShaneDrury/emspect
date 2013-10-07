__author__ = 'srd1g10'

import unittest
import os
import pickle

from emspect.lib.lec import LECFactory


class IoTests(unittest.TestCase):
    def setUp(self):
        self.iwasaki32c_lec_file = os.path.join('testfiles', 'result_LECs_physmh_physunits_ChPTFV.xml')
        self.pickled_lec_file = os.path.join('testfiles', 'lec.pickle')

    def tearDown(self):
        if os.path.exists(self.pickled_lec_file):
            os.remove(self.pickled_lec_file)

    def test_extract_lec_32c(self):
        g = LECFactory.open(self.iwasaki32c_lec_file, 'Iwasaki32cLEC')
        lec = g.extract_lec('32ID_0.0042')
        self.failUnless(lec['F0'][0] == 0.119392183648112)
        self.failIf(lec['F0'][0] == 999)

    def test_write_lec_to_file(self):
        g = LECFactory.open(self.iwasaki32c_lec_file, 'Iwasaki32cLEC')
        g.pickle_lec('32ID_0.0042', self.pickled_lec_file)
        with open(self.pickled_lec_file, 'rb') as f:
            lec = pickle.load(f)
        self.failUnless(lec['F0'][0] == 0.119392183648112)
        self.failIf(lec['F0'][0] == 999)

