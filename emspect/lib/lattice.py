__author__ = 'srd1g10'

from pyontdd.lib.lattice import Lattice24c, Lattice32c


class Iwasaki24c(Lattice24c):
    pass


class Iwasaki32c(Lattice32c):
    pass


class IwasakiDSDR32c(Lattice32c):
    lattice_size = {"x": 32, "y": 32, "z": 32, "t": 64, "s": 32}
    a_inv = 1.37
    a_inv_err = 0.01
    Z = None # Undefined