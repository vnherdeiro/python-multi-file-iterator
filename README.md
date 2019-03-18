# Multiple files iterator


- Provides a class extension of the iterator allowing iteration through a list of files while only opening one (in read-only mode) at the time

- Can be used as:
    
```python
    input_files = glob.glob('*.txt')
    input_files_iterator = MultiFileIterator( input_files)
    content = list(input_files_iterator)
```