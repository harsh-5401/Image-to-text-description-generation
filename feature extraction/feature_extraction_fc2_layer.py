from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image
from keras.models import Model
import numpy as np

# Set NumPy print options to display the entire array
np.set_printoptions(threshold=np.inf)

# Load the model with include_top=True
# include_top = True means considering classification layer as well

base_model = VGG16(weights='imagenet', include_top=True)

# Create a feature extractor that outputs 'fc2'
feature_extractor = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

# Load an image (replace 'image.jpg' with your image path)
img_path = "D:\\codes\\Third-year-Project\\feature extraction\\flicker 8k dataset\\archive\\Images\\10815824_2997e03d76.jpg"

img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Extract features
features = feature_extractor.predict(x)

# flattened_features = features.flatten()
# print("after flattening:" , flattened_features.shape)

print("Feature vector shape:")
print(features.shape)  # Should print (1, 4096)
print("Feature vector:")
print(features)  # Displays the feature vector