import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots(3,1)


def modem():


    w_o = [40,241,231,41,25,64,54,226,161,70,51,88,67,57,99,282,222,213,310,189]
    w = [31,200,181,34,18,53,37,184,118,55,40,77,45,43,71,150,172,185,198,110]

    w_o_e = [1.6666666666666667, 14.176470588235293, 12.833333333333334, 1.64, 1.4705882352941178, 2.6666666666666665, 
    2.25, 15.066666666666666, 7.666666666666667, 3.1818181818181817, 2.217391304347826, 3.8260869565217392, 2.7916666666666665, 
    3.1666666666666665, 5.2105263157894735, 11.28, 12.333333333333334, 10.65, 14.090909090909092, 9.947368421052632]


    w_e = [3.0, 13.333333333333334, 8.733333333333333, 3.0, 0.6153846153846154, 5.5, 2.8333333333333335, 14.857142857142858, 
    6.285714285714286, 3.5, 4.444444444444445, 9.625, 3.0, 
    1.6428571428571428, 14.2, 15.0, 11.466666666666667, 14.23076923076923, 14.142857142857142, 8.461538461538462]

    a = list(range(0,len(w_o)))
    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']


    X_axis = np.arange(len(x))
    ax[0].bar(X_axis-0.2, w_o, yerr = w_o_e, label = 'QUIC', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[0].bar(X_axis+0.2, w, yerr = w_e, label = 'Our System', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[0].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[0].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[0].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[0].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[0].legend(bbox_to_anchor=[0.5, 0.25])
    ax[0].set_xticks(X_axis)
    ax[0].set_xticklabels(x)
    ax[0].set_ylabel('Time in Sec')
    x#plt.tight_layout()
    #plt.show()


def three_g():
    w_o = [1.355,6.92,8.8,3.6,1.4,2.3,1.3,14.7,18.7,18,19.5,21.6,33.23,12,8,34.6,66,71,54,46]
    w = [1.12465, 4.9132, 7.128000000000001, 3.204, 1.274, 1.4949999999999999, 0.962, 13.524, 
    12.155, 15.66, 13.649999999999999, 17.28, 25.9194, 9.48, 7.36, 31.14, 52.14, 46.15, 42.660000000000004, 39.1]
    w_o_e = [0.06452380952380952, 0.3642105263157895, 0.55, 
    0.14400000000000002, 0.06666666666666667, 0.14375, 0.08125, 0.8166666666666667, 0.9842105263157894, 0.8181818181818182, 
    1.0263157894736843, 0.9, 1.3845833333333333, 0.6, 0.4444444444444444, 1.5727272727272728, 2.64, 3.380952380952381, 2.7, 1.9166666666666667]

    w_e = [0.1606642857142857, 0.49132, 0.5940000000000001, 0.2912727272727273, 0.098, 
    0.299, 0.0962, 1.2294545454545454, 1.2155, 1.566, 2.275, 2.468571428571429, 5.18388, 0.79, 0.5257142857142857, 
    2.224285714285714, 10.428, 3.55, 6.094285714285715, 2.606666666666667]
    
    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']
    
    X_axis = np.arange(len(x))
    ax[1].bar(X_axis-0.2, w_o, yerr = w_o_e, label = 'QUIC', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[1].bar(X_axis+0.2, w, yerr = w_e, label = 'Our System', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[1].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[1].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[1].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[1].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[1].set_xticks(X_axis)
    ax[1].set_xticklabels(x, rotation = 0)
    ax[1].set_ylabel('Time in Sec')
    #plt.tight_layout()
    #plt.show()

def four_g():
    w_o = [0.16,1.39,1.4,1.6,0.27,1.1,0.47,1.8,1.79,0.39,1.33,1.28,3.23,2.15,1.8,1.01,2.3,1.4,2.3,0.89]
    w = [0.1472, 1.3482999999999998, 1.3439999999999999, 1.568, 0.24570000000000003, 1.0120000000000002, 0.39949999999999997, 
    1.602, 1.6289, 0.3705, 1.1438000000000001, 1.1136, 
    2.907, 2.021, 1.584, 0.9696, 2.0469999999999997, 1.3159999999999998, 2.139, 0.8188000000000001]
    w_o_e = [0.009411764705882354, 0.08176470588235293, 0.07368421052631578, 0.1, 0.018000000000000002, 
    0.04782608695652174, 0.01958333333333333, 0.08571428571428572, 0.08136363636363636, 0.01625, 0.0665, 0.07529411764705883, 0.17, 0.086, 0.10588235294117647, 0.045909090909090906, 
    0.09583333333333333, 0.07777777777777778, 0.10952380952380951, 0.049444444444444444]
    w_e = [0.016355555555555554, 0.16853749999999998, 0.2688, 0.224, 0.030712500000000004, 
    0.07784615384615387, 0.030730769230769228, 0.22885714285714287, 0.2327, 0.0463125, 0.0879846153846154, 0.07954285714285714, 0.4845, 0.3368333333333333, 0.1056, 0.1616, 0.1705833333333333, 
    0.1462222222222222, 0.19445454545454544, 0.13646666666666668]

    
    x = ['FB', 'Insta', 'Twitter', 'WApp', 'TTok',
        'Google', 'YT', 'Yahoo', 'Zoom', 'Netflix',
        'Amazon', 'MSfy', 'AliEx', 'Ebay', 'Flipkart',
        'Qq', 'WPost', 'NYT', 'ACBNews', 'CNN']
    
    X_axis = np.arange(len(x))
    ax[2].bar(X_axis-0.2, w_o, yerr = w_o_e, label = 'QUIC', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    ax[2].bar(X_axis+0.2, w, yerr = w_e, label = 'Our System', width = 0.4, alpha=0.85, ecolor='black', capsize=2)
    print('5g', w)
    print('5g', w_o_e)
    print('5g', w_e)
    ax[2].axvspan(-0.5, 4.5, alpha=0.2, color='red')
    ax[2].axvspan(4.5, 9.5, alpha=0.2, color='blue')
    ax[2].axvspan(9.5, 14.5, alpha=0.2, color='orange')
    ax[2].axvspan(14.5, 19.5, alpha=0.2, color='green')
    ax[2].set_xticks(X_axis)
    ax[2].set_xticklabels(x, rotation = 0)
    ax[2].set_ylabel('Time in Sec')
    ax[2].set_xlabel('Websites')
    #plt.tight_layout()
    plt.show()

modem()
three_g()
four_g()

