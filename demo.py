from ctypes import cdll

lib = cdll.LoadLibrary('./libadd.so')
print lib.add(1, 3)
