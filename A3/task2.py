from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILES_PATH_TD = "TD_cleaned"
FILES_PATH_SLI = "SLI_cleaned"
RETRACTING_SIGN = '[//]'
REPETITION_SIGN = '[/]'
GRAMMAR_ERROR_SIGN = '[*]'
PAUSES_SIGNS = ['(.)','(..)','(...)']
ALL_SIGNS = "'(.)(..)(...)[*][/][//],"
END_OF_STATEMENT = '.!?'
COLUMN_DATAFRAME_LIST = ['statements', 'unique words', 'repetition', 'retracting', 'errors', 'pauses']
Y_LABEL_LIST = [20, 40, 60, 80, 100, 120, 140, 160, 180]

list_of_files = list()

data_sli_temp = np.empty
data_td_temp = np.empty

def analyze_content(path):
    number_of_statements = 0
    unique_words = list()
    number_of_repetition = 0
    number_of_rectractions = 0
    grammar_errors = 0
    number_of_pauses = 0

    content_file = open(path, 'r')
    for line in content_file:
        strippedLine = line.strip("\n")
        words = line.split(" ")
        if strippedLine[-1:] in END_OF_STATEMENT:
            number_of_statements += 1
        for word in words:
            if word not in unique_words and word not in ALL_SIGNS:
                unique_words.append(word)
            if word in PAUSES_SIGNS:
                number_of_pauses += 1
        if REPETITION_SIGN in line:
            number_of_repetition += 1
        if RETRACTING_SIGN in line:
            number_of_rectractions += 1
        if GRAMMAR_ERROR_SIGN in line:
            grammar_errors += 1
    temp_arr = np.array([number_of_statements, len(unique_words), number_of_repetition, number_of_rectractions, grammar_errors, number_of_pauses])
    return temp_arr

def create_table(data_list, filenames):
    df = pd.DataFrame(data=data_list, columns=COLUMN_DATAFRAME_LIST, index=filenames)
    print(df)

def add_paths_to_list(paths):
    something = 1
    for path in paths:
        list_of_files.append(str(path))

def get_all_files():
    pathlist_TD = Path(FILES_PATH_TD).glob('TD-*.txt')
    pathlist_SLI  = Path(FILES_PATH_SLI).glob('SLI-*.txt')
    add_paths_to_list(pathlist_TD)
    add_paths_to_list(pathlist_SLI)

def present_bar_chart_files(data, names):
    x1 = [0,10,20,30,40,50,60,70,80,90,100]
    x2 = [1,11,21,31,41,51,61,71,81,91,101]
    x3 = [2,12,22,32,42,52,62,72,82,92,102]
    x4 = [3,13,23,33,43,53,63,73,83,93,103]
    x5 = [4,14,24,34,44,54,64,74,84,94,104]
    x6 = [5,15,25,35,45,55,65,75,85,95,105]

    plt.bar(x1, data[:,[0]].flatten(), label='statements')
    plt.bar(x2, data[:,[1]].flatten(), label='unique words')
    plt.bar(x3, data[:,[2]].flatten(), label='repetition')
    plt.bar(x4, data[:,[3]].flatten(), label='retraction')
    plt.bar(x5, data[:,[4]].flatten(), label='errors')
    plt.bar(x6, data[:,[5]].flatten(), label='pauses')
    plt.xticks(x1, names)
    plt.legend()
    plt.show()

def present_bar_chart_avg(avg_sli, avg_td):
    x = [[0,10], [1,11], [2,12], [3,13], [4,14], [5,15]]
    labels = ['statements', 'unique words', 'repetition',
        'retraction', 'errors', 'pauses']

    for i, v in enumerate(avg_sli):
        x_axis = 'x'+str(i+1)
        plt.bar(x[i], [avg_sli[i], avg_td[i]], label=labels[i])

    plt.xticks([2,12], ["SLI" , "TD"])
    plt.legend()
    plt.show()

get_all_files()

sli_file_names = list()
td_file_names = list()
for path in list_of_files:
    filename = str(path.split("/")[-1:]).strip("['.txt']")
    if "SLI" in path:
        sli_file_names.append(filename)
        data_sli_temp = np.append(data_sli_temp, analyze_content(path))
    else:
        td_file_names.append(filename)
        data_td_temp = np.append(data_td_temp, analyze_content(path))

sli_file_names.append("Average")
td_file_names.append("Average")

data_sli = np.delete(data_sli_temp, 0)
data_sli = np.reshape(data_sli, (10, 6))
sli_means = np.average(data_sli, axis=0)
data_sli = np.append(data_sli, sli_means)
data_sli = np.reshape(data_sli, (11, 6))

data_td = np.delete(data_td_temp, 0)
data_td = np.reshape(data_td, (10, 6))
td_means = np.average(data_sli, axis=0)
data_td = np.append(data_td, td_means)
data_td = np.reshape(data_td, (11, 6))

print("SLI frame")
create_table(data_sli, sli_file_names)
print("TD frame")
create_table(data_td, td_file_names)

present_bar_chart_files(data_sli, sli_file_names)
present_bar_chart_files(data_td, td_file_names)
present_bar_chart_avg(data_sli[-1:].flatten(), data_td[-1:].flatten())
