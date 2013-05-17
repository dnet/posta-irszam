Parser for Hungarian Post ZIP code listings
===========================================

The Hungarian Post (Magyar Posta) publishes ZIP codes in an Excel spreadsheet
on the [ZIP code lookup page of their homepage][1], and this library parses it
into a ZIP code -> city name tuples or dictionary.

generator module
----------------

The `generator` module has a `Generator` class, which can be instantiated with
a string parameter having the name of the XLS file. The following methods can
be used to parse the input.

   - `generate_items` is a generator and yields `(zip, city)` tuples
   - `generate_dict` returns a ZIP code -> city dictionary
   - `generate_pickled` saves such a dictionary into a [Pickle][2] file

The `generator` module can also be called from the command line with two
arguments, as it can be seen in the following example.

	$ python generator.py input.xls output.pickle

lookup module
-------------

The `lookup` modules has a `Lookup` class, which can be instantiated with a
string parameter having the name of a Pickle file generated by `Generator`.
The `get` method can be used to get the city name associated with a certain
ZIP code. The `lookup` module can also be called from the command line with
two arguments as it can be seen in the following example.

	$ python lookup.py test.pickle 4032
	Debrecen

License
-------

The whole project is available under MIT license.

Dependencies
------------

 - Python 2.x (tested on 2.7.3)
 - [xlrd][3] (Debian/Ubuntu package: `python-xlrd`)


  [1]: http://www.posta.hu/ugyfelszolgalat/iranyitoszam_kereso 
  [2]: http://docs.python.org/library/pickle.html
  [3]: http://www.python-excel.org/
