

import csv
import math

# Load CSV
def load_csv(filename):
    with open(filename, 'r') as f:
        data = list(csv.reader(f))
    header = data.pop(0)
    return data, header


# Calculate entropy
def entropy(data):
    labels = [row[-1] for row in data]
    unique = set(labels)

    if len(unique) == 1:
        return 0

    ent = 0
    for val in unique:
        p = labels.count(val) / len(labels)
        ent -= p * math.log2(p)

    return ent


# Split data based on attribute
def split_data(data, index):
    splits = {}

    for row in data:
        key = row[index]
        splits.setdefault(key, []).append(row)

    return splits


# Choose best attribute to split
def best_attribute(data):
    base_entropy = entropy(data)
    n = len(data[0]) - 1

    best_gain = -1
    best_attr = -1

    for i in range(n):
        splits = split_data(data, i)

        new_entropy = sum(
            (len(sub) / len(data)) * entropy(sub)
            for sub in splits.values()
        )

        gain = base_entropy - new_entropy

        if gain > best_gain:
            best_gain = gain
            best_attr = i

    return best_attr


# Build decision tree
def build_tree(data, features):

    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not features:
        return max(set(labels), key=labels.count)

    idx = best_attribute(data)
    attr = features[idx]

    tree = {attr: {}}

    splits = split_data(data, idx)

    new_features = features[:idx] + features[idx+1:]

    for val, subset in splits.items():
        reduced_subset = [row[:idx] + row[idx+1:] for row in subset]
        tree[attr][val] = build_tree(reduced_subset, new_features)

    return tree


# Print the tree
def print_tree(tree, indent=""):

    if isinstance(tree, str):
        print(indent + "->", tree)

    else:
        for attr, branches in tree.items():
            for val, subtree in branches.items():
                print(f"{indent}{attr} = {val}")
                print_tree(subtree, indent + "  ")


# Main
data, features = load_csv("data3.csv")

tree = build_tree(data, features)

print("Decision Tree:")
print_tree(tree)