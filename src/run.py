import os
import sys


wb_path = r'"C:\Program Files\ANSYS Inc\v192\Framework\bin\Win64\runwb2"'
script = 'script.wbjn'
cmdline = '{} -B -R {}'.format(wb_path, script)

try:
    os.system(cmdline)
except Exception:
    print('Failed to launch ANSYS Workbench!')
    sys.exit(0)




