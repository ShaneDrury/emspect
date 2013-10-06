__author__ = 'srd1g10'

import unittest
from emspect.lib.io import LECFactory
import os


class IoTests(unittest.TestCase):
    def setUp(self):
        self.iwasaki32c_lec_file = os.path.join()

    def test_extract_lec_32c(self):
        g = LECFactory.extract_lec('myfile', 'Iwasaki32cLEC')
        lec = g.extract_lec('0.0042')

        self.failUnless(lec['F0'][0] == 0.1)