import numpy as np
import datetime
from datetime import timedelta

def load_to_arrays(infile):
    f=open(infile,"r")
    arrays=[]
    date=datetime.datetime.strptime(infile.split("/")[-1][0:10],"%Y-%m-%d")
    tag=""
    pos=f.tell()
    nextline=f.readline()
    while nextline[0:2]=="#T":
    	pos=f.tell()
    	tag=nextline[3:]
    	nextline=f.readline()
    f.seek(pos)
    splitline=nextline.split(" ")
    stime=timedelta(hours=int(splitline[0]),minutes=int(splitline[1]),seconds=int(splitline[2]),microseconds=int(splitline[3]   ))
    l=[]
    time=date+stime
    line=f.readline()
    while line!="":
        if line[0:2]=="#T":
            arrays.append((tag,time,np.array(l)))
            l=[]
            tag=line[3:]
            pos=f.tell()
            nextline=f.readline()
            while nextline[0:2]=="#T":
                pos=f.tell()
                tag=nextline[3:]
                nextline=f.readline()
            f.seek(pos)
            splitline=nextline.split(" ")
            stime=timedelta(hours=int(splitline[0]),minutes=int(splitline[1]),seconds=int(splitline[2]),microseconds=int(splitline[3]   ))
            time=date+stime
        else:
            splitline=line.strip().split(" ")
            t=(timedelta(hours=int(splitline[0]),minutes=int(splitline[1]),seconds=int(splitline[2]),microseconds=int(splitline[3]))-stime).total_seconds()
            x=[t]
            x.extend(list(map(float,splitline[4:])))
            l.append(x)
        line=f.readline()

    arrays.append((tag,time,np.array(l)))
    return arrays
            
