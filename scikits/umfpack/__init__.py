from info import __doc__

from umfpack import *

__all__ = filter(lambda s:not s.startswith('_'),dir())
try:
    from scipy.testing.pkgtester import Tester
except:
    from numpy.testing import Tester
test = Tester().test
