import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

def load_and_preprocess_image(image_path):
    """
    Load and preprocess image for VGG16
    """
    # Load image and resize to 224x224 (VGG16 input size)
    img = image.load_img(image_path, target_size=(224, 224))
    
    # Convert image to array
    img_array = image.img_to_array(img)
    
    # Expand dimensions to match model's expected input
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess input for VGG16
    processed_img = preprocess_input(img_array)
    
    return processed_img

def extract_features(image_path):
    """
    Extract features from image using VGG16
    """
    # Load VGG16 model without top classification layers
    model = VGG16(weights='imagenet', include_top=False)
    
    # Load and preprocess the image
    processed_img = load_and_preprocess_image(image_path)
    
    # Extract features
    features = model.predict(processed_img)
    
    # Flatten the features
    flattened_features = features.flatten()
    
    return flattened_features

# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "path/to/your/image.jpg"
    
    try:
        # Extract features
        features = extract_features(image_path)
        print(f"Feature vector shape: {features.shape}")
        print(f"First few features: {features[:10]}")
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
