find all files under a directory that ends with a ".c"

Python's os module

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

cannot use os.walk()

Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
       [
        'path1',
        'path2'
        ...
       ]

     