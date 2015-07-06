import load
import numpy as np
import numpy
from scipy import interpolate
import matplotlib.pyplot as plt
import time
from test import *









print("start loading")
data_seb1=load.load_to_arrays("../data/tagged/sebastian/2015-05-25-12:45:25_accdata")
print("seb 1/6")
data_seb2=load.load_to_arrays("../data/tagged/sebastian/2015-05-25-15:43:27_accdata")
print("seb 2/6")
data_seb3=load.load_to_arrays("../data/tagged/sebastian/2015-05-30-14:12:48_accdata")
print("seb 3/6")
data_seb4=load.load_to_arrays("../data/tagged/sebastian/2015-05-30-14:35:01_accdata")
print("seb 4/6")
data_seb5=load.load_to_arrays("../data/tagged/sebastian/2015-05-30-14:39:01_accdata")
print("seb 5/6")
data_seb6=load.load_to_arrays("../data/tagged/sebastian/2015-05-30-14:45:30_accdata")
print("seb 6/6")

data_theo1=load.load_to_arrays("../data/tagged/theo/2015-05-25-12:45:24_accdata")
print("theo 1/7")
data_theo2=load.load_to_arrays("../data/tagged/theo/2015-05-25-15:43:25_accdata")
print("theo 2/7")
data_theo3=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:12:55_accdata")
print("theo 3/7")
data_theo4=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:35:02_accdata")
print("theo 4/7")
data_theo5=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:39:03_accdata")
print("theo 5/7")
data_theo6=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:45:29_accdata")
print("theo 6/7")
data_theo7=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:48:01_accdata")
print("theo 7/7")
data_theo8=load.load_to_arrays("../data/tagged/theo/2015-05-30-14:56:41_accdata")
print("done")

print("start cutting ")
clk=time.clock()
time_anchor=clk
cycles_seb1=[]
for i in range(len(data_seb1)):
    cycles_seb1.append(cut_into_cycles(
        data_seb1[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 1/6 needed: ",time.clock()-clk)
clk=time.clock()
cycles_seb2=[]
for i in range(len(data_seb2)):
    cycles_seb2.append(cut_into_cycles(
        data_seb2[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 2/6 needed: ",time.clock()-clk)
clk=time.clock()
cycles_seb3=[]
for i in range(len(data_seb3)):
    cycles_seb3.append(cut_into_cycles(
        data_seb3[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 3/6 needed: ",time.clock()-clk)
clk=time.clock()
cycles_seb4=[]
for i in range(len(data_seb4)):
    cycles_seb4.append(cut_into_cycles(
        data_seb4[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 4/6 needed: ",time.clock()-clk)
clk=time.clock()
cycles_seb5=[]
for i in range(len(data_seb5)):
    cycles_seb5.append(cut_into_cycles(
        data_seb5[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 5/6 needed: ",time.clock()-clk)
clk=time.clock()
cycles_seb6=[]
for i in range(len(data_seb6)):
    cycles_seb6.append(cut_into_cycles(
        data_seb6[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("seb 6/6 needed: ",time.clock()-clk)
print("time for seb_data: ",time.clock()-time_anchor)
seb_anchor=time.clock()

clk=time.clock()
cycles_theo1=[]
for i in range(len(data_theo1)):
    cycles_theo1.append(cut_into_cycles(
        data_theo1[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 1/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo2=[]
for i in range(len(data_theo2)):
    cycles_theo2.append(cut_into_cycles(
        data_theo2[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 2/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo3=[]
for i in range(len(data_theo3)):
    cycles_theo3.append(cut_into_cycles(
        data_theo3[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 3/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo4=[]
for i in range(len(data_theo4)):
    cycles_theo4.append(cut_into_cycles(
        data_theo4[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 4/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo5=[]
for i in range(len(data_theo5)):
    cycles_theo5.append(cut_into_cycles(
        data_theo5[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 5/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo6=[]
for i in range(len(data_theo6)):
    cycles_theo6.append(cut_into_cycles(
        data_theo6[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 6/7 needed: ",time.clock()-clk)
clk=time.clock()
cycles_theo7=[]
for i in range(len(data_theo7)):
    cycles_theo7.append(cut_into_cycles(
        data_theo7[i][2]
        ,lambda data,time: pass_cut(data,time,height=.5,delta=0.3, search=1),quicksane))
print("theo 7/7 needed: ",time.clock()-clk)
print("theo_time_needed: ",time.clock()-seb_anchor)
print("time_needed_absolute: ",time.clock()-time_anchor)
print("done")


#here starts testing of string similarity
def make_D(cycles,time):
    D=np.zeros((len(cycles),len(cycles)))
    print("start producing D: ")
    for i in range(len(cycles)):
        print("percentage: ",(((i+1)*1./len(cycles))**2)*100)
        for j in range(len(cycles))[:i]:
            D[j,i]=D[i,j]=similarity(cycles[i],cycles[j],time[i],time[j])
    D=D*1.
    return D

def k_median_eliminating_full(cycles,D,k=3):
    #implement distance matrix so you dont have to compute often
    clusters=range(len(cycles))
    nodes=range(len(cycles))
    while len(nodes)>3:
        index=np.argmin(D[nodes][:,nodes])
        index=(index//len(nodes),index%len(nodes))
        nodes.remove(nodes[index[1]])
        nodes.remove(nodes[index[0]])
        pre_nodes=[]
        for i in range(len(clusters)):
            if clusters[i]==index[0]:
                pre_nodes.append(i)
            if clusters[i]==index[1]:
                clusters[i]==index[0]
                pre_nodes.append(i)
        nodes.append(pre_nodes[np.argmin(np.mean(D[pre_nodes][:,pre_nodes],axis=0))])
    for i in range(len(np.unique(clusters))):
        for j in range(len(clusters)):
            if clusters[j]==np.unique(clusters)[i]:
                clusters[j]=i
    return clusters
D=0
try:
     D=np.load('Distance_string.npy')
except (IOError):
     D=make_D(cycles_theo2[2][4],cycles_theo2[2][0])
     np.save('Distance_string',D)
#D=np.load('Distance_string.npy')
testing=k_median_eliminating_full(cycles_theo2[2][4],D)
print(testing)
for i in range(len(testing)):
    if testing[i]==0:
        plt.plot(cycles_theo2[2][0][i],cycles_theo2[2][4][i],"green")
for i in range(len(testing)):
    if testing[i]==1:
        plt.plot(cycles_theo2[2][0][i],cycles_theo2[2][4][i],"blue")
for i in range(len(testing)):
    if testing[i]==2:
        plt.plot(cycles_theo2[2][0][i],cycles_theo2[2][4][i],"red")
plt.show()
