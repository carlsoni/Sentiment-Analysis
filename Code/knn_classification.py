import numpy as np

# respective distance calculations
def euclidean_distance(vec1, vec2):
    return np.sqrt(np.sum((vec1 - vec2) ** 2))

def manhattan_distance(vec1, vec2):
    return np.abs(sum(vec1 - vec2)) 

def cosine_distance(vec1, vec2):
    return 1 - np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def knn_classification(test_feat, train_label, train_feat, k, DstType):
    """
    k-Nearest Neighbor Classification.

    :param test_feat: Test feature vector.
    :param train_label: Training set ground truth label set.
    :param train_feat: Training set feature vector set.
    :param k: Hyperparameter k of KNN.
    :param DstType: Distance computation method.
    :return: Predicted label of the testing file.
    """
    
    distances = []
    
    # changes the didtance function based on the value passed to the finction allowing easy modification of hyper paramters
    distance_funcs = {1 : euclidean_distance, 2 : manhattan_distance, 3 : cosine_distance}
    if DstType not in distance_funcs:
        raise ValueError("Unsupported distance type")
    distance_func = distance_funcs[DstType]

    # iterates the 2D array and sents it off to the distance function for evaluation
    for i in range(len(train_feat)):
        dist = distance_func(test_feat, train_feat[i])
        distances.append((train_label[i], dist))

    # sort distances for ease pf access to the nearest neighbors
    distances.sort(key=lambda x : x[1])

    # sums the values and lets the neighbors vote
    neighbor_labels = [distances[i][0] for i in range(k)]
    predicted_label = max(set(neighbor_labels), key=neighbor_labels.count)
    
    return predicted_label

