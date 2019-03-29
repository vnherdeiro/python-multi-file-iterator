from base64 import b64encode
from os import urandom
import unittest
from unittest.mock import patch
from MultiFileIterator import MultiFileIterator 
from io import StringIO

# generates random content mocking file content
def genRandomFileContent(n_lines=100, line_length=64):
	genLine = lambda : b64encode(urandom(line_length)).decode('utf-8')
	return '\n'.join( genLine() for _ in range(line_length))

n_files = 5
filenames = ['dumbfile_%d' %(file_index+1) for file_index in range(n_files)]
filecontent = [genRandomFileContent() for _ in range(n_files)]

def FakeFileOpen():
	for content in filecontent:
		yield StringIO(content)

class Test_MultiFileIterator( unittest.TestCase):

	@patch("builtins.open", side_effect=FakeFileOpen()) #mocking the user keyboard input when asked to pick a feed
	def test_read(self, *args, **kwargs):
		iterator = MultiFileIterator( filenames)
		self.assertEqual( iterator.read(), ''.join(filecontent))

	@patch("builtins.open", side_effect=FakeFileOpen()) #mocking the user keyboard input when asked to pick a feed
	def test_readlines(self, *args, **kwargs):
		iterator = MultiFileIterator( filenames)
		file_lines = [content.splitlines(True) for content in filecontent]
		self.assertEqual( iterator.readlines(), [line for lines in file_lines for line in lines])

if __name__ == '__main__':
	unittest.main()