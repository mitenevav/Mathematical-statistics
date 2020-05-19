import pyglobus
import numpy as np
import matplotlib.pyplot as plt
import calibration
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

SHT_PATH = "sht/"
CALIBR_PATH = "calibr/"
NUM_SIGNAL_FROM_SHT = {
        80 : b'SXR 80 mkm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        50 : b'SXR 50 mkm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        27 : b'SXR 27 \xec\xea\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        15 : b'SXR 15 \xec\xea\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    }
SIGNAL_SAMPLING_RATE = int(1e6)
LOW_PASS_CUTOFF = 5000
LEFT = 0.14
RIGHT = 0.20

def plot(x, y, label_x, label_y, label, new_fig=True):
    if new_fig:
        plt.figure(figsize=(15, 10))

    plt.plot(x, y, label=label)
    plt.xlabel(label_x, fontsize=14)
    plt.ylabel(label_y, fontsize=14)

def thinning(x, y, scale):
    xx = []
    yy = []
    for i in range(0, len(x), scale):
        xx.append(x[i])
        yy.append(y[i])
    return xx, yy

def setBorder(signal1, signal2):
    l = max( min(signal1[0]), min(signal2[0]), LEFT)
    r = min( max(signal1[0]), max(signal2[0]), RIGHT)


    res1 = [ [], [] ]
    for i in range(len(signal1[0])):
        if signal1[0][i] >= l and signal1[0][i] <= r:
            res1[0].append(signal1[0][i])
            res1[1].append(signal1[1][i])


    res2 = [ [], [] ]
    for i in range(len(signal2[0])):
        if signal2[0][i] >= l and signal2[0][i] <= r:
            res2[0].append(signal2[0][i])
            res2[1].append(signal2[1][i])

    return res1, res2

def div(opp1, opp2):
    res = []
    for i in range(len(opp1)):
        res.append(opp1[i] / opp2[i])
    return res

def process(signal1, signal2, table):
    sign1 = signal1.copy()
    sign2 = signal2.copy()

    sign1, sign2 = setBorder(sign1, sign2)

    result = div(sign1[1], sign2[1])

    result = calibration.getTemperature1(table, result)

    return sign1[0], result

def makeSignals(nums, shtReader):
    signals = []
    for i in range(len(nums)):
        signal = shtReader.get_signals(NUM_SIGNAL_FROM_SHT[nums[i]])

        data = np.array((signal[0].get_data_x(), signal[0].get_data_y()))

        pyglobus.dsp.low_pass_filter(data[1], LOW_PASS_CUTOFF, SIGNAL_SAMPLING_RATE)

        signals.append(data)

    return signals

def mainProcess(shtNum, nums):
    nums.sort(reverse=True)

    shtReader = pyglobus.util.ShtReader(SHT_PATH + "sht" + str(shtNum) + ".sht")

    signals = makeSignals(nums, shtReader)

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            filename = 'R' + str(nums[i]) + '-' + str(nums[j]) + '.txt'

            table = calibration.getCalibration(CALIBR_PATH + filename)

            x, y = process(signals[i], signals[j], table)

            plot(x, y, "Time (ms)", "T (eV)", "R" + str(nums[i]) + "-" + str(nums[j]), new_fig=False)
    plt.title("SHT"+str(shtNum))
    plt.legend()
    plt.show()



if __name__ == "__main__":
    SHT_NUMBER = 38515
    NUM_SXR = [80, 50, 15]
    mainProcess(SHT_NUMBER, NUM_SXR)

