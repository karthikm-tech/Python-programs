#1. pip install scikit-learn 2. python -m pip install scikit-learn
# Import necessary modules from scikit-learn and other libraries
from sklearn.datasets import load_iris        # For loading the Iris dataset
from sklearn.linear_model import LogisticRegression   # For implementing Logistic Regression
from sklearn.model_selection import train_test_split  # For splitting the dataset into training and testing
from sklearn.metrics import accuracy_score    # For evaluating model accuracy
from sklearn.cluster import KMeans            # For implementing KMeans clustering (Unsupervised Learning)

from sklearn.semi_supervised import SelfTrainingClassifier  # For Semi-supervised learning
import numpy as np                            # For handling numerical operations
import random                                 # For generating random numbers (used in Reinforcement Learning)

# Load the Iris dataset (a commonly used dataset in machine learning)
iris = load_iris()

X = iris.data        # Features (sepal and petal length, width)
y = iris.target      # Target labels (species of Iris)

# Split the dataset into training and testing subsets (70% for training, 30% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --------------------------------------------------------------------
# 1. Supervised Learning (Logistic Regression)
# --------------------------------------------------------------------

model_supervised = LogisticRegression(max_iter=200)   # Create logistic regression model with 200 iterations
model_supervised.fit(X_train, y_train)                # Train the model on the training data

y_pred = model_supervised.predict(X_test)             # Predict the labels for the test data

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Supervised Learning (Logistic Regression) Accuracy:", round(accuracy,2))


# --------------------------------------------------------------------
# 2. Unsupervised Learning (KMeans Clustering)
# --------------------------------------------------------------------

kmeans = KMeans(n_clusters=3, random_state=42)    # Create a KMeans model with 3 clusters
kmeans.fit(X_train)                               # Fit the model

cluster_labels = kmeans.predict(X_test)           # Predict cluster labels for the test set

# Function to map predicted cluster labels to true class labels using majority voting
def map_clusters(true_labels, cluster_labels):
    mapped = np.zeros_like(cluster_labels)
    for i in np.unique(cluster_labels):
        mask = cluster_labels == i
        mapped[mask] = np.bincount(true_labels[mask]).argmax()
    return mapped

mapped_labels = map_clusters(y_test, cluster_labels)

# Calculate and print approximate accuracy
accuracy_unsup = accuracy_score(y_test, mapped_labels)
print("Unsupervised Learning (KMeans Clustering) Accuracy (approx):", round(accuracy_unsup,2))


# --------------------------------------------------------------------
# 3. Semi-supervised Learning (SelfTrainingClassifier with Logistic Regression)
# --------------------------------------------------------------------

y_semi = np.copy(y_train)   # Copy the training labels

# Mask most of the labels to simulate a semi-supervised scenario
y_semi[30:] = -1

semi_model = SelfTrainingClassifier(LogisticRegression(max_iter=200))

# Train the semi-supervised model on the training data with masked labels
semi_model.fit(X_train, y_semi)

y_pred_semi = semi_model.predict(X_test)   # Predict the labels for the test data

# Calculate and print the accuracy
accuracy_semi = accuracy_score(y_test, y_pred_semi)
print("Semi-supervised Learning (SelfTrainingClassifier with Logistic Regression) Accuracy:", round(accuracy_semi,2))


# --------------------------------------------------------------------
# 4. Reinforcement Learning (Random Agent)
# --------------------------------------------------------------------

correct = 0     # Initialize the counter for correct guesses

for _ in range(100):     # Simulate 100 random attempts
    i = random.randint(0, len(y_test)-1)    # Randomly select an index from the test set
    guess = random.randint(0,2)             # Randomly guess one of the three possible classes (0,1,2)

    if guess == y_test[i]:                  # Check if the guess is correct
        correct += 1

# Calculate and print the accuracy of the random guess agent
print("Reinforcement Learning (Random Guess Agent) Accuracy:", round(correct / 100.0,2))

