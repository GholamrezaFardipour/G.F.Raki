import numpy as np

d = np.empty((5058,3042,2))

txt5="266.bmp"

f = open(txt5, mode="rb")
data = f.read()
leng = (len(data))
leng = leng-1

for i in range (0,3041):
    for j in range (0,((4056*3)+1),3):
        p = leng-((i*4056)+j)
        jj=j//3
        dd=data[p] + data[p-1] + data[p-2]
        if dd<150:
            d[jj][i][0]=0
        else:
            d[jj][i][0]= dd

n=1
for i in range (1,3041):
    for j in range (1,4057):
        if d[j][i][0]>0:
            if d[j-1][i][0]>0:
                d[j][i][1]=d[j-1][i][1]
            if d[j+1][i-1][0]>0:
                d[j][i][1]=d[j+1][i][1]
            if d[j][i-1][0]>0:
                d[j][i][1]=d[j][i-1][1]
            if d[j-1][i-1][0]>0:
                d[j][i][1]=d[j-1][i-1][1]
            if d[j][i][1]==0:
                d[j][i][1]=n
                n=n+1

s = np.empty(n+1)
v = np.empty(n+1)

for mm in range(1,n+1):
    s[mm]=0
    v[mm]=0

for i in range (1,3041):
    for j in range (1,4057):
        if d[j][i][0]>0:
            t = int(d[j][i][1])
            ss=s[t]
            vv=v[t]
            s[t]=ss+1
            v[t]=vv+ d[j][i][0]

save=0
vave=0
smax=0
vmax=0

for m in range(1,n+1):
    save=save+s[m]
    vave=vave+v[m]
    if s[m]>smax:
        smax=s[m]
    if v[m]>vmax:
        vmax=v[m]
m=0
if n>1:
    n=n-1
    m=n

save=save/n
vave=vave/n

print(txt5)
print ("group's area max: ",smax)
print ("group's value max: ",vmax)
print ("Average of group's Area: ",save)
print ("Average of group's values: " , vave)
print("number of groups: ", m)

f.close()





