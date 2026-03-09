import ctypes
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(base_dir,"..","..", "lib", "libcore.so")

c_lib = ctypes.CDLL(lib_path)
