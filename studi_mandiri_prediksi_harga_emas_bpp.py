import pandas as pd
import numpy as np
from google.colab import files
uploaded = files.upload()
ADA = pd.read_excel('Data Harga Emas.xlsx')
print(ADA)

x=ADA.iloc[:,0:3].values #mengambil kolom open, high dan low
y=ADA.iloc[:,-1].values #mengambil kolom close

from sklearn.model_selection import train_test_split
#datatest 75% dari total data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.75, random_state=70)

#Import tf.keras.Sequential
import tensorflow as tf

model= tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units=9, activation='relu', input_shape=(3,)))
model.add(tf.keras.layers.Dense(units=1))
model.compile(loss='mean_absolute_error', optimizer=tf.keras.optimizers.Adam(0.001))

model.fit(x_train, y_train, epochs=200)

#Simpan model backpropagation
model.save("model.ADA")

#Menampilkan Hasil Prediksi dan Data Aktual
hasil=model.predict(x_test)
print(x_test)
print(hasil)

import matplotlib.pyplot as plt

a=range(len(y_test))

plt.scatter(a, hasil, color='blue') #hasil prediksi
plt.scatter(a, y_test, color='green') #Data Aktual
plt.title("Hasil Testing Harga Emas terhadap Data Aktual")
plt.xlabel("Data Tes")
plt.ylabel("Harga Emas")
plt.show()

plt.scatter(a, hasil, color='blue') #hasil prediksi
plt.plot(a, y_test, color='red') #Data Aktual
plt.title("Hasil Testing Harga Emas terhadap Data Aktual")
plt.xlabel("Data Tes")
plt.ylabel("Harga Emas")
plt.show()

1#*************************************#
#   Aplikasi Prediksi Harga Emas   #
#Menggunakan Algoritma Backpropagation#
#                                     #
#*************************************#
open = input('Input Open Price($): ')
high = input('Input High Price($): ')
low = input('Input Low Price($): ')

closeprice=model.predict([[float(open),float(high),float(low)]])
print('Cardano Will Close The Price in :')
print(closeprice)
