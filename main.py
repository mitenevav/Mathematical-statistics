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
RES_PATH = "results/"
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


#plotting
def plot(x, y, label_x, label_y, label, new_fig=True):
    if new_fig:
        plt.figure(figsize=(15, 10))

    plt.plot(x, y, label=label)
    plt.xlabel(label_x, fontsize=14)
    plt.ylabel(label_y, fontsize=14)



#the alignment of the intervals
#INPUT: signal1 - first signal
#       signal2 - second signal
#OUTPUT:    result vectors
def makeInterval(signal1, signal2):
    l = max( min(signal1[0]), min(signal2[0]))
    r = min( max(signal1[0]), max(signal2[0]))


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

#setting borders
#INPUT: signal - signal
#       left - left border
#       right - right border
#OUTPUT:    result vectors
def setBorders(signal, left, right):
    x = []
    y = []
    for i in range(len(signal[0])):
        if signal[0][i] >= left and signal[0][i] <= right:
            x.append(signal[0][i])
            y.append(signal[1][i])

    return x, y

#division of vectors
#INPUT: op1 - first operand
#       op2 - second operand
#OUTPUT:    result vector
def div(op1, op2):
    res = []
    for i in range(len(op1)):
        res.append(op1[i] / op2[i])
    return res

#getting results using two signals
#INPUT: signal1 - first signal
#       signal2 - second signal
#       table - table created from the calibration file
#OUTPUT:    result vectors
def process(signal1, signal2, table):
    sign1 = signal1.copy()
    sign2 = signal2.copy()

    sign1, sign2 = makeInterval(sign1, sign2)

    result = div(sign1[1], sign2[1])

    result = calibration.getTemperature(table, result)

    return sign1[0], result

#getting a signal
#INPUT: nums - sxr numbers
#       sht_reader - generated shtReader
#       RIO - region of interest
#       borders - manual border adjustment
#       left - left border
#       right - right border
#OUTPUT:    list of signals
def makeSignals(nums, shtReader, ROI=True, borders=False, left = LEFT, right = RIGHT):
    signals = []
    for i in range(len(nums)):
        signal = shtReader.get_signals(NUM_SIGNAL_FROM_SHT[nums[i]])

        data = np.array((signal[0].get_data_x(), signal[0].get_data_y()))

        if ROI:
            roi = pyglobus.sawtooth.get_signal_roi(data[1], mean_scale=1)
            x = np.copy(data[0][ roi[0]:roi[1]])
            y = np.copy(data[1] [roi[0]:roi[1]])
            data = np.array((x, y))

        if borders:
            x, y = setBorders(data, left, right)
            data = np.array((x, y))


        pyglobus.dsp.low_pass_filter(data[1], LOW_PASS_CUTOFF, SIGNAL_SAMPLING_RATE)

        signals.append(data)

    return signals


#getting results from an html file
#INPUT: shtNum - sht file number
#       nums - sxr numbers
#       RIO - region of interest
#       borders - manual border adjustment
#       left - left border
#       right - right border
#       graphics - output of graphs
def mainProcess(shtNum, nums, ROI=True, borders=False, left=LEFT, right=RIGHT, graphics=True):
    nums.sort(reverse=True)

    shtReader = pyglobus.util.ShtReader(SHT_PATH + "sht" + str(shtNum) + ".sht")

    signals = makeSignals(nums, shtReader, ROI=ROI, borders=borders, left=left, right=right)

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            filename = 'R' + str(nums[i]) + '-' + str(nums[j]) + '.txt'

            table = calibration.getCalibration(CALIBR_PATH + filename)

            x, y = process(signals[i], signals[j], table)

            if graphics:
                plot(x, y, "Time (ms)", "T (eV)", "R" + str(nums[i]) + "-" + str(nums[j]), new_fig=False,)

            outputResults("Temperature" + "_" + "SHT" + str(shtNum) + "_" +str(nums[i]) + "-" + str(nums[j]) + ".txt", x, y)
    if graphics:
        plt.title("SHT"+str(shtNum))
        plt.legend()
        plt.show()


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#output results to a file
#First column - time (ms)
#Second column - temperature (eV)
def outputResults(filename, column1, column2):
    f = open(RES_PATH + filename, 'w')
    for i in range(len(column1)):
        f.write(str( toFixed(column1[i], 7)) + "\t" + str(toFixed(column2[i], 1)) + "\n")
    f.close()

if __name__ == "__main__":
    SHT_NUMBER = 38515
    NUM_SXR = [80, 50, 15]
    mainProcess(SHT_NUMBER, NUM_SXR)