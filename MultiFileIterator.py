from itertools.chain import from_iterator


class MultiFileIterator:

	def __init__(self, input_files):
		if isinstance( input_files, str):
			input_files = [input_files,]
		self.iterator = from_iterables(map( lambda x : open(x), input_files))

	def __iter__(self):
		return self.iterator

	def __next__(self):
		return next( self.iterator)


	def __enter__(self):
		return self.iterator

	def __exit__(self):
		return
