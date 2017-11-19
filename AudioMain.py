
import AudioBytes
import numpy as np
import matplotlib.pyplot as plt

AudioFile = AudioBytes.GetRecordAudio(2,5)
plt.plot(AudioFile)
plt.show()
