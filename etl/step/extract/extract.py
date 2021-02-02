from os import listdir, path

def corpus_subdirs(path):
    """ pathの中のdir(txt以外)をlistにして返す """
    subdirs = []
    for x in listdir(path):
        if not x.endswith('.txt'):
            subdirs.append(x)
    return subdirs

def corpus_filenames(path):
    """ pathの中のファイルをlistにして返す """
    labels = []  # *.txt
    for y in listdir(path):
        if not y.startswith('LICENSE'):
            labels.append(y)
    return labels