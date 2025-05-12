import cv2                                                             # Import OpenCV library
import numpy as np                                                     # Import NumPy library
import os                                                              # Import os module to work with files and directories
from sklearn.model_selection import train_test_split                   # Import train_test_split to split data into train and test sets
from sklearn.neighbors import KNeighborsClassifier                     # Import KNeighborsClassifier for KNN algorithm
from sklearn.metrics import accuracy_score                             # Import accuracy_score to evaluate the model's performance



# This function extracts features from an image
def extract_features(image):
    # Calculate the mean color for each channel (Red, Green, Blue)
    mean_color = np.mean(image, axis=(0, 1))                           # Red, Green, Blue mean
    return mean_color                                                  # Return the mean color as the feature of the image
    


# This function prepares the dataset by loading images and their corresponding labels
def prepare_dataset(image_folder):
    features = []                                                      # List to store the image features
    labels = []                                                        # List to store the image labels
      


    # Assuming all images are in one folder without any subfolders
    for filename in os.listdir(image_folder):
        img_path = os.path.join(image_folder, filename)               # Get the image path
        img = cv2.imread(img_path)                                    # Read the image
        


        # Check if the image was successfully loaded
        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)            # Convert the image from BGR to RGB
            img_features = extract_features(img_rgb)                  # Extract features from the image
            features.append(img_features)                             # Add the features to the list
            

            # Here, assuming the label is part of the filename
            # Example: "cat_1.jpg" or "dog_2.jpg"
            if 'cat' in filename.lower():
                labels.append('cat')                                  # Assign 'cat' label if the filename contains 'cat'
            elif 'dog' in filename.lower():
                labels.append('dog')                                  # Assign 'dog' label if the filename contains 'dog'
            else:
                continue                                              # Skip the image if it doesn't match a known label
    
    return np.array(features), np.array(labels)                       # Return features and labels as NumPy arrays



# Load images and labels from the "test" folder
image_folder = "E:/ImageEnhancementProject/Dataset/test/"             # Folder containing test images
features, labels = prepare_dataset(image_folder)                      # Prepare the dataset by extracting features and labels



# Split the dataset into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)



# Apply KNN algorithm
knn = KNeighborsClassifier(n_neighbors=3)                             # Create a KNN classifier with 3 neighbors
knn.fit(X_train, y_train)                                             # Train the model using the training data
 


# Test the model
y_pred = knn.predict(X_test)                                          # Predict the labels for the test data



# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)                             # Compute accuracy by comparing predictions with true labels
print("Accuracy:", accuracy)                                          # Print the accuracy of the model
