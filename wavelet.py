#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://3month-of-life.blogspot.com/2011/07/wavelet-shrinkage-python.html
#https://habrahabr.ru/post/103899/
import pywt
import pylab
import random
import scipy


# отрисовка графиков функций
def plot(data):
    pylab.figure()
    pylab.plot(data)
    pylab.grid(True)


# число точек дискретизации
N = 65536

# массивы чистого и зашумленного сигналов
data = scipy.ones(N, float)
ndata = scipy.ones(N, float)

# дисперсия шума
sigma = 4

# генерируем сигнал и накладываем шум
for i in range(N):
    data[i] = 10 * scipy.sin(6.28 * (1 / float(N) + i / 10e+8) * i)
    ndata[i] = data[i] + random.gauss(0, sigma)

# знаходим максимальный уровень разложения
w = pywt.Wavelet('sym20')
dec_level = pywt.dwt_max_level(N, w.dec_len)

# находим коэффициенты разложения для макисмального уровня
coeffs = pywt.wavedec(ndata, 'sym20', 'zpd', dec_level)

# зная шумовую дисперсию вычисляем treshold-level
tr_level = sigma * scipy.sqrt(2 * scipy.log(N))
print tr_level

# tresholding
for i in range(dec_level):
    #tcoeffs = pywt.thresholding.soft(coeffs[i + 1], tr_level)
    tcoeffs = pywt.threshold(coeffs[i + 1], tr_level)
    coeffs[i + 1] = tcoeffs

# обратное преобразование - получаем очищенный сигнал
rdata = pywt.waverec(coeffs, 'sym20', 'zpd')

# рисуем графики
plot(data)
plot(ndata)
plot(rdata)
pylab.show()





