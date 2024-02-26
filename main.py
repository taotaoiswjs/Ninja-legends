#游戏规则：
#玩家1：w键跳,a,d键前进后退,s键发射武器
#玩家2：上键跳,左,右键前进后退,下键发射武器
from pgzrun import *

WIDTH = 1280
HEIGHT = 720
#创建背景和游戏准备界面
bg = Actor("bg.png")
ready = Actor("ready.png")
#游戏准备的状态变量,两个角色的初始速度变量和跳跃状态变量
state = "准备"

jump_speed1 = 12
jump1 = False
jump_speed2 = 12
jump2 = False

life_show1 = Actor("life_show1.png", [120, 50])
shoot1 = False

life_show2 = Actor("life_show2.png", [1150, 50])
shoot2 = False

win_1 = Actor("win_1.png", [3000, 360])
win_2 = Actor("win_2.png", [3000, 360])

#作答区域创意区:可修改两个角色的图片
ninja1 = Actor("ninja1.png", [200, 500]) 
ninja2 = Actor("ninja2.png", [1080, 500]) 

#作答区域创意区:可修改两个飞镖的图片
dart1 = Actor("dart1.png", [1500, 300])
dart2 = Actor("dart2.png", [1500, 300])

#作答区域创意区:可修改两个角色的初始血量
life1 = 20
life2 = 20

def draw():
    bg.draw()

    ninja1.draw()
    ninja2.draw()
    dart1.draw()
    dart2.draw()
    
    life_show1.draw()
    life_show2.draw()
    screen.draw.text(str(life1), [120, 32], color='white', fontsize=35,fontname="ziti.ttf")
    screen.draw.text(str(life2), [1120, 32], color='white', fontsize=35,fontname="ziti.ttf")
    ready.draw()
    win_1.draw()
    win_2.draw()

def update():
    global jump1, jump_speed1, jump2, jump_speed2, shoot1, shoot2, life1, life2 ,state
    if state == "准备":
        if keyboard.space == True:
            state = "开始"
            ready.left = 3000
    if state == "开始":
        #ninja1的跳跃逻辑
        if keyboard.w == True:
            jump1 = True
        if jump1 == True:
            ninja1.y = ninja1.y - jump_speed1
            jump_speed1 = jump_speed1 - 0.28
    
            if ninja1.bottom > 600:
                ninja1.bottom = 600
                jump1 = False  
                jump_speed1 = 12 
        if keyboard.a == True:
            ninja1.x = ninja1.x - 6
        elif keyboard.d == True:
            ninja1.x = ninja1.x + 6
        
        
        #作答区域创意区:可修改两个武器的旋转角度(改变数字大小即可)
        dart1.angle = dart1.angle + 8
        dart2.angle = dart2.angle + 8
        
        #ninja1的飞镖发射以及输赢规则
        if keyboard.s == True:
            sounds.shoot.play()
            shoot1 = True
            dart1.x = ninja1.x + 75
            dart1.y = ninja1.y - 20
            
        if shoot1 == True:
            #作答区域创意区:可修改武器的射速(改变数字大小)
            dart1.x = dart1.x + 18
            
        if dart1.colliderect(ninja2):
            #作答区域创意区:可以增加武器的威力(改变数字大小)
            life2 = life2 - 1
            sounds.hit.play()
            dart1.left = 2000
        #作答区域创意区,设置不同的获胜条件,让life2等于其他数字时游戏结束
        if life2 == 0:
            state = "结束"
            win_1.left = 0
            
        # ---------------------------------------------------------------------------------------------------------------#
        #ninja2的跳跃逻辑
        if keyboard.up == True:
            jump2 = True
        
        if jump2 == True:
            ninja2.y = ninja2.y - jump_speed2
            jump_speed2 = jump_speed2 - 0.28
    
            if ninja2.bottom > 600:
                ninja2.bottom = 600
                jump2 = False
                jump_speed2 = 12
        
        if keyboard.left == True:
            ninja2.x = ninja2.x - 6
        elif keyboard.right == True:
            ninja2.x = ninja2.x + 6
        
        #ninja2的飞镖发射以及输赢规则
        if keyboard.down == True:
            sounds.shoot.play()
            shoot2 = True
            dart2.x = ninja2.x - 50
            dart2.y = ninja2.y 
        if shoot2 == True:
            #作答区域创意区:可修改武器的射速(改变数字大小)
            dart2.x = dart2.x - 18
            
        if dart2.colliderect(ninja1):
            #作答区域创意区:可以增加武器的威力(改变数字大小)
            life1 = life1 - 1
            sounds.hit.play()
            dart2.right = -1000
        #作答区域创意区,设置不同的获胜条件,让life1等于其他数字时游戏结束
        if life1 == 0:
            win_2.left = 0
            state = "结束"
            
go()
