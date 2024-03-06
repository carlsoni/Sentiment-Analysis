import os
import sentimentalAnalysis as sa


posFolder = '/Users/ianexclam/Desktop/CSE 408/HW3/Data/pos'#'../Data/pos'
negFolder = '/Users/ianexclam/Desktop/CSE 408/HW3/Data/neg'#'../Data/neg'

# added new file path to wordwithStregth.txt and dict is made in this file for effecency 
words_strength_path = '/Users/ianexclam/Desktop/CSE 408/HW3/Data/wordwithStrength.txt'#'../Data/wordwithStrength.txt
setimental_dict = sa.build_sentimental_dict(words_strength_path)
# Process positive files
files = os.listdir(posFolder)
for file in files:
    if file.endswith('.txt'):
        sent_score = sa.sentimentalAnalysis(os.path.join(posFolder, file), setimental_dict)
        print(file)
        print(f"Groundtruth: Positive, sentimental score: {sent_score}")

# Process negative files
files = os.listdir(negFolder)
for file in files:
    if file.endswith('.txt'):
        sent_score = sa.sentimentalAnalysis(os.path.join(negFolder, file), setimental_dict)
        print(file)
        print(f"Groundtruth: Negative, sentimental score: {sent_score}")
