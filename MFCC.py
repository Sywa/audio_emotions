# coding: utf-8
from python_speech_features import mfcc
from python_speech_features import logfbank
from python_speech_features.base import fbank
import scipy.io.wavfile as wav
import matplotlib as plt


#https://en.wikipedia.org/wiki/Mel-frequency_cepstrum
#http://www.top-technologies.ru/ru/article/view?id=35724
#http://python-speech-features.readthedocs.io/en/latest/
#http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/
#https://habrahabr.ru/post/150251/
#https://habrahabr.ru/post/140828/
#https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%B4%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B9_%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8_%D0%B2%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9_%D1%88%D0%BA%D0%B0%D0%BB%D1%8B


#MFCC
#(rate,sig) = wav.read("mfcc.wav")

def MFCC(record):
    (rate, sig) = wav.read(record)
    sig = sig[:10000]

    #mfcc_feat = mfcc(sig,rate)
    mfcc_feat = mfcc(sig,rate,0.025,0.01,13,26,512,0,None,0.97,22,True)
    fbank_feat = logfbank(sig,rate)

    print("mfcc_feat",mfcc_feat)
    print("Count samples", len(sig))
    print("mfcc_len ",len(mfcc_feat[0]))
    print("mfcc_len ",len(mfcc_feat))
    print("fbank",fbank_feat[0])

    plt.plot(fbank_feat[1:3,:])
    plt.show()



