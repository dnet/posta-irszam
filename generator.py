#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import with_statement, print_function
from xlrd import open_workbook, XL_CELL_NUMBER
from itertools import imap
import re, pickle

CITY_NAME_RE = re.compile(r'(Bp\.|[^ ]+ )u\.')

class Generator(object):
	def __init__(self, excel_filename):
		self.book = open_workbook(excel_filename)

	def generate_pickled(self, filename):
		output = self.generate_dict()
		with file(filename, 'wb') as jar:
			pickle.dump(output, jar, protocol=pickle.HIGHEST_PROTOCOL)

	def generate_dict(self):
		return dict(self.generate_items())
	
	def generate_items(self):
		for sheet in self.book.sheets():
			if sheet.name == u'Települések':
				for row in imap(sheet.row, xrange(sheet.nrows)):
					irsz = row[0]
					if irsz.ctype != XL_CELL_NUMBER:
						continue
					yield int(irsz.value), row[1].value
			else:
				match = CITY_NAME_RE.match(sheet.name)
				if not match:
					continue
				city = match.group(1).strip() if match.group(1) != 'Bp.' else 'Budapest'
				for row in imap(sheet.row, xrange(sheet.nrows)):
					irsz = row[0]
					if irsz.ctype != XL_CELL_NUMBER:
						continue
					yield int(irsz.value), city


def main():
	import sys
	try:
		input_file, output_file = sys.argv[1:]
	except ValueError:
		print('Usage: {0} input.xls output.pickle'.format(sys.argv[0]), file=sys.stderr)
		raise SystemExit(1)
	else:
		gen = Generator(input_file)
		gen.generate_pickled(output_file)


if __name__ == '__main__':
	main()
