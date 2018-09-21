#!C:\Program Files (x86)\Python37-32\python.exe

import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None
#if sys.platform == "win32":
  # base = "Win32GUI"

options = {
    'build_exe': {
		 'include_msvcr':True
    }
}   
   
   
setup(
    name = "PsiNorm.exe",
    version = "1.9.0",
    author="Bilal Bahadır Akbulut",
    description = "PsiNorm Persentil Hesaplayıcı",
    options = options,
    executables = [Executable("PsiNorm.py", icon="psiNormIcon.ico", base = base)])
