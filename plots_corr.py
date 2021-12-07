import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
fig,ax = plt.subplots(3,1)


def modem():

    w_o = [40,241,231,41,25,64,54,226,161,70,51,88,67,57,99,282,222,213,310,189]
    w = [31,200,181,34,18,53,37,184,118,55,40,77,45,43,71,150,172,185,198,110]

    change = []
    change_e = [0.015000000000000001, 0.008101165777514326, 0.009410878976096368, 0.007423117709437965, 0.011200000000000002, 0.0078125, 0.016569200779727095, 0.0084473049074819, 0.01780538302277433, 0.012605042016806721, 0.012687427912341408, 0.0078125, 0.01427644386761843, 0.01023391812865497, 
    0.01414141414141414, 0.026004728132387706, 0.013248542660307366, 0.007732670533001934, 0.02007168458781362, 0.017416225749559082]

    for i in range(0,20):
        change.append((w_o[i] - w[i])/w_o[i])
     
    a = list(range(0,len(w_o)))
    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']


    X_axis = np.arange(len(x))
    ax[0].bar(X_axis, change, yerr = change_e, width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[0].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[0].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[0].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[0].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[0].set_xticks(X_axis)
    ax[0].set_xticklabels(x)
    ax[0].set_ylabel('Decrease in Load Time')
    #plt.tight_layout()
    #plt.show()


def three_g():
    w_o = [1.355,6.92,8.8,3.6,1.4,2.3,1.3,14.7,18.7,18,19.5,21.6,33.23,12,8,34.6,66,71,54,46]
    w = [1.12465, 5.3132, 7.128000000000001, 3.204, 1.274, 1.8949999999999999, 1.0962, 13.524, 
    15.155, 15.66, 13.649999999999999, 17.28, 25.9194, 9.48, 7.36, 31.14, 52.14, 46.15, 42.660000000000004, 39.1]

    change = []
    change_e = [0.007391304347826089, 0.010095501382256847, 0.007916666666666664, 0.005238095238095237, 0.004736842105263154, 0.008385093167701866, 0.00627076923076923, 0.003333333333333334, 0.009977483816493105, 0.007647058823529412, 0.01578947368421053, 0.013333333333333334, 0.014666666666666663, 0.013999999999999997, 
    0.003999999999999998, 0.004000000000000001, 0.011052631578947368, 0.019444444444444445, 0.009545454545454543, 0.007142857142857141]

    for i in range(0,20):
        change.append((w_o[i] - w[i])/w_o[i])



    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']
    
    X_axis = np.arange(len(x))
    ax[1].bar(X_axis, change, yerr = change_e, width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[1].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[1].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[1].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[1].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[1].set_xticks(X_axis)
    ax[1].set_xticklabels(x, rotation = 0)
    ax[1].set_ylabel('Decrease in Load Time')
    #plt.tight_layout()
    #plt.show()

def four_g():
    w_o = [0.16,1.39,1.4,1.6,0.27,1.1,0.47,1.8,1.79,0.39,1.33,1.28,3.23,2.15,1.8,1.01,2.3,1.4,2.3,0.89]
    w = [0.1472, 1.3482999999999998, 1.3439999999999999, 1.568, 0.24570000000000003, 1.0120000000000002, 0.39949999999999997, 
    1.602, 1.6289, 0.3705, 1.1438000000000001, 1.1136, 
    2.907, 2.021, 1.584, 0.9696, 2.0469999999999997, 1.3159999999999998, 2.139, 0.8188000000000001]
    
    change = []
    change_e = [0.004705882352941178, 0.0015000000000000026, 0.0018181818181818197, 0.0009090909090909098, 0.003749999999999998, 0.0036363636363636303, 0.006250000000000001, 0.006470588235294116, 0.005294117647058824, 0.002380952380952383, 0.006999999999999997, 0.007222222222222227, 0.004347826086956522,
     0.0028571428571428576, 0.005217391304347826, 0.0024999999999999996, 0.005789473684210529, 0.0031578947368421082, 0.004375000000000001, 0.004210526315789469]
    

    for i in range(0,20):
        change.append((w_o[i] - w[i])/w_o[i])

    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']
    
    X_axis = np.arange(len(x))
    ax[2].bar(X_axis, change, yerr = change_e, width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[2].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[2].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[2].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[2].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[2].set_xticks(X_axis)
    ax[2].set_xticklabels(x, rotation = 0)
    ax[2].set_ylabel('Decrease in Load Time')
    ax[2].set_xlabel('Websites')
    #plt.tight_layout()
    plt.show()

modem()
three_g()
four_g()
