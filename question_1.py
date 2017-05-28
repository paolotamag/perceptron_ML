# 1536242 - Paolo Tamagnini
#paolotamag@gmail.com

import numpy as np
import matplotlib.pyplot as plt

x1_vector = np.array([0.15,0.2,0.45,0.65,0.65,0.85,0.95,1.05])
x2_vector = np.array([0.75,0.4,0.65,0.95,0.15,1.0,0.55,0.25])

x1_list = [str(x) for x in list(x1_vector)]
x2_list = [str(x) for x in list(x2_vector)]
y_vector = np.array([1,1,1,-1,1,-1,-1,-1])

for x in zip(x1_list,x2_list,y_vector):
    print "x1:"+str(x[0]),"| x2:"+str(x[1]),"| y:"+str(x[2])

color_y = []
for y in y_vector:
    if y == 1:
        color_y.append('white')
    else:
        color_y.append('black')

P = len(x1_vector)
x_matrix = np.zeros((P,2))
for i in range(0,P):
    for j in range(0,2):
        if j == 0:
            x_matrix[i,j] = x1_vector[i]
        elif j == 1:
            x_matrix[i,j] = x2_vector[i]
        else:
            print 'error'        
print     
stop = int(input("please insert the desired maximum number of updates:"))        
        
omega = np.array([1,-1])
b = 0.2
cc = 0
k = 0
omega_list = []
b_list = []
omega_list.append(omega)
b_list.append(b)
while cc < P :
    for i in range(0,P):
        
        t = b + np.dot(omega,x_matrix[i,:])
        
        if t >= 0:
            sgn = 1
        elif t < 0:
            sgn = -1
        else:
            print 'error'
            
        if y_vector[i]*(sgn) <= 0:
            omega = omega + y_vector[i]*x_matrix[i,:]
            omega_list.append(omega)
            b = b + y_vector[i]
            b_list.append(b)
            k = k + 1
            if k == stop:
                break


        else:
            cc +=1
    
    if cc < P:
        cc = 0
    if k == stop:
        break
for j in range(0,len(omega_list)):    

    plt.scatter(x1_vector,x2_vector, c=color_y, s=list(np.repeat(100,8)))
    
    plt.ylim([-1,2])
    plt.xlim([-1,2])
    
    for i in range(0,8):
        plt.annotate((x1_list[i],x2_list[i]),(x1_vector[i]+0.01,x2_vector[i]-0.02), fontsize=10)
        
    x_for_line = np.array(range(-10,21))/float(10)
    
    yfit1 = [-b_list[j]/omega_list[j][1] - omega_list[j][0]/omega_list[j][1] * xi for xi in x_for_line]
    yfit2 = [-b_list[j]/omega_list[j][0] - omega_list[j][1]/omega_list[j][0] * xi for xi in x_for_line]
    
    x1_for_line = np.concatenate((x_for_line,yfit2))
    x2_for_line = np.concatenate((yfit1,x_for_line))
    plt.plot(x1_for_line,x2_for_line)
    
    lenxArrow = 0.1
    pointOnLine = (x_for_line[15], yfit1[15])
    
    coeffArrow = -1/(-omega_list[j][0]/omega_list[j][1])
    interceptArrow = -coeffArrow*pointOnLine[0] + pointOnLine[1]
    
    tipArrow = (pointOnLine[0]+lenxArrow,coeffArrow*(pointOnLine[0]+lenxArrow)+interceptArrow)
    
    if ( b_list[j] + omega_list[j][0] * tipArrow[0]   + omega_list[j][1] * tipArrow[1] )< 0:
        lenxArrow = - lenxArrow
        tipArrow = (pointOnLine[0]+lenxArrow,coeffArrow*(pointOnLine[0]+lenxArrow)+interceptArrow)
        

    ax = plt.axes()
    
    ax.arrow(pointOnLine[0], pointOnLine[1], tipArrow[0]-pointOnLine[0], tipArrow[1]-pointOnLine[1], head_width=0.02, head_length=0.05, fc='k', ec='k')
    

    plt.title("1536242 - step: " + str(j))
    plt.show()
print
for i in range(0,len(omega_list)):
    print "step",i,": w_1=",omega_list[i][0],"| w_2=",omega_list[i][1],"| b=",b_list[i]
print
print "# of lines: ",k +1
if cc == P:
    print "a solution was found"
else:
    print "no solution found"