import numpy

def ZRC(frame):
    signs = numpy.sign(frame)
    signs[signs == 0] = -1
    return len(numpy.where(numpy.diff(signs))[0]) / len(frame)


def Energy(frame):
    return sum([abs(x) ** 2 for x in frame]) / len(frame)

def LogEnergy(frame):
    return 0

def chunks(l, k):
    for i in range(0, len(l), k):
        yield l[i:i + k]

def Entropy(frame, numSubFrames):
    lenSubFrame = int(numpy.floor(len(frame) / numSubFrames))
    shortFrames = list(chunks(frame, lenSubFrame))
    energy = [Energy(s) for s in shortFrames]
    totalEnergy = sum(energy)
    energy = [e / totalEnergy for e in energy]
    entropy = 0.0
    for e in energy:
        if e != 0:
            entropy = entropy - e * numpy.log2(e)
    return entropy