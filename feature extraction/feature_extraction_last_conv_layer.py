from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras import preprocessing
import numpy as np

# Load the model with include_top=False and pooling='avg'
model = VGG16(weights='imagenet', include_top=False , pooling='avg')



# Load an image (replace 'image.jpg' with your image path)
# img_path = 'image.jpg'
img_path = "D:\\codes\\Third-year-Project\\feature extraction\\flicker 8k dataset\\archive\\Images\\10815824_2997e03d76.jpg"

img = preprocessing.image.load_img(img_path, target_size=(224, 224))
x = preprocessing.image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Extract features

features = model.predict(x)
print("Feature vector shape:")
print(features.shape)  # Should print (1, 512)
print("Feature vector:")
print(features)  # Displays the feature vector