'''To simulation the orbit of the planet

I don't take the real data in the program,for I think using my data can show the different way I use in this program

__author__      = "Ge Feng"
__student ID__  = "180001827"
__institution__ = "Peking University"
'''

import turtle as t
import math as m

mercury = t.Turtle()
venus = t.Turtle()
earth = t.Turtle()
mars = t.Turtle()
jupiter = t.Turtle()
sun = t.Turtle()
planet = [mercury,venus,earth,mars,jupiter]

mercury_pos = [0,100]#Although it seem like a man-made aircraft that flies away to the deep space
venus_pos = [0,90.0]
earth_pos = [0,100]
mars_pos = [0,40.0]
jupiter_pos = [0,60]

mercury_spe = [2,0]
venus_spe = [3,0]
earth_spe = [6,0]
mars_spe = [4,0]
jupiter_spe = [5,0]

ori_mercury_pos = [0,0]
ori_venus_pos = [0,0]
ori_earth_pos = [0,0]
ori_mars_pos = [0,0]
ori_jupiter_pos = [0,0]

ori_mercury_spe = [0,0]
ori_venus_spe = [0,0]
ori_earth_spe = [0,0]
ori_mars_spe = [0,0]
ori_jupiter_spe=[0,0]

pos = [mercury_pos,venus_pos,earth_pos,mars_pos,jupiter_pos]
spe = [mercury_spe,venus_spe,earth_spe,mars_spe,jupiter_spe]
count=[0,0,0,0,0]#To make sure the calibration won't happen when the planet orbit at the initial time
origin_pos = [ori_mercury_pos,ori_venus_pos,ori_earth_pos,ori_mars_pos,ori_jupiter_pos]
origin_spe = [ori_mercury_spe,ori_venus_spe,ori_earth_spe,ori_mars_spe,ori_jupiter_spe]
clo=['red','yellow','black','blue','green']

def calibration(i):
    '''To calibration the deviation during the orbit
    '''
    if(abs(pos[i][0]-origin_pos[i][0])<3 and abs(pos[i][1]-origin_pos[i][1])<3 and count[i]>10):
        count[i] = 0
        pos[i][0] = origin_pos[i][0]
        pos[i][1] = origin_pos[i][1]
        spe[i][0] = origin_spe[i][0]
        spe[i][1] = origin_spe[i][1]

def cal(a,b):
    '''To calculate what the next second's speed influenced by the gravitational
    '''
    dis2=a[0]*a[0]+a[1]*a[1]
    b[0]-=1000*a[0]/(dis2*m.sqrt(dis2))
    b[1]-=1000*a[1]/(dis2*m.sqrt(dis2))

def run(a,b,c):
    '''To go to the next second's postion
    '''
    a[0]+=b[0]
    a[1]+=b[1]
    c.goto(a[0],a[1])

for i in [0,1,2,3,4]:
    '''initialization
    '''
    planet[i].penup()
    planet[i].goto(pos[i][0],pos[i][1])
    planet[i].pendown()
    planet[i].color(clo[i])
    planet[i].shape('circle')
    planet[i].shapesize(0.1,0.1)
    for j in [0,1]:
        origin_pos[i][j]=pos[i][j]
        origin_spe[i][j]=spe[i][j]

sun.shape('circle')
sun.shapesize(1,1)
sun.color('orange')
scr=t.Screen()
scr.bgcolor('#191970')

while(True):
    '''orbit one by one'''
    for i in [0,1,2,3,4]:
        count[i]+=1
        calibration(i)
        cal(pos[i],spe[i])
        run(pos[i],spe[i],planet[i])
