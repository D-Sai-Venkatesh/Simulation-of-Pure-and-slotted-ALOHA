import math

import random

import matplotlib.pyplot as plt

import time

random.seed(time)

def next_interval(load):
    return (-1.0/load) * math.log(random.random())

def generate_pkts(load,no_pkts):
    time = 0
    pkts = [] 
    for x in range(0,no_pkts):
        time += next_interval(load)
        pkts.append(time)
    return pkts

def troughput(pkts,load):
    success = 0
    for x in range(1,len(pkts)-1):
        fail = 0
        if (pkts[x] - pkts[x-1] > 1 and pkts[x+1] - pkts[x] > 1):
            success = success + 1
    # print(success,len(pkts))
    return (float(success)/len(pkts)) * load

def sim ():
    load = 0.1
    loads = []
    through_put = []
    while(load <= 5):
        loads.append(load)
        pkts = generate_pkts(load,10000)
        through_put.append(troughput(pkts,load))
        load = load + 0.1

    plt.plot(loads,through_put,label = 'experiment')

    loads = []
    current_load = 0.1
    while(current_load <= 5):
        loads.append(current_load)
        current_load += 0.1
    throughput = []
    for x in loads:
        throughput.append(x * pow(math.e,(-1*2*x)))

    plt.plot(loads,throughput,label = 'ideal')

    plt.xlabel('load')
    plt.ylabel('throughput')
    plt.title('pure Aloha')
    plt.show()



sim()