import os
import re

def build_voc(stop_words, folder):
    voc = set()
    # Sets the stop words to all lower case to avoid duplicates
    stop_words = set(word.lower() for word in stop_words)

    # Loop through all the files in the folder that end with .txt
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder, filename)

            try:
                # open file and parse each individual word into lowercase and put them all in a list
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read().lower()  
                    words = re.findall(r'\b\w+\b', content)


                    # loops the words list and adds them to a set if they are not in the stop words
                    for word in words:
                        if word not in stop_words:
                            voc.add(word)
            except IOError as e:
                print(f"Error reading file {filename}: {e}")
            except UnicodeDecodeError as e:
                print(f"Encoding error in file {filename}: {e}")
    return list(voc)



