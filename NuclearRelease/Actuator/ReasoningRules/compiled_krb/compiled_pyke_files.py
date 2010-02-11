# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.0.4'

compiler_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

targets = target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
    ('ReasoningRules', 'testcase2.krb'): [1265218532.426867, 'testcase2_fc.py'],
    ('ReasoningRules', 'testcase.krb'): [1264804932.9155619, 'testcase_fc.py'],
  },
  compiler_version)
