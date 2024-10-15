import matplotlib.pyplot as plt
from matplotlib.widgets import Widget
import numpy as np
import math
import cmath
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from sympy import plot_implicit, Eq
from sympy.abc import x, y
from sympy import *
from sympy.plotting import plot, plot_implicit, plot_parametric
from math import pi
from time import sleep
from tqdm import tqdm

from rich import print



def mxp(x,b,m):
    x = np.linspace(0, 10, 11) # constructs a numpy array of [0.0, 1.0, ... 10.0]
    plt.plot(x, m*x+b, linestyle='solid')

    plt.show()




def cir(a,h,k):

    fig = plt.figure()
    ax = plt.gca()

    major_ticks = np.arange(0, 50, 5)
    minor_ticks = np.arange(0, 40, 5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')

    Drawing_colored_circle = plt.Circle(( a , h ), k )

    ax.add_artist( Drawing_colored_circle )
    plt.title( 'Colored Circle' )
    plt.show()




def ell(u,v,a,b):
    fig,ax = plt.subplots()
    t = np.linspace(0, 2*pi, 100)
    plt.grid(color='lightgray',linestyle='--')
    for i in tqdm(range(3)):
        sleep(.25)
    print("[bold orange]Center is: [/bold orange](", u, ",", v, ")")

    vert1 = u + a
    vert2 = u - a
    vert3 = v + b
    vert4 = v - b

    if a > b: # horizontal transverse axis

        #vertices
        print("[bold green]Vertices: [/bold green]\n(",vert1,",",v,")\n(",vert2,",",v,")")
        print("[bold green]Vertices: [/bold green]\n(",u,",",vert3,")\n(",u,",",vert4,")")

        foci = (a**2)-(b**2)

        fx1 = u - math.sqrt(foci)
        fx2 = u + math.sqrt(foci)
        print("[bold magenta]Foci: [/bold magenta]\n(",round(fx1,4), ",", v, ")\n(",round(fx2,4), ",", v, ")")
        print("(",u,"+-",u"\u221A", foci, ",", v, ")" )

        #foci
        plt.plot(fx1+.025*np.cos(t) , v+.025*np.sin(t) )
        plt.plot(fx2+.025*np.cos(t) , v+.025*np.sin(t) )

        #ellipse
        plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
        plt.show()
    elif b > a: # vertical transverse axis

        #vertices
        print("Vertices: \n(",vert1,",",v,")\n(",vert2,",",v,")")
        print("Vertices: \n(",u,",",vert3,")\n(",u,",",vert4,")")

        foci = (b**2)-(a**2)

        fy1 = v - math.sqrt(foci)
        fy2 = v + math.sqrt(foci)
        print("Foci: \n(", u, ",", round(fy2,4), ")\n(", u, ",", round(fy1,4), ")")
        print("(",u,",", v, "+-",u"\u221A", foci, ")" )

        #foci
        plt.plot( u+.025*np.cos(t) , (fy1+.025*np.sin(t) ))
        plt.plot( u+.025*np.cos(t) , (fy2+.025*np.sin(t) ))

        #ellipse
        plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
        plt.show()
    else:
        print("is circmle")





def parb(a,b):

    fig,ax = plt.subplots()

    # And a corresponding grid
    ax.grid(which='both')

    x = np.arange(a,b,1)

    y = x**2

    plt.plot(x,y)

    plt.show()

def hypb(c, a,b):
    if c == 2:
        plot_implicit(Eq(x**2/a- y**2, b), (x,-20,20))
    elif c == 1:
        plot_implicit(Eq(y**2/a- x**2, b), (x,-20,20))
    plt.show()


def loading():
    for i in tqdm(range(100)):
        sleep(.1)

print("[bold green]Welcome to the graphing calculator!\nWhat can i graph for you today?[/bold green]")
print("[bold magenta]1. MX+B \n2. Circles\n3. Ellipse\n4. Parabola\n5. Hyperbola[/bold magenta]")
choice1 = int(input("Enter: "))



if choice1 == 1:
    choice63 = int(input("M(slope): "))
    choice61 = int(input("X+__(if just x type 0): "))
    choice62 = int(input("B(y-intercept): "))
    mxp(choice61, choice62, choice63)
elif choice1 == 2:
    choice71 = int(input("A: "))
    choice72 = int(input("H: "))
    choice73 = int(input("K: "))
    cir(choice71, choice72, choice73)
elif choice1 == 3:
    choice81 = int(input("center x: "))
    choice82 = int(input("center y: "))
    choice83 = int(input("major axis length: "))
    choice84 = int(input("minor axis length: "))
    ell(choice81, choice82, choice83, choice84)
elif choice1 == 4:
    choice91 = int(input("Negative x: "))
    choice92 = int(input("Positive x: "))
    parb(choice91, choice92)
elif choice1 == 5:
    choice103 = int(input("1. Vertical 2. Horizontal: "))
    #choice104 = int(input("y: "))
    choice101 = int(input("A: "))
    choice102 = int(input("B: "))
    hypb(choice103, choice101, choice102)
elif choice1 == 100:
    loading()
else:
    print(choice1, "was not an option")
