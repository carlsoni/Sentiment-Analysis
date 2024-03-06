
# creates the dictionary for sentimental values 
def build_sentimental_dict(filename):
    sentimental_dict = {}
    try:
        # open file and parse each individual word into lowercase and put them all in a list
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            content = content.split()
            # iteraye through the content of the file setting each key as a word and each vale as the words sentimental value
            i = 1
            while i < len(content):
                sentimental_dict[content[i-1]] = float(content[i])
                i += 2
    # error checking
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
    except UnicodeDecodeError as e:
        print(f"Encoding error in file {filename}: {e}")
    return sentimental_dict

def sentimentalAnalysis(filename, sentimental_dict):
    score = 0
    try: 
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            content = content.split()

            # sums the score of each value at the location of each word within the dict
            for word in content:
                if word in sentimental_dict:
                    score += sentimental_dict[word]

    except IOError as e:
        print(f"Error reading file {filename}: {e}")
    except UnicodeDecodeError as e:
        print(f"Encoding error in file {filename}: {e}")
    return score
    