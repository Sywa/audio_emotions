#https://habrahabr.ru/post/184728/
def smoothing_filter(s):
    signal=[]
    for i in range(1,len(s)-1):
        signal.append((s[i-1]+s[i]+s[i+1])/3)
    return signal

def smoothing_filter_by_habr(s):
    signal = []
    for i in range(1, len(s) - 1):
        signal.append( (0.25*s[i - 1]) + (0.5 * s[i]) + (0.25*s[i + 1]) )
    return signal

#FIR filter design with Python and SciPy
# http://mpastell.com/2010/01/18/fir-with-scipy/
#PyMedia
#http://pymedia.org/tut/dump_wav.html



def low_requency_filter(signal, a, b):
    #y[n] = a * x[n] + b * y[n - 1]...y[0]
    result_signal = []
    for i in range(0,len(signal)):
        if (i==0):
            result_signal.append(0)
        else:
            result_signal.append(a * signal[i] + b * result_signal[n - 1])
    return result_signal