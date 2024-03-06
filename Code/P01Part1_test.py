import os
import numpy as np
import build_voc as bv
import bow_feature_extraction as bfe
import knn_classification as kc

def read_files_from_folder(folder):
    """
    Read all text files in the given folder and return their paths.

    :param folder: Path to the folder.
    :return: A list of file paths.
    """
    return [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.txt')]

def main():
    pos_folder = '/Users/ianexclam/Desktop/CSE 408/HW3/Data/pos'#'../Data/pos'
    neg_folder = '/Users/ianexclam/Desktop/CSE 408/HW3/Data/neg'#'../Data/neg'

    stopwords = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'at', 'for', 'with', 'without', 'of', 'to', 'from', 'by', 'i', 'was', 'were'}

    voc = bv.build_voc(stopwords, pos_folder)
    voc += bv.build_voc(stopwords, neg_folder)  # Concatenate vocabularies
    voc = list(set(voc))  # Remove duplicates

    # Extract features and labels
    feat = []
    label = []

    # Process positive reviews
    for file in os.listdir(pos_folder):
        if file.endswith('.txt'):
            filepath = os.path.join(pos_folder, file)
            feat_vec = bfe.bow_feature_extraction(filepath, voc)
            feat.append(feat_vec)
            label.append(1)

    # Process negative reviews
    for file in os.listdir(neg_folder):
        if file.endswith('.txt'):
            filepath = os.path.join(neg_folder, file)
            feat_vec = bfe.bow_feature_extraction(filepath, voc)
            feat.append(feat_vec)
            label.append(0)

    # Convert to numpy arrays for easier manipulation
    feat = np.array(feat)
    label = np.array(label)
    
    # KNN Classification
    correct_ct = 0
    DistType = 3  # Different distance type (assuming this is handled in your knn_classification function)
    K = 17  # Different K values
    for ii in range(label.size):
        train_feat = np.delete(feat, ii, axis=0)
        train_label = np.delete(label, ii)

        pred_label = kc.knn_classification(feat[ii], train_label, train_feat, K, DistType)
        if pred_label == label[ii]:
            correct_ct += 1

    accuracy = correct_ct / label.size
    print("Accuracy:", accuracy)
    

if __name__ == "__main__":
    main()
