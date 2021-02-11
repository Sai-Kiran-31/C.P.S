from mpl_toolkits.mplot3d import axes3d
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d
import matplotlib
from matplotlib.patches import FancyArrowPatch
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import style
import numpy as np
import tkinter

class DemoSplashScreen: 
    def __init__(self, parent): 
        self.parent = parent 
        self.aturSplash() 
        self.aturWindow() 

    def aturSplash(self): 
        self.gambar = Image.open('start.png')
        self.imgSplash = ImageTk.PhotoImage(self.gambar)

    def aturWindow(self):
        lebar, tinggi = self.gambar.size 
        setengahLebar = (self.parent.winfo_screenwidth()-lebar)//2 
        setengahTinggi = (self.parent.winfo_screenheight()-tinggi)//2
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setengahLebar,setengahTinggi))
        Label(self.parent, image=self.imgSplash).pack()


if __name__ == '__main__': 
    root = Tk()
    root.overrideredirect(True) 
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=700, mode='determinate') 
    progressbar.pack(side="bottom") 
    app = DemoSplashScreen(root) 
    progressbar.start()
    root.after(3010, root.destroy) 
    root.mainloop()


root = tkinter.Tk()

class Controller(tkinter.Frame):
    def __init__(self, parent):
        '''Initialises basic variables and GUI elements.'''
        frame = tkinter.Frame.__init__(self, parent,relief=tk.GROOVE,width=100,height=100,bd=1)

#root = tkinter.Tk()
root.geometry("700x600")
root.wm_title("C.P.S (Crystal Planes and Structures)")
root.wm_iconbitmap('1.ico')
root.maxsize(1400,1200)
root.minsize(700,600)

fig = Figure(figsize=(5, 4), dpi=100)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
ax = fig.add_subplot(111, projection='3d')
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()



ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

def plane1():
    A,B,C=[x,0,0,x],[0,y,0,0],[[0,0,z,0]]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([0,0,z,0])
    ax.plot_wireframe(A,B,C,color='red')
    ax.scatter(A,B,C)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    verts=[list(zip(A,B,D))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    #plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)
    

    


def great(h,k,l):
    global p
    if(h>k>l or h>l>k or h==k>l or h==l>k):
        p=h
    elif(k>h>l or k>l>h or k==h>l or k==l>h):
        p=k
    elif(h==k==l):
        p=h
    else:
        p=l
    
def great1(h,k,l):
    if(abs(h)>k>l or abs(h)>l>k or abs(h)>k==l or abs(h)==k>l or abs(h)==l>k):
         return h
    elif(k>abs(h)>l or k>l>abs(h) or k>abs(h)==l):
        return -k
    else:
        return -l




def great2(h,k,l):
    if(abs(k)>h>l or abs(k)>l>h or abs(k)>h==l or abs(k)==h>l or abs(k)==l>h):
         return k
    elif(h>abs(k)>l or h>l>abs(k) or h>abs(k)==l):
        return -h
    else:
        return -l

    


def great3(h,k,l):
    if(abs(l)>h>k or abs(l)>k>h or abs(l)>h==k or abs(l)==h>k or abs(l)==k>h):
         return l
    elif(h>abs(l)>k or h>k>abs(l) or h>abs(l)==k or h==abs(l)>k or h==k>abs(l)):
        return -h
    else:
        return -k


def great12(h,k,l):
    if(abs(h)>abs(k)>l or abs(h)>l>abs(k) or abs(h)>l==abs(k) or abs(h)==abs(k)>l):
        return h
    elif(abs(k)>abs(h)>l or abs(k)>l>abs(h) or abs(k)>l==abs(h) or abs(k)==abs(h)>l):
        return k
    else:
        return -l




def great23(h,k,l):
    if(abs(l)>abs(k)>h or abs(l)>h>abs(k) or abs(l)>h==abs(k) or abs(l)==abs(k)>h):
        return l
    elif(abs(k)>abs(l)>h or abs(k)>h>abs(l) or abs(k)>h==abs(l) or abs(k)==abs(l)>h):
        return k
    else:
        return -h





def great13(h,k,l):
    if(abs(l)>abs(h)>k or abs(l)>k>abs(h) or abs(l)>k==abs(h) or abs(l)==abs(h)>k):
        return l
    elif(abs(h)>abs(l)>k or abs(h)>k>abs(l) or abs(h)>k==abs(l) or abs(h)==abs(l)>k):
        return h
    else:
        return -k



def greatall(h,k,l):
    global p
    if(abs(h)>abs(k)>abs(l) or abs(h)>abs(l)>abs(k) or abs(h)==abs(k)>abs(l) or abs(h)==abs(l)>abs(k)):
        p=h
    elif(abs(k)>abs(h)>abs(l) or abs(k)>abs(l)>abs(h) or abs(k)==abs(h)>abs(l) or abs(k)==abs(l)>abs(h)):
        p=k
    elif(h==k==l):
        p=h
    else:
        p=l
def getvar():
    global n,a
    n=e.get()
    a=n.split(" ")
    a=[int(b) for b in a]


def getd():
    global n,a
    n=e3.get()
    a=n.split(" ")
    a=[int(b) for b in a]









def con():
    global x,y,z
    if(a[0]>0 and a[1]>0 and a[2]>0):
        s=a[0]*a[1]*a[2]
        x,y,z=s/a[0],s/a[1],s/a[2]
        great(x,y,z)




    if((a[0]==0 and a[1]!=0 and a[2]!=0)):
        s=abs(a[1]*a[2])
        y,z=int(s/a[1]),int(s/a[2])
        if(abs(y)>=abs(z)):
            x=abs(y)
        else:
            x=abs(z)


    if((a[0]!=0 and a[1]==0 and a[2]!=0)):
        s=abs(a[0]*a[2])
        x,z=int(s/a[0]),int(s/a[2])
        if(abs(x)>=abs(z)):
            y=abs(x)
        else:
            y=abs(z)



    if((a[0]!=0 and a[1]!=0 and a[2]==0)):
        s=abs(a[0]*a[1])
        x,y=int(s/a[0]),int(s/a[1])
        if(abs(x)>=abs(y)):
            z=abs(x)
        else:
            z=abs(y)


    if(a[0]!=0 and a[1]==0 and a[2]==0):
        x=a[0]

    if(a[0]==0 and a[1]!=0 and a[2]==0):
        y=a[1]


    if(a[0]==0 and a[1]==0 and a[2]!=0):
        z=a[2]


    if((a[0]<0 and a[1]>0 and a[2]>0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])

    if((a[0]>0 and a[1]<0 and a[2]>0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])



    if((a[0]>0 and a[1]>0 and a[2]<0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])


    if((a[0]<0 and a[1]<0 and a[2]>0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])



    if((a[0]>0 and a[1]<0 and a[2]<0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])




    if((a[0]<0 and a[1]>0 and a[2]<0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])
    


    if((a[0]<0 and a[1]<0 and a[2]<0)):
        s=abs(a[0]*a[1]*a[2])
        x,y,z=int(s/a[0]),int(s/a[1]),int(s/a[2])
        greatall(x,y,z)
    


def cube():
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()





def cube1():
    q=great1(x,y,z)
    
    
    p=abs(q)
    
    X, Y, Z = np.asarray([0,0,0,0,0,q,q,0,0,q,q,0,0,q,q,0,q,q,q,q]),np.asarray([0,p,p,0,0,0,p,p,p,p,0,0,p,p,p,p,p,p,0,0]),np.asarray([[0,0,p,p,0,0,0,0,p,p,p,p,p,p,0,0,0,p,p,0]])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()



def cube7():
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()



def cube2():
    q=great2(x,y,z)
    
    
    p=abs(q)
    X, Y, Z = (np.asarray([0,0,0,0,0,p,p,0,0,0,p,p,0,0,0,p,p,0,p,p,p]),
    np.asarray([0,0,q,q,0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q]),
    np.asarray([[0,p,p,0,0,0,p,p,0,0,0,0,0,p,p,p,p,p,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()



    
def cube3():
    
    q=great3(x,y,z)
  
    
    p=abs(q)
    X, Y, Z = (np.asarray([0,0,p,p,0,0,0,0,0,p,p,0,0,p,p,p,p,0,0,p]),
    np.asarray([0,p,p,0,0,0,p,p,0,0,0,0,0,0,p,p,0,0,p,p]),
    np.asarray([[0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q,q]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()






def cube4():
    
    q=great12(x,y,z)
   
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,q,q,q,q,0,0]),
    np.asarray([0,0,q,q,0,0,q,q,0,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,p,p,p,p,p,p,0,0,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()






def cube5():
    
    q=great23(x,y,z)
    
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,p,p,0,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()






def cube6():
    
    q=great13(x,y,z)
    
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([0,0,p,p,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    plane1()



def cubex():
    p=x
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



def cubey():
    p=y
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    
    A,B,C=[x,x,0,0,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)





def cubez():
    p=z
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,0,0,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)




def cubex1():
    q=-x
    
    p=abs(q)
    
    X, Y, Z = (np.asarray([0,0,0,0,0,p,p,0,0,0,p,p,0,0,0,p,p,0,p,p,p]),
    np.asarray([0,0,q,q,0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q]),
    np.asarray([[0,p,p,0,0,0,p,p,0,0,0,0,0,p,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    ax.plot_wireframe(X, Y, Z)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def cubex2():
    q=-x
    
    p=abs(q)
    
    X, Y, Z = (np.asarray([0,0,p,p,0,0,0,0,0,p,p,0,0,p,p,p,p,0,0,p]),
    np.asarray([0,p,p,0,0,0,p,p,0,0,0,0,0,0,p,p,0,0,p,p]),
    np.asarray([[0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q,q]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)





def cubex3():
    q=-x
    
    p=abs(q)
    
    X, Y, Z =( np.asarray([0,p,p,0,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)

def cubey1():
    q=-y
    
    p=abs(q)
    
    X, Y, Z = np.asarray([0,0,0,0,0,q,q,0,0,q,q,0,0,q,q,0,q,q,q,q]),np.asarray([0,p,p,0,0,0,p,p,p,p,0,0,p,p,p,p,p,p,0,0]),np.asarray([[0,0,p,p,0,0,0,0,p,p,p,p,p,p,0,0,0,p,p,0]])
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,x,0,0,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)




def cubey2():
    q=-y
    
    p=abs(q)
    
    X, Y, Z = (np.asarray([0,0,p,p,0,0,0,0,0,p,p,0,0,p,p,p,p,0,0,p]),
    np.asarray([0,p,p,0,0,0,p,p,0,0,0,0,0,0,p,p,0,0,p,p]),
    np.asarray([[0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q,q]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,x,0,0,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)





def cubey3():
    q=-y
    
    p=abs(q)
    
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([0,0,p,p,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)




def cubez1():
    q=-z
    
    p=abs(q)
    
    X, Y, Z = np.asarray([0,0,0,0,0,q,q,0,0,q,q,0,0,q,q,0,q,q,q,q]),np.asarray([0,p,p,0,0,0,p,p,p,p,0,0,p,p,p,p,p,p,0,0]),np.asarray([[0,0,p,p,0,0,0,0,p,p,p,p,p,p,0,0,0,p,p,0]])
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,0,0,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)





def cubez2():
    q=-z
    
    p=abs(q)
    
    X, Y, Z = (np.asarray([0,0,0,0,0,p,p,0,0,0,p,p,0,0,0,p,p,0,p,p,p]),
    np.asarray([0,0,q,q,0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q]),
    np.asarray([[0,p,p,0,0,0,p,p,0,0,0,0,0,p,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,0,0,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def cubez3():
    q=-z
    
    p=abs(q)
    
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,q,q,q,q,0,0]),
    np.asarray([0,0,q,q,0,0,q,q,0,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,p,p,p,p,p,p,0,0,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[0,y,y,0,0],[z,0,0,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)




def cubex0():
    y,z=x,x
    p=x
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,x,x,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



def cubex_0():
    y,z=x,x
    p=x
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,x,x,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)

def cubey0():
    x,z=y,y
    p=y
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,x,x,0,0],[y,y,y,y,y],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



def cubey_0():
    x,z=y,y
    p=x
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,0,x,x,0],[y,y,y,y,y],[0,z,z,0,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



def cubez0():
    y,x=z,z
    p=z
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[0,x,x,0,0],[0,0,y,y,0],[z,z,z,z,z]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def cubez_0():
    x,y=z,z
    p=x
    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    #ax.plot_wireframe(X, Y, Z)
    A,B,C=[x,x,x,x,x],[0,y,y,0,0],[0,0,z,z,0]
    A=np.asarray(A)
    B=np.asarray(B)
    C=np.asarray(C)
    D=np.asarray([C])
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(A,B,D,color='red')
    ax.scatter(A,B,C)
    verts=[list(zip(A,B,C))]
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#80007a')
    plt.gca().add_collection3d(srf)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


def d1():
    
    

    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)




def dx():
    q=great1(x,y,z)
   
    
    p=abs(q)
    
    X, Y, Z = np.asarray([0,0,0,0,0,q,q,0,0,q,q,0,0,q,q,0,q,q,q,q]),np.asarray([0,p,p,0,0,0,p,p,p,p,0,0,p,p,p,p,p,p,0,0]),np.asarray([[0,0,p,p,0,0,0,0,p,p,p,p,p,p,0,0,0,p,p,0]])
    ax.clear()
    
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def dy():
    q=great2(x,y,z)
    
    
    p=abs(q)
    X, Y, Z = (np.asarray([0,0,0,0,0,p,p,0,0,0,p,p,0,0,0,p,p,0,p,p,p]),
    np.asarray([0,0,q,q,0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q]),
    np.asarray([[0,p,p,0,0,0,p,p,0,0,0,0,0,p,p,p,p,p,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def dz():
    q=great3(x,y,z)
   
    p=abs(q)
    X, Y, Z = (np.asarray([0,0,p,p,0,0,0,0,0,p,p,0,0,p,p,p,p,0,0,p]),
    np.asarray([0,p,p,0,0,0,p,p,0,0,0,0,0,0,p,p,0,0,p,p]),
    np.asarray([[0,0,0,0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q,q]]))
    ax.clear()
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


def dxy():
    q=great12(x,y,z)
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,q,q,q,q,0,0]),
    np.asarray([0,0,q,q,0,0,q,q,0,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,p,p,p,p,p,p,0,0,p,p,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)



def dyz():
    q=great23(x,y,z)
   
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,p,p,0,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([0,0,q,q,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    ax.clear()
    
    

    X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)

def dzx():
    q=great13(x,y,z)
   
    
    p=abs(q)
    X, Y, Z =( np.asarray([0,q,q,0,0,0,0,q,q,0,0,0,q,q,q,q]),
    np.asarray([0,0,p,p,0,0,p,p,0,0,p,p,p,p,0,0]),
    np.asarray([[0,0,0,0,0,q,q,q,q,q,q,0,0,q,q,0]]))
    ax.clear()
    ax.plot_wireframe(X, Y, Z)
    a=Arrow3D([0,x],[0,y],[0,z],mutation_scale=30,lw=3,arrowstyle="-|>",color="r")
    ax.add_artist(a)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)

    






def directions():
    con()
    if(a[0]>0 and a[1]>0 and a[2]>0):
        d1()

    if(a[0]<0 and a[1]>0 and a[2]>0):
        dx()



    if(a[0]>0 and a[1]<0 and a[2]>0):
        dy()


    if(a[0]>0 and a[1]>0 and a[2]<0):
        dz()



    if(a[0]<0 and a[1]<0 and a[2]>0):
        dxy()



    if(a[0]>0 and a[1]<0 and a[2]<0):
        dyz()


    if(a[0]<0 and a[1]>0 and a[2]<0):
        dzx()





    if(a[0]<0 and a[1]<0 and a[2]<0):
        d1()    
    


def graph():
    con()
    if(a[0]==0 and a[1]>0 and a[2]>0):
        cubex()


    if(a[0]>0 and a[1]==0 and a[2]>0):
        cubey()



    if(a[0]>0 and a[1]>0 and a[2]==0):
        cubez()


    if(a[0]==0 and a[1]<0 and a[2]>0):
        cubex1()

    if(a[0]==0 and a[1]>0 and a[2]<0):
        cubex2()


    if(a[0]==0 and a[1]<0 and a[2]<0):
        cubex3()

    if(a[0]>0 and a[1]==0 and a[2]==0):
        cubex0()


    if(a[0]<0 and a[1]==0 and a[2]==0):
        cubex_0()


    if(a[0]==0 and a[1]>0 and a[2]==0):
        cubey0()

    if(a[0]==0 and a[1]<0 and a[2]==0):
        cubey_0()

    if(a[0]==0 and a[1]==0 and a[2]>0):
        cubez0()


    if(a[0]==0 and a[1]==0 and a[2]<0):
        cubez_0()

    if(a[0]<0 and a[1]==0 and a[2]>0):
        cubey1()

    if(a[0]>0 and a[1]==0 and a[2]<0):
        cubey2()


    if(a[0]<0 and a[1]==0 and a[2]<0):
        cubey3()


    if(a[0]<0 and a[1]>0 and a[2]==0):
        cubez1()


    if(a[0]>0 and a[1]<0 and a[2]==0):
        cubez2()

    if(a[0]<0 and a[1]<0 and a[2]==0):
        cubez3()

    if(a[0]>0 and a[1]>0 and a[2]>0):
        cube()

    if(a[0]<0 and a[1]>0 and a[2]>0):
        cube1()



    if(a[0]>0 and a[1]<0 and a[2]>0):
        cube2()


    if(a[0]>0 and a[1]>0 and a[2]<0):
        cube3()



    if(a[0]<0 and a[1]<0 and a[2]>0):
        cube4()



    if(a[0]>0 and a[1]<0 and a[2]<0):
        cube5()


    if(a[0]<0 and a[1]>0 and a[2]<0):
        cube6()





    if(a[0]<0 and a[1]<0 and a[2]<0):
        cube7()
def Diamond():
     p=1
     q=p/2
     r=p/4
     s=3*r

     X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
     
     X1,Y1,Z1=(np.asarray([q,0,q,p,q,q]),
               np.asarray([0,q,p,q,q,q]),
               np.asarray([[q,q,q,q,0,p]]))

     X2,Y2,Z2=(np.asarray([s,r,s,r]),
               np.asarray([s,r,r,s]),
               np.asarray([[r,r,s,s]]))


     X3,Y3,Z3=(np.asarray([0,r,q,s,p,s,p,s,p,s,q,r,0,r,0,r,q,s,q,r,q,s]),
               np.asarray([0,r,0,r,0,r,q,s,p,s,q,r,q,s,p,s,q,r,q,s,p,s]),
               np.asarray([[0,r,q,s,p,s,q,r,0,r,0,r,q,s,p,s,p,s,p,s,q,r]]))
     
     ax.clear()
     ax.plot_wireframe(X, Y, Z)
     ax.plot_wireframe(X3,Y3,Z3,linewidth=5)
     ax.scatter(X,Y,Z,s=250,color="blue")
     ax.scatter(X1,Y1,Z1,s=250,color="blue",label="C")
     ax.scatter(X2,Y2,Z2,s=250,color="blue")
     
     
     ax.legend(fontsize=10)
     canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)
def structure():
     p=1
     q=p/2
     r=p/4
     s=3*r

     X, Y, Z = (np.asarray([0,p,p,0,0,0,0,0,p,p,0,p,p,0,p,p]),
               np.asarray([0,0,p,p,0,0,p,p,p,p,p,p,0,0,0,0]),
               np.asarray([[0,0,0,0,0,p,p,0,0,p,p,p,p,p,p,0]]))
     
     X1,Y1,Z1=(np.asarray([q,0,q,p,q,q]),
               np.asarray([0,q,p,q,q,q]),
               np.asarray([[q,q,q,q,0,p]]))

     X2,Y2,Z2=(np.asarray([s,r,s,r]),
               np.asarray([s,r,r,s]),
               np.asarray([[r,r,s,s]]))


     X3,Y3,Z3=(np.asarray([0,r,q,s,p,s,p,s,p,s,q,r,0,r,0,r,q,s,q,r,q,s]),
               np.asarray([0,r,0,r,0,r,q,s,p,s,q,r,q,s,p,s,q,r,q,s,p,s]),
               np.asarray([[0,r,q,s,p,s,q,r,0,r,0,r,q,s,p,s,p,s,p,s,q,r]]))
     ax.clear()
     ax.plot_wireframe(X, Y, Z)
     ax.scatter(X,Y,Z,s=150,color="red")
     ax.scatter(X1,Y1,Z1,s=150,color="red",label=e1.get())
     ax.scatter(X2,Y2,Z2,s=250,color="blue",label=e2.get())
     ax.plot_wireframe(X3,Y3,Z3,linewidth=5)
     ax.legend(fontsize=10)
     canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0,padx=70)


    
nb=ttk.Notebook(root)
nb.pack()
page1=ttk.Frame(nb)
nb.add(page1,text="Miller Indices")
page2=ttk.Frame(nb)
nb.add(page2,text="Structures")
page3=ttk.Frame(nb)
nb.add(page3,text="Diamond")
page4=ttk.Frame(nb)
nb.add(page4,text="Directions")
l=Label(page1,text="Enter Miller indices",font=("Bold"))
l.pack()
l4= Label(page1,text="note: format is h<space>k<space>l<space>")
l4.pack()
l4=Label(page4,text="Enter Miller indices",font=("Bold"))
l5= Label(page4,text="note: format is h<space>k<space>l<space>")
l4.pack()
l5.pack()
e=Entry(page1)
e.pack()
e3=Entry(page4)
e3.pack()
w=Button(page1,text="set values",command=getvar)
w.pack()

g=Button(page1,text="graph",command=graph)
g.pack()

dia=Button(page3,text="Diamond",command=Diamond)
dia.pack(padx=20)
l1=Label(page2,text="Enter Atom 1")
l1.pack()
e1=Entry(page2)
e1.pack()
l2=Label(page2,text="Enter Atom 2")
l2.pack()
e2=Entry(page2)
e2.pack()
structure=Button(page2,text="show structure",command=structure)
structure.pack()
w1=Button(page4,text="set values",command=getd)
w1.pack()
g1=Button(page4,text="graph",command=directions)
g1.pack()


tkinter.mainloop()
