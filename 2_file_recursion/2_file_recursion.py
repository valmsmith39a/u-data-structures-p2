import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    isDir = os.path.isdir(path)
    found_items = []
    if isDir:
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            isDir = os.path.isdir(item_path)
            if isDir:
                found_items += find_files(suffix, item_path)
            else:
                if item.endswith(suffix):
                    found_items.append(item_path)
    else:
        isFile = os.path.isfile(path)
        if isFile:
            if path.endswith(suffix):
                found_items.append(path)

    return found_items


print("--- Test 1 ---")
suffix = ".c"
path = "./"
print(find_files(suffix, path))
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print("--- Test 2 ---")
suffix = ".h"
path = "./testdir"
print(find_files(suffix, path))
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']

print("--- Test 3 ---")
suffix = ".txt"
path = "./"
print(find_files(suffix, path))
# []
