from pathlib import Path

FILES_PATH_TD = "dataset/TD/"
FILES_PATH_SLI = "dataset/SLI/"
SPEAKER_ID_CHILD = "*CHI"
START_SPEAKER_OR_INFO_LINE = "*%@"
WORD_PREFIX = "&+"
SYMBOLS_LIST = "[//][/][*]"
SLI_PATH_OUTPUT = "SLI_cleaned"
TD_PATH_OUTPUT = "TD_cleaned"

list_of_files = list()

def add_paths_to_list(paths):
    for path in paths:
        list_of_files.append(str(path))

def filter_string(sentence):
    words = sentence.split(" ")
    temp = ""
    words.pop(0)
    for word in words:
        if word.startswith("[") and word in SYMBOLS_LIST:
            temp += " " + word
        elif word.startswith("<"):
            temp += " " + word[1:]
        elif "(" in word and word[1] is not ".":
            temp_word = word
            temp_word = word.replace("(", "")
            temp_word = temp_word.replace(")", "")
            temp += " " + temp_word
        elif word[0] not in WORD_PREFIX and word.endswith(">"):
            temp +=  " " + word[:-1]
        elif word[0] not in WORD_PREFIX and not word.startswith("["):
            temp += " " + word

    if temp is not ".":
        return temp.strip("\n")

def read_data_from_file(path):
    temp_list = list()
    content_file = open(path, 'r')
    child_speaker = False
    temp_line = ""

    for line in content_file:
        if SPEAKER_ID_CHILD in line:
            temp_line += line[:-1]
            child_speaker = True
        elif child_speaker and line[0] not in START_SPEAKER_OR_INFO_LINE:
            temp_line += " " + line[1:]
            child_speaker = False
        else:
            child_speaker = False
            if temp_line:
                temp_list.append(filter_string(temp_line))
                temp_line = ""

    content_file.close()
    return temp_list

def get_all_files():
    pathlist_TD = Path(FILES_PATH_TD).glob('TD-*.txt')
    pathlist_SLI  = Path(FILES_PATH_SLI).glob('SLI-*.txt')

    add_paths_to_list(pathlist_TD)
    add_paths_to_list(pathlist_SLI)

def handle_output(output_path):
        output_handle = open(output_path, 'w')
        output_handle.write("\n".join(list_test))
        output_handle.close()

get_all_files()

td_dir_cleaned = Path(TD_PATH_OUTPUT)
sli_dir_cleaned = Path(SLI_PATH_OUTPUT)
td_dir_cleaned.mkdir(exist_ok=True, parents=True)
sli_dir_cleaned.mkdir(exist_ok=True, parents=True)

for full_path in list_of_files:
    list_test = read_data_from_file(full_path)

    if "TD" in full_path:
        output_path = TD_PATH_OUTPUT+"/"+str(full_path.split("/")[2:]).strip('[\'\']')
        handle_output(output_path)
    else:
        output_path = SLI_PATH_OUTPUT+"/"+str(full_path.split("/")[2:]).strip('[\'\']')
        handle_output(output_path)
