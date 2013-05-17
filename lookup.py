#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import with_statement, print_function
import pickle

class Lookup(object):
	def __init__(self, pickle_filename):
		with file(pickle_filename, 'rb') as jar:
			self.lut = pickle.load(jar)

	def get(self, irsz):
		return self.lut[irsz]


def main():
	import sys
	try:
		input_file, irsz = sys.argv[1:]
		irsz = int(irsz)
	except ValueError:
		print('Usage: {0} input.pickle <irsz>'.format(sys.argv[0]), file=sys.stderr)
		raise SystemExit(1)
	else:
		lup = Lookup(input_file)
		print(lup.get(irsz))


if __name__ == '__main__':
	main()
