##################################################################################################################################


import load
import numpy as np
import numpy
from scipy import interpolate
import matplotlib.pyplot as plt
import time






##################################################################################################################################
#                     Here be Inputs and Includes
# 
#
#
#
#
#
#####################################################################################################################################################################################################################################################################
#
#
#                     Here follows definititions. ONE PER CELL!!!
#
#
##################################################################################################################################
#   Sebastians Resample function
#   Takes: Data, Time , samplerate
#   Output: interpolated Data and Time of length samplerate
#   
#

def resample(y,x,num):
    f = interpolate.interp1d(x, y)
    x2 = np.linspace(x[0], x[-1], num)
    return f(x2),x2

#   Theos Cycle Cut generator
#   Searches for passings on defined heigth
#      and ignores nearby passings, effect-
#      ively searching for big carvings
#
#   Note: This one is quite fast

def pass_cut(data,t,height=0,delta=0, search=0):
    relation=np.sign(data-height)
    all_crossings=numpy.diff(relation)
    #We lose one entry here so every where is followed by a +1
    if search>0:
        crossings=np.where(all_crossings>0)[0]+1
    elif search<0:
        crossings=np.where(all_crossings<0)[0]+1
    else:
        tmp=np.logical_or(all_crossings<0,all_crossings>0)
        crossings=np.where(tmp)[0]+1
    #Now whe have our crossings and need to get the delta of the time into it
    time=t[crossings]
    return crossings[np.where(np.diff(time)>delta)]
        
# Another one of Theos Cycle cut generators
# Searches for Maxima and chooses big local Maxima with
#      a certain distance to the last big Maximum
#
# Explanation for search parameter: >=0 searches maxima, <0 searches minima
#

#def min_o_max_cut(data,t,delta=0,sigma=0.2,sigma2=0.05,search=1):
#    sec_derivative_ish=np.diff(np.sign(np.diff(data)))
#    Min_Max=[]
#    if search>=0:
#        working=np.where(sec_derivative_ish<0)[0]
#        Min_Max=data[working]
#    else:
#        working=np.where(sec_derivative_ish>0)[0]
#        Min_Max=data[working]
#    if search>=0:
#        for index in range(len(Min_Max)):
#            if index < delta:
#                lower=0
#            else:
#                lower=index-delta
#            if len(Min_Max)-index-1< delta:
#                upper=len(Min_Max)-1
#            else:
#                upper=index+delta
            
# Just an euclidean norm
#
#
#

def my_norm(cycle): 
    return np.sum(cycle**2)/len(cycle)


# My try at metrics
#
#
#
#
#

def metrics(x,y):
    diffx=np.array([0]+list(np.diff(x)))
    diffy=np.array([0]+list(np.diff(y)))
    abs_diff=np.maximum(np.abs(diffx),np.abs(diffy))
    abs_diff[np.where(abs_diff==0)]=np.amin(abs_diff[abs_diff>0])
    #abs_diff=abs_diff/np.amin(abs_diff)
    things=np.abs(x-y)
    things=things[things>abs_diff*100]
    return np.sum(things)
    

# projection divergence
#
#
#
#
def proj_divergence(data1,data2,time1,time2):
    x=np.array(zip(data1,time1))
    y=np.array(zip(data2,time2))
    divergence=0
    for i in y:
        divergence+=np.amin(np.norm(x-i,axis=1))
    return divergence

# Similarity of strings algorithm 
# changed to work on gaits:
#
#
#
#
def similarity(gait1,gait2,time1,time2,g=12):
    #we do not set g as gap penality but instead take the time gap as gap
    #and use g as multiplier for the time
    M=np.zeros((len(gait1),len(gait2)))
    #As we do want 0 to be identical gaits and big values to be big differences we have to change some of the idea
    #beginning with changing the signs
    for i in range(len(gait1)):
	M[i,0]=time1[i]*g
    for j in range(len(gait2)):
        M[0,j]=time2[j]*g
    #also we need some nice p (in this case just the norm)
    def p(x,y):
        return np.abs(x-y)
    for i in range(len(gait1))[1:]:
        for j in range(len(gait2))[1:]:
            M[i,j]=min(
			M[i-1,j]+(time1[i]-time1[i-1])*g
			,M[i,j-1]+(time2[j]-time2[j-1])*g
			,M[i,j]+p(gait1[i],gait2[j])
			,M[i,j]+p(gait2[j],gait1[i])
			)
    return M[len(gait1)-1,len(gait2)-1]


# Theos quick first try at sanity
#
#

def quicksane(cuts,axis,data,mini=150,maxi=200):
    return np.logical_and(np.logical_and(np.diff(cuts)>mini,np.diff(cuts)<maxi),np.logical_or(cuts[1:]<0,np.logical_or(np.arange(len(cuts)-1)<80,np.arange(len(cuts)-1)>130)))

# Theos Gait_Cycle extractor
# Takes: Cuts and Data
# Returns: List of Lists of Arrays of Data which are cut and resampled to the same length
#          And are checked to be sane
#
#


def cut_into_cycles(data,cutter,sanity_check,axis=4,debug=0,static_samplerate=True,samplerate=200):
    cuts=cutter(data[:,axis],data[:,0])
    sane=sanity_check(cuts,axis,data)
    if debug>2:
        print("cuts:",cuts)
        print("sanity:",sane)
    if debug>0:
        print("sane cuts percentage of cycles:",len(cuts[sane])*1./(len(cuts)-1))
        length=len(data[:,axis])
        cut_length=0
        for i in range(len(cuts)-1):
            if sane[i]:
                cut_length+=cuts[i+1]-cuts[i]
        print("sane cuts percentage of data length:",cut_length*1./length)
        print("# of sane cycles:", len(cuts[sane]))
        print("range of length", min(np.diff(cuts))," to ", max(np.diff(cuts)))
        dbg=np.sort(np.diff(cuts))
        print("range of 80 percent:",dbg[ceil(len(dbg)*.1)]," to ",dbg[floor(len(dbg)*.9)])
        print("range of 60 percent:",dbg[ceil(len(dbg)*.2)]," to ",dbg[floor(len(dbg)*.8)])
    if debug>1:
        plt.hist(np.diff(cuts),bins=40)
        plt.show()
    
    cycles=[[],[],[],[],[],[],[]]
    for i in range(len(cuts)-1):
        if sane[i]:
            for j in range(1,7):
                if j==1:
                    tmpd=data[:,j][cuts[i]:cuts[i+1]]
                    tmpt=data[:,0][cuts[i]:cuts[i+1]]-data[:,0][cuts[i]]
                    if static_samplerate:
                        tmpd,tmpt=resample(tmpd,tmpt,samplerate)
                    cycles[j].append(tmpd)
                    cycles[0].append(tmpt)
                else:
                    tmpd=data[:,j][cuts[i]:cuts[i+1]]
                    tmpt=data[:,0][cuts[i]:cuts[i+1]]
                    if static_samplerate:
                        tmpd=resample(tmpd,tmpt,samplerate)[0]
                    cycles[j].append(tmpd)
                    
    return cycles
