#!/usr/bin/env python3

"""
Made by 
Samarth Chauhan
2018410
B-3
"""

from copy import deepcopy
from math import cos,sin,radians
import matplotlib.pyplot as plt
from matplotlib import patches

#this class will do transformation on polygon
class Transformation_polymer(object):
    #to scale cordinates of polygon
    def Scale(self,cordiante_S,Scale_x,Scale_y):
        #scaler multiplication matrix
        Scale_matrix=[[Scale_x,0],
                    [0,Scale_y]]
        #to store result matix multiplication
        result=[[0,0,0,0],[0,0,0,0]]
        #matrix multiplication
        for i in range(0,2):
            for j in range(0,4):
                for k in range(0,2):
                    result[i][j]+=round(Scale_matrix[i][k]*cordiante_S[k][j],2)   
        return result

    #to rotate polygon (it only creates matrix by matrix multiplication)
    def Rotate(self,cordinate_R,theta):          
        #rotational matrix       
        rotate_matrix=[[cos(radians(theta)),-sin(radians(theta))],
                    [sin(radians(theta)),cos(radians(theta))]]
        #to store result matix multiplication
        result=[[0,0,0,0],[0,0,0,0]]
        #matrix multiplication
        for i in range(0,2):
            for j in range(0,4):
                for k in range(0,2):
                    result[i][j]+=round(rotate_matrix[i][k]*cordinate_R[k][j],2)
        return result

    #to translate center of polygon (it only creates matrix by matrix multiplication)
    def Tranlate(self,cordinate_T,Dx,Dy):
        #tranlational matrix
        transform_matrix=[[1,0,Dx],
                        [0,1,Dy],
                        [0,0,0]]
        #cordinate matix
        cordinate_T=[cordinate_T[0],
                    cordinate_T[1],
                    [1,1,1,1]]
        #to store result matix multiplication
        result=[[0,0,0,0],[0,0,0,0]]
        #matrix multiplication
        for i in range(0,2):
            for j in range(0,4):
                for k in range(0,3):
                    result[i][j]+=round(transform_matrix[i][k]*cordinate_T[k][j],2)    
        return result
    
    #to draw polygon
    def Draw(self,cordinate_D):
        #to create separate matrix for plotting
        x_cordinate=[]
        y_cordinate=[]
        #to separate x and y axis cordinate from cordinate
        for axis in range(1):
            for point in range(0,4):
                x_cordinate.append(cordinate_D[axis][point])
                y_cordinate.append(cordinate_D[axis+1][point])        
        #these are the separate matrix for x and y axis 
        x_cordinate.append(cordinate_D[0][0])
        y_cordinate.append(cordinate_D[1][0])
        #to draw grid
        plt.grid(b=None, which='major', axis='both')
        #to plot polygon
        plt.plot(x_cordinate,y_cordinate)
        #to show plot on screen 
        plt.show()

#class to apply transformation on ellipse
class Transformation_disc(object):
    #to scale axis of ellipse (it only creates matrix)
    def Scale(self,centre,scale_x,scale_y):  
        
        #to store result matix multiplication
        result=[0,0,0,0,0]
        
        #if the ellipse is more towars x axis then simple scaling will be applicable
        if (centre[4]<=45 and centre[4]>=0) or (centre[4]>135 and centre[4]<225) or (centre[4]>=315 and centre[4]<360):
            #scaler matrix      
            scale_matrix=[1,1,scale_x,scale_y,1]
            #matrix multiplication
            for i in range(0,5):
                result[i]+=round(scale_matrix[i]*centre[i],2)    
        
        #if the ellipse is rotated more towards y axis then we have to multiply x by scale_y and y by scale_y
        else:
            #scaler matrix      
            scale_matrix=[1,1,scale_y,scale_x,1]
            #matrix multiplication
            for i in range(0,5):
                result[i]+=round(scale_matrix[i]*centre[i],2)
        return result

    #to rotate ellipse (it only creates matrix)
    def Rotate(self,cordinates,angle):    
        angle=float(angle)      
        if cordinates[4]!=0:
            #to make angle positive
            if (angle)<0:
                angle=360+angle
           
            #rotational matrix
            rotate_matrix=[1,1,1,1,((angle+cordinates[4])/cordinates[4])]    
            #to store result matix multiplication
            result=[0,0,0,0,0]
            
            #matrix multiplication
            for i in range(0,5):
                result[i]+=round(cordinates[i]*rotate_matrix[i],2)            
            
            if result[4]>360:
                result[4]=360-result
            return result
        else:
            #to make angle positive
            if (angle)<0:
                angle=360+angle
            #if the angle is zero then we just have to add angle to angle variable in cordinate list
            result=deepcopy(cordinates)
            result[4]+=round(angle,2)
            return result
        
    #to tranlate center of ellipse (it only creates matrix)
    def Tranlate(self,centre,x,y):
        #to multiply matrix if and only if centre of ellipse if not at origin
        if centre[0]!=0 and centre[1]!=0:
            #transformation matrix
            translate_matrix=[((int(x)+centre[0])/centre[0]),((int(y)+centre[1])/centre[1]),1,1,1]
            #to store result matix multiplication
            result=[0,0,0,0,0]     
            #matrix multiplication  
            for i in range(0,5):
                result[i]+=round(centre[i]*translate_matrix[i],2)        
            return result
        #to simply add cordinate to center of ellipse if it is at origin 
        else:
            result=deepcopy(centre)
            result[0]+=round(int(x),2)
            result[1]+=round(int(y),2)
            return result

    #to draw circle and ellipse
    def Draw(self,cordinate):
        #to draw grid
        plt.grid(b=None, which='major', axis='both')
        #to draw ellipse on the basis of cordinate
        ellipse=patches.Ellipse((cordinate[0],cordinate[1]),width=cordinate[2],height=cordinate[3],angle=cordinate[4],linewidth=1,fill=False)
        ax=plt.gca()
        ax.add_patch(ellipse)
        plt.axis('scaled')
        #to show ellipse on screen
        plt.show()


if __name__ == "__main__":    
    
    #to get input for shape
    shape=input()
   
    #to all transformation applied by user
    finaldata=[]  

    if shape=="polygon":

        #data is the instance of class Transformation_polymer
        data=Transformation_polymer()

        #list to store vertices
        vertices_x=list(map(int,input().split()))       
        vertices_y=list(map(int,input().split()))
        #to make cordinates of polygon 
        cordi=[vertices_x,vertices_y]
        
               
        
        #to initilize choice
        choice="test"

        #to take input until choice equals to quit    
        while choice!="quit":
            choice=input()
            #to do scaling if choice is S
            if choice[0]=="S":
                choice,Scale_x,Scale_y=choice.split(" ")
                Scale_x,Scale_y=int(Scale_x),int(Scale_y)  
                cordi=deepcopy(data.Scale(cordi,Scale_x,Scale_y))
                finaldata.append(cordi)

            #to do rotation if choice is R
            elif choice[0]=="R":
                choice,theta=choice.split(" ")
                theta=int(theta)
                cordi=deepcopy(data.Rotate(cordi,theta))
                finaldata.append(cordi)

            #to do translational if choice is T
            elif choice[0]=="T":
                choice,trans_x,trans_y=choice.split(" ")
                trans_x,trans_y=int(trans_x),int(trans_y)
                cordi=deepcopy(data.Tranlate(cordi,trans_x,trans_y))
                finaldata.append(cordi)

            else:
                pass

    

        print("\n")
        #loop for printing values
        data.Draw([vertices_x,vertices_y])
        for outter in range(0,len(finaldata)):
            data.Draw(finaldata[outter])
            for middle in range(0,2):
                for inner in range(0,4):
                    print(finaldata[outter][middle][inner],end=" ")
                print("\n",end="")
            print("\n")
    
    elif shape=="disc":
        #data is the instance of class Transformation_disc
        data=Transformation_disc()
        #input to get cordinates of orignal ellipse
        center_x,center_y,width=map(int,input().split(" "))        
        cordi=[center_x,center_y,width*2,width*2,0]
        startpoint=cordi

        #to initilize choice
        choice="test"  

        #to take input until choice equals to quit  
        while choice!="quit":

            choice=input()
            #to do scaling if choice is S
            if choice[0]=="S":
                choice,Scale_x,Scale_y=choice.split(" ")
                Scale_x,Scale_y=int(Scale_x),int(Scale_y)
                cordi=deepcopy(data.Scale(cordi,Scale_x,Scale_y))
                finaldata.append(cordi)

            #to do rotation if choice is R
            elif choice[0]=="R":
                choice,theta=choice.split(" ") 
                cordi=deepcopy(data.Rotate(cordi,theta))            
                finaldata.append(cordi)

            #to do translational if choice is T
            elif choice[0]=="T":
                choice,trans_x,trans_y=choice.split(" ")
                trans_x,trans_y=int(trans_x),int(trans_y)
                cordi=deepcopy(data.Tranlate(cordi,trans_x,trans_y))
                finaldata.append(cordi)

            else:
                pass
           
    
        print("\n")
        #to print first and orignal ellipse
        data.Draw(startpoint)

        #loop for printing values
        for outter in range(0,len(finaldata)):  
            #print(finaldata[outter])     
            data.Draw(finaldata[outter])            
            for inner in range(0,3):
                print(finaldata[outter][inner],end=" ")
            #to print both radii if they are not equal
            if finaldata[outter][2]!=finaldata[outter][3]:
                print(finaldata[outter][3],end=" ")
            print("\n")
           
         
    else:
        print("enter valid shape")
        exit()
    
    


   
