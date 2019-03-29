class MultiFileIterator:

	def __init__(self, input_files):
		if isinstance( input_files, str):
			input_files = [input_files,]
		self.iterator = map( lambda x : open(x), input_files)
		self.input_files = input_files

	def __iter__(self):
		return self.iterator

	def __next__(self):
		return next( self.iterator)

	def __enter__(self):
		return self

	def __exit__(self, *args):
		return

	def read(self):
		return ''.join( it.read() for it in self.iterator)

	def readlines(self):
		return [lines for it in self.iterator for lines in it.readlines()]

	def reset(self):
		self.iterator = map( lambda x : open(x), self.input_files)
