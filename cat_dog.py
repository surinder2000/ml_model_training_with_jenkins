from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras_preprocessing.image import ImageDataGenerator
model = Sequential()

model.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu',input_shape=(64, 64, 3)))

model.add(MaxPooling2D(pool_size=(2, 2)))
add_layers=0
while add_layers!=0:
    model.add(Convolution2D(filters=64,kernel_size=(3,3),activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    add_layers-=1

model.add(Flatten())

model.add(Dense(units=128, activation='relu'))

model.add(Dense(units=1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

no_of_epochs=1

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_data = train_datagen.flow_from_directory(
        '/root/cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
validation_data = test_datagen.flow_from_directory(
        '/root/cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        training_data,
        epochs=no_of_epochs,
        validation_data=validation_data)
model.save('/root/cat_dog.h5')

score = model.evaluate(test_set)

with open('/root/accuracy.txt','w') as file:
    file.write(str(score[1]*100))
    file.close()


