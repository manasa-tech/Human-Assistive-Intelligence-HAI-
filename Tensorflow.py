# --------------------------------------------------
# TensorFlow Deep Learning Example
# Handwritten Digit Classification using MNIST
# --------------------------------------------------

# 1. Import required libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 2. Check TensorFlow version
print("TensorFlow version:", tf.__version__)

# 3. Load MNIST dataset
mnist = tf.keras.datasets.mnist

# 4. Split dataset into training and testing
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 5. Display dataset shapes
print("Training images shape:", x_train.shape)
print("Training labels shape:", y_train.shape)
print("Test images shape:", x_test.shape)
print("Test labels shape:", y_test.shape)

# 6. Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# 7. Display one sample image
plt.imshow(x_train[0], cmap="gray")
plt.title("Sample Training Image")
plt.show()

# 8. Build neural network model
model = tf.keras.models.Sequential()

# 9. Flatten layer converts 28x28 to 784
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

# 10. First hidden layer
model.add(tf.keras.layers.Dense(128, activation='relu'))

# 11. Dropout layer for regularization
model.add(tf.keras.layers.Dropout(0.2))

# 12. Second hidden layer
model.add(tf.keras.layers.Dense(64, activation='relu'))

# 13. Output layer with 10 classes
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# 14. Print model summary
model.summary()

# 15. Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 16. Train the model
history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_split=0.2
)

# 17. Evaluate model using test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# 18. Plot training accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'])
plt.show()

# 19. Plot training loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'])
plt.show()

# 20. Make predictions
predictions = model.predict(x_test)

# 21. Print prediction for first image
print("Predicted digit:", np.argmax(predictions[0]))
print("Actual digit:", y_test[0])

# 22. Display the test image
plt.imshow(x_test[0], cmap="gray")
plt.title("Test Image")
plt.show()

# 23. Function to visualize predictions
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap="gray")

    predicted_label = np.argmax(predictions_array)

    if predicted_label == true_label:
        color = "blue"
    else:
        color = "red"

    plt.xlabel(
        "{} {:2.0f}% ({})".format(
            predicted_label,
            100 * np.max(predictions_array),
            true_label
        ),
        color=color
    )

# 24. Function to plot prediction values
def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]

    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])

    thisplot = plt.bar(range(10), predictions_array)

    plt.ylim([0, 1])

    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# 25. Visualize prediction
i = 10
plt.figure(figsize=(6,3))

plt.subplot(1,2,1)
plot_image(i, predictions[i], y_test, x_test)

plt.subplot(1,2,2)
plot_value_array(i, predictions[i], y_test)

plt.show()

# 26. Save trained model
model.save("digit_classifier_model.h5")

print("Model saved successfully")

# 27. Load the saved model
loaded_model = tf.keras.models.load_model("digit_classifier_model.h5")

print("Model loaded successfully")

# 28. Evaluate loaded model
loss, accuracy = loaded_model.evaluate(x_test, y_test)

print("Loaded model accuracy:", accuracy)

# 29. Predict again using loaded model
new_predictions = loaded_model.predict(x_test)

print("New prediction for first image:", np.argmax(new_predictions[0]))

# 30. Convert prediction probabilities
probabilities = new_predictions[0]

print("Prediction probabilities:", probabilities)

# 31. Show top predicted digit
top_prediction = np.argmax(probabilities)

print("Top predicted digit:", top_prediction)

# 32. End of TensorFlow example
print("TensorFlow deep learning example completed.")