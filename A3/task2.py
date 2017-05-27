from pathlib import Path
import pandas as pd
import numpy as np

FILES_PATH_TD = "TD_cleaned"
FILES_PATH_SLI = "SLI_cleaned/"

list_of_files = list()

def analyze_content():
    for path in list_of_files:
        content_file = open(path, 'r')
        for line in content_file.read():
            pass

def add_paths_to_list(paths):
    something = 1
    for path in paths:
        list_of_files.append(str(path))

def get_all_files():
    pathlist_TD = Path(FILES_PATH_TD).glob('TD-*.txt')
    pathlist_SLI  = Path(FILES_PATH_SLI).glob('SLI-*.txt')
    add_paths_to_list(pathlist_TD)
    add_paths_to_list(pathlist_SLI)
    analyze_content()

get_all_files()
print("\n".join(list_of_files))
SLI-data = np.array([1,2,3,4])
print(str(SLI-data))
