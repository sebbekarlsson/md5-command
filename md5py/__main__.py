import sys
import hashlib


def md5(fname):
	m = hashlib.md5()
	m.update(fname)
	print(m.hexdigest())

if (__name__) == '__main__':
	md5(sys.argv[1])
