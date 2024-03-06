import numpy as np
import re

def linear_search(word, voc):
    i = 0
    while i < len(voc):
        if voc[i] == word:
            return i
        i += 1


def bow_feature_extraction(filepath, voc):
    vect = np.zeros(len(voc))
    voc_set = set(voc)
    try:
        # open file and parse each individual word into lowercase and put them all in a list
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read().lower()  
            words = re.findall(r'\b\w+\b', content)

            for word in words:
                if word in voc_set:
                    vect[linear_search(word, voc)] += 1

    except IOError as e:
        print(f"Error reading file {filepath}: {e}")
    except UnicodeDecodeError as e:
        print(f"Encoding error in file {filepath}: {e}")
    return vect
