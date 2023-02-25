#author: hammy

from pyautogui import *
import pyautogui
import time
import os
import keyboard
import random
import win32api, win32con
import win32com.client as comclt
import subprocess

#This is for educational and historical purposes only. any use/redistribution or alteration is not my responsibility or liability
#This was a project I made for fun, there are many ways I have already improved it, and many ways it has yet to be improved.
contx = 0
xDead = 432
xOff = 820
yOff = 480
invx =27
tcount = 13
instance_count = 0
tr = 0
# Find the location of the BlueStacks window on the screen
print('starting bot now')    
print('press esc to quit')
#define a "click" action using win32 api
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while (keyboard.is_pressed('esc')== False):
    def open_bluestacks_instances():
        # Kill any existing BlueStacks tasks
        subprocess.call("taskkill /im HD-Player.exe /f", shell=True)
        subprocess.call("taskkill /im HD-MultiInstanceManager.exe /f", shell=True)
        subprocess.call("WMIC PROCESS WHERE name='HD-Player.exe' CALL TERMINATE", shell=True)
        subprocess.call("WMIC PROCESS WHERE name='HD-MultiInstanceManager.exe' CALL TERMINATE", shell=True)

        # Wait for tasks to be killed
        time.sleep(4)
        
        #replace all quotes with your values
        instances = ["Nougat32_x", "Nougat32_x", "Nougat32_x", "Nougat32_2", "Nougat32_x"]
        for i, instance in enumerate(instances):
            subprocess.Popen(f"C:/Program Files/BlueStacks_nxt/HD-Player.exe --instance {instance} --cmd launchApp --package sts.pl")
            time.sleep(1)
        subprocess.run("C:/Program Files\BlueStacks_nxt/HD-MultiInstanceManager.exe")
        time.sleep(20)

    splitTime = 0

    number = random.uniform(0.05,0.1)
    numtype = random.uniform(0.08, 0.1)
    def hostMap():
        click(562,23)
        #click map after confirming home state by continue button
        click(476,63)
        time.sleep(0.8)
        #click host
        click(210,433)
        time.sleep(number)

        #click "back" to find map, range(x) x being the map you want
        for i in range(1):
            click(277,134)
        time.sleep(number)
        click(660,300)
        
        #click password
        click(92,436)
        time.sleep(number)

        #type password
        pyautogui.write('He456llo World!', numtype)

        #enter password
        click(759,48)
        time.sleep(number)

        #click create map
        click(359,440)
        
  
    def spawn():
        for i in range(6):
            
            # x and y will vary map to map.
            x = 0
            y = 0
            click (x,y)
            time.sleep(.01)
            click (x+xOff,y)
            time.sleep(.01)
            click (x+xOff,y+yOff)
            time.sleep(.01)
            click (x,y+yOff)
            time.sleep(.01)
            click (x,y+yOff+yOff)
            time.sleep(0.3)
        
    def inviteLobby():
        #invite alternate accounts
        #friend menu (gear) X:   15 Y:   44 RGB: (105, 174, 222)
        time.sleep(.2)
        click (23,63)
        time.sleep(.6)
        click (517,69)
        time.sleep(.1)
        time.sleep(number)
        
        click (267,211)
        time.sleep(.1)
        time.sleep(number)
        click (273,282)
        time.sleep(.1)
        time.sleep(number)
        click (237,352)
        time.sleep(.1)
        time.sleep(number)
        click (261,410)
        
    def joinLobby():
        #join on alts
        #alt friend loctions:
        #TR X: 1208 Y:   67 RGB: (238, 255, 255)
        click(1208,67)
        time.sleep(.2)
        click(1342,214)
        time.sleep(.2)
        click(1580,48)
        
        #ML X:  395 Y:  545 RGB: ( 93, 108, 122)
        click(395,545)
        time.sleep(.2)
        click(516,693)
        time.sleep(.2)
        click(762,530)
        
        #MR X: 1210 Y:  547 RGB: (238, 239, 255)
        click(1210,547)
        time.sleep(.2)
        click(1355,700)
        time.sleep(.2)
        click(1582,529)
        
        #BL X:  386 Y: 1022 RGB: ( 98, 114, 116)
        click(386,1022)
        time.sleep(.2)
        click(513,1181)
        time.sleep(.2)
        click(761,1008)

        #Close main's friend menu
        click(32,72)
        x=1
        while x == 1:
            startSharing()
            x = x+1
            break

    def clickAll(x,y):
        click(x,y)
        click(x+xOff,y)
        click(x+xOff,y+yOff)
        click(x,y+yOff)
        click(x,y+yOff+yOff)
    def clickAllC(x,y,count1,count2,count3,count4):
        click(x,y)
        if count1==0:
            click(x+xOff,y)
        if count2==0:
            click(x+xOff,y+yOff)
        if count3==0:
            click(x,y+yOff)
        if count4==0:
            click(x,y+yOff+yOff)


    def runSkills():
        splitTime = 0
        if(pyautogui.pixel(688,333)[1]>100):
            pyautogui.mouseUp(button='left')
            mainIce()
        if(pyautogui.pixel(684,292)[0] >200):
            mainFire()
            splitTime = splitTime+5
            print("The time in run is roughly ",splitTime, " seconds.")
            pyautogui.mouseDown(x=64, y=252, button='left')
        if(pyautogui.pixel(754,209)[2]>200):
            pyautogui.mouseUp(button='left')
            mainLight()
            mainPot()
            mainHeal()
            pyautogui.mouseDown(x=64, y=252, button='left')
        if(pyautogui.pixel(688,216)[1]>140):
            pyautogui.mouseUp(button = 'left')
            mainHeal()
            mainPot()        


    #split is the main movement system. this handles movement by clicking and holding on the joystick at a given location
    #then, the bot will check if any instances have disconnected/died and act accordingly. I have made many versions to
    #respond in different manners depending on the event/map and desired result.
    
    def split(x):
        
            xDead = 432
            xOff = 820

            yDead = 224
            yOff = 480

            xRespawn = 240
            yRespawn = 240
            spawn()
            click(746,163)
            
            #how to read this: 
            # c is an iterable which will indicate a change in direction. This can be increased 
            # or decreased depending on the needs of the map. 
            # I divided maps into segments and had a consistent 
            # direction until a certain pixel (or set of pixels) matched a desired location 
            # This version goes off of strictly timing because it works & is simpler, use pyautogui.pixel to alter for harder maps
                        
            for i in range(x):
                y = 0
                c=1
                #run straight to the wall, then turn
                while c==1:
                  
                    x = 0
                    for i in pyautogui.locateAllOnScreen('dc.png'):
                        x = 1
                    if x == 1:
                        c = c+100
                        print('disconnected')
                        open_bluestacks_instances()

                    if (pyautogui.pixel(xDead,yDead)[0]==203 and pyautogui.pixel(xDead,yDead)[1]== 209 and pyautogui.pixel(xDead,yDead)[2]== 218)\
                       or (pyautogui.pixel(355,209)[0]==101 and pyautogui.pixel(355,209)[1]== 104 and pyautogui.pixel(355,209)[2]== 109):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break

                    if (pyautogui.pixel(393,380)[0]==238 and pyautogui.pixel(393,380)[1]== 204 and pyautogui.pixel(393,380)[2]== 85):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break
                    if(y>10):
                        c=c+100
                        break
                    pyautogui.mouseDown(x=60, y=264, button='left')
                    time.sleep(3.3)
                    fight(2)
                    if(pyautogui.pixel(684,292)[0] >200):
                        pyautogui.mouseUp(button='left')
                        mainFire()
                        mainPot()
                    pyautogui.mouseUp(x=79, y=253, button='left')
                    fight(20)
                    pyautogui.mouseDown(x=40, y=250, button='left')
                    time.sleep(1)
                    pyautogui.mouseUp()
                    fight(2)
                    

                    c=c+1
                    break
                    
            
                while c==2:

                    mainAuto()
                    if (pyautogui.pixel(432,224)[0]==203 and pyautogui.pixel(432,224)[1]== 209 and pyautogui.pixel(432,224)[2]== 218)\
                   or (pyautogui.pixel(355,209)[0]==101 and pyautogui.pixel(355,209)[1]== 104 and pyautogui.pixel(355,209)[2]== 109):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break
                    if (pyautogui.pixel(393,380)[0]==238 and pyautogui.pixel(393,380)[1]== 204 and pyautogui.pixel(393,380)[2]== 85):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break
                    if(y>20):
                        c=c+100
                        break
                    runSkills()
                    y= y+1                  
                    pyautogui.mouseDown(x=54, y=275, button='left')
                    time.sleep(3)
                    fight(25)
                    c=c+1
                    
                #run into the top wall
                while c==3:

                    mainAuto()
                    if (pyautogui.pixel(432,224)[0]==203 and pyautogui.pixel(432,224)[1]== 209 and pyautogui.pixel(432,224)[2]== 218)\
                       or (pyautogui.pixel(355,209)[0]==101 and pyautogui.pixel(355,209)[1]== 104 and pyautogui.pixel(355,209)[2]== 109):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break
                    if (pyautogui.pixel(393,380)[0]==238 and pyautogui.pixel(393,380)[1]== 204 and pyautogui.pixel(393,380)[2]== 85):
                        pyautogui.mouseUp(button='left')
                        click(xRespawn,yRespawn)
                        click(xRespawn,yRespawn)
                        c=c+100
                        break
                    if(y>30):
                        c=c+100
                        break
                    runSkills()
                    y = y+1
                    pyautogui.mouseDown(x=115, y=315, button='left')
                    time.sleep(1.7)
                    fight(460)
                    c=c+1
                    getGold()
                    break
                    
                if c>14:
                    x = 0
                    for i in pyautogui.locateAllOnScreen('dc.png'):
                        x = 1

                    print(c)
                    
                    checkDead()
                    time.sleep(.5)
                    clearShare()
                    
                    stopSharing()
                    logOut()
                    tr = 1
                    print(tr)
                    break
    

    def startSharing():
        
        time.sleep(.3)
        clearShare()
        time.sleep(.3)
        click(233,354)
        pyautogui.hotkey('ctrl','shift','9')
        time.sleep(.5)
        #1st down
        click(234,159)
        time.sleep(.2)
        #2nd down
        click(233,196)
        #3rd down
        click(233,229)
        #4rd down
        click(233,263)
        
        click(541,357)
        
    def stopSharing():
        click(562,22)

    def clearShare():
        
        click(416,24)
        time.sleep(.3)
        pyautogui.hotkey('ctrl','shift','9')
        if pyautogui.pixel(233,354)[2] <200:
            for i in range(2):
                click(233,354)
                time.sleep(.5)
        if pyautogui.pixel(233,354)[2] >200:
            click(233,354)
        click(588,119)
    def mainAuto():
        pyautogui.hotkey('left','num2')
        #if(pyautogui.pixel(683,396)[0]<50):
        pyautogui.hotkey('left','num5')

    def isDisconnected():
        #You have been disconnected from the server button:
        #135 Y:  230 RGB: (173, 141,  93)
        for i in range(3):
            x = 388
            y = 415
            xChk = 135
            yChk = 230
            if (pyautogui.pixel(xChk,yChk)[0] == 173 and pyautogui.pixel(xChk,yChk)[1] == 141 and pyautogui.pixel(xChk,yChk)[2] == 93):
                click(x,y)
            yChk = yChk+yOff
            y = y+yOff
        for i in range(2):
            x = 388
            y = 415
            xChk = 135
            yChk = 230
            x = x+xOff
            xChk = xChk + xOff
            if (pyautogui.pixel(xChk,yChk)[0] == 173 and pyautogui.pixel(xChk,yChk)[1] == 141 and pyautogui.pixel(xChk,yChk)[2] == 93):
                click(x,y)
            yChk = yChk+yOff
            y = y+yOff
        time.sleep(5)
        #X:  399 Y:  346 RGB: (238, 204,  85)
        for i in range(3):
            x = 399
            y = 346
            xChk = 399
            yChk = 346
            if (pyautogui.pixel(xChk,yChk)[0] == 238 and pyautogui.pixel(xChk,yChk)[1] == 204 and pyautogui.pixel(xChk,yChk)[2] == 85):
                click(x,y)
            yChk = yChk+yOff
            y = y+yOff
        for i in range(2):
            x = 399
            y = 346
            xChk = 399
            yChk = 346
            x = x+xOff
            xChk = xChk + xOff
            if (pyautogui.pixel(xChk,yChk)[0] == 238 and pyautogui.pixel(xChk,yChk)[1] == 204 and pyautogui.pixel(xChk,yChk)[2] == 85):
                click(x,y)
            yChk = yChk+yOff
            y = y+yOff

    #Main Skills:
    def mainBuffs():
        click(725,150)
    def mainDrain():
        click(630,340)
    def mainFire():
        click(685,276) 
    def mainLight():
        click(744,217)
    def mainIce():
        click(688,333) 
    def mainHeal():
        click(688,214)  
    def mainPot():
        click(550,440)
    def mainClear():
        click(389,274)

    def allFire():
        fire1()
        fire()
        fire2()
        fire3()

    def light():
        click(754,209)
        
    def allLight():
        light()
        lightning()
        lightning2()
        lightning3()

    def heal():
        click(688,216)
    def allHeal():
        
        heal()
      
        heals()
        
        heals2()
       
        heals3()
    def fire1():
        click(684,292)

    #Top Right (1):
        
    def buffs():
        click(725+820,150)
    def drain():
        click(630+820,340)
    def fire():
        click(1505,280)
    def lightning():
        click(1560,220)  
    def ice():
        click(1505,350)
    def heals():
        click(1507,218)
   

    #Middle Left (2):

    def buffs2():
         click(725,150+960)
    def drain2():
        click(630,340+480)
    def fire2():
        click(680,760)
    def lightning2():
        click(745,700)
    def ice2():
        click(687,825)
    def heals2():
        click(686,700)
    def clear2():
        click(389,274+480)

    #Middle Right (3):
    
    def buffs3():
        click(725+820,150+480)
    def drain3():
        click(630+820,340+480)
    def fire3():
        click(1505,760)
    def lightning3():
        click(1560,700)
    def ice3():
        click(1505,825)
    def heals3():
        click(1507,697)
    def clear3():
        click(389+820,274+480)

    #Bottom Left:

    def root():
        #X:  680 Y: 1230 RGB: (129, 102,  67) r>100
        if pyautogui.pixel(680,1230)[0]>100:
            click(680,1230)
    def scream():
        #X:  737 Y: 1175 RGB: (179,  51,  34) r>140
        if pyautogui.pixel(737,1175)[0]>110:
            click(737,1175)
    def blast():
        #X:  681 Y: 1289 RGB: (240, 238, 206) r?200
        if pyautogui.pixel(681,1289)[0]>200:
            click(681,1289)
    def clear():
        pyautogui.press('num2')
        
    #leave map on all toons
    def logOut():
        time.sleep(number)
        click (20,62)
        time.sleep(number)
        click (845,547)
        time.sleep(number)
        click (20,1026)
        time.sleep(number)
        click (845,62)
        time.sleep(number)
        click (20,547)
        time.sleep(.5)
        click (670,453)
        time.sleep(number)
        click (1500,453)
        time.sleep(number)
        click (661,939)
        time.sleep(number)
        click (670,1416)
        time.sleep(number)
        click (1500,933)
        time.sleep(3)
        
        time.sleep(number)
        click (20,62)
        time.sleep(number)
        click (845,547)
        time.sleep(number)
        click (20,1026)
        time.sleep(number)
        click (845,62)
        time.sleep(number)
        click (20,547)
        time.sleep(.5)
        click (670,453)
        time.sleep(number)
        click (1500,453)
        time.sleep(number)
        click (661,939)
        time.sleep(number)
        click (670,1416)
        time.sleep(number)
        click (1500,933)
        time.sleep(number)
        click (20,62)
        time.sleep(number)
        click (845,547)
        time.sleep(number)
        click (20,1026)
        time.sleep(number)
        click (845,62)
        time.sleep(number)
        click (20,547)
        time.sleep(.5)
        click (670,453)
        time.sleep(number)
        click (1500,453)
        time.sleep(number)
        click (661,939)
        time.sleep(number)
        click (670,1416)
        time.sleep(number)
        click (1500,933)
    #click all auto buttons
    def allAuto():
        #click to reset auto, then click auto attack
        x=416
        y=24
        click(x,y)
        pyautogui.hotkey('left','num2')
        pyautogui.hotkey('left','num5')
        click(x+xOff,y)
        pyautogui.hotkey('left','num2')
        pyautogui.hotkey('left','num5')
        click(x+xOff,y+yOff)
        pyautogui.hotkey('left','num2')
        pyautogui.hotkey('left','num5')
        click(x,y+yOff)
        pyautogui.hotkey('left','num2')
        pyautogui.hotkey('left','num5')
        click(x,y+yOff+yOff)
        pyautogui.hotkey('left','num2')
        pyautogui.hotkey('left','num5')
        
        click(717,432)
        click(717+xOff,432)
        click(717+xOff,432+yOff)
        click(717,432+yOff)
        click(717,432+yOff+yOff)

        
    #click all potions
    def pots():
        x = 550
        y = 440
        click(x,y)
        click(x+820,y)
        click(x+820,y+480)
        click(x,y+480)
        click(x,y+960)
    def stayBack():
        x = 307
        y = 357
        click(x,y)
        click(x+820,y)
        click(x+820,y+480)
        click(x,y+960)
        click(x,y+480)
    #collect all gold
    def getGold():
        pyautogui.mouseDown(36,267)
        time.sleep(2.5)
        pyautogui.mouseUp()
        fight(1)
        time.sleep(1)
        pyautogui.mouseDown(110,301)
        time.sleep(1.0)
        pyautogui.mouseUp()
        fight(1)
        pyautogui.mouseDown(110,290)
        time.sleep(.8)
        pyautogui.mouseUp()
        pyautogui.mouseDown(55,320)
        time.sleep(1.5)

        
    #this function will check to see if any characters have died, then respawns them
    def checkDead():      
            if (pyautogui.pixel(xDead,yDead)[0]==203 and pyautogui.pixel(xDead,yDead)[1]== 209 and pyautogui.pixel(xDead,yDead)[2]== 218):
                click(xRespawn,yRespawn)
            if (pyautogui.pixel(xDead,yDead)[0]==203 and pyautogui.pixel(xDead,yDead)[1]== 209 and pyautogui.pixel(xDead,yDead)[2]== 218):
                click(xRespawn,yRespawn)
            if (pyautogui.pixel(xDead+xOff,yDead)[0]==203 and pyautogui.pixel(xDead+xOff,yDead)[1]== 209 and pyautogui.pixel(xDead+xOff,yDead)[2]== 218):
                click(xRespawn+xOff,yRespawn)
            if (pyautogui.pixel(xDead,yDead+yOff)[0]==203 and pyautogui.pixel(xDead,yDead+yOff)[1]== 209 and pyautogui.pixel(xDead,yDead+yOff)[2]== 218):
                click(xRespawn,yRespawn+yOff)
            if (pyautogui.pixel(xDead+xOff,yDead+yOff)[0]==203 and pyautogui.pixel(xDead+xOff,yDead+yOff)[1]== 209 and pyautogui.pixel(xDead+xOff,yDead+yOff)[2]== 218):
                click(xRespawn+xOff,yRespawn+yOff)
            if (pyautogui.pixel(xDead,yDead+yOff+yOff)[0]==203 and pyautogui.pixel(xDead,yDead+yOff+yOff)[1]== 209 and pyautogui.pixel(xDead,yDead+yOff+yOff)[2]== 218):
                click(xRespawn,yRespawn+yOff+yOff)
       
    #these functions are for bluestacks "multi sync" 
    def startAllShare():

        click(416,24)
        time.sleep(.3)
        pyautogui.hotkey('ctrl','shift','9')
        time.sleep(.3)
        click(233,357)
        time.sleep(.3)
        click(532,355)
    def stopAllShare():
        click(416,24)
        time.sleep(.3)
        pyautogui.hotkey('ctrl','shift','9')
        time.sleep(.3)
        click(532,355)
        time.sleep(.3)
        click(233,357)
        time.sleep(.3)
        click(588,116)
        
    
    #this is a loop to kill enemies
    def fight(x):
        xDead = 432
        xOff = 820     
        yDead = 224
        yOff = 480
        xRespawn = 240
        yRespawn = 240
        potCounter = 0
        for i in range (x):

            mainBuffs()
            mainFire()
            mainHeal()
            mainLight()
            click(685,151)
            click(744,284)
            click(745,347)
            click(623,284)
            mainIce()
            mainDrain()
            
            #bluestacks actually allows "num2" which is a keyboard button input allowing to unselect enemies
            pyautogui.hotkey('num2')
           
            click(719,436)
            checkDead()
            
        

    #set of functions to clear inventory
    def confirm():
        click(395,341)
        time.sleep(.5)

    def clickRare():
        click(670,395)
        time.sleep(.5)

    def clickEpic():
        click(670,344)
        time.sleep(.5)

    def clickCommon():
        click(664,245)
        time.sleep(.5)

    def clickTrash():
        click(664,195)
        time.sleep(.5)
        
    def clickUncommon():
        click(665,295)
        time.sleep(.5)

    def sellAll():
        #click sell all
        click(636,450)
        time.sleep(.5)

        #click epic
        clickEpic()
        confirm()


        #click rare
        clickRare()
        confirm()


        #click uncommon
        clickUncommon()
        confirm()

        #click common
        clickCommon()
        confirm()

        clickTrash()
        confirm()

        time.sleep(.3)
        click(748,70)
        
    def invClear():
        startSharing()
        tcount = 0
        for x in range(2):
            click(227,68)
            time.sleep(.5)

        #because the button is very unreliable, there needs to be a spam of these buttons, but it will always catch the DB
        #getDailyBlessing:
        time.sleep(.5)
        click(123,72)
        time.sleep(.5)
        click(708,280)
        time.sleep(.5)
        click(380,400)
        click(380,400)
        click(380,350)
        click(380,360)
        click(380,400)
        click(380,340)
        click(380,350)
        click(380,360)
        click(380,400)
        click(380,400)
        click(380,350)
        click(380,360)
        click(380,400)
        click(380,340)
        click(380,350)
        click(380,360)
        time.sleep(1)
        click(123,72)
        time.sleep(.5)
        click(708,280)
        time.sleep(.5)
        click(380,390)
        click(380,400)
        click(380,370)
        click(380,360)
        click(380,350)
        click(380,340)
        click(380,350)
        click(380,360)
        click(380,400)
        click(380,400)
        click(380,355)
        click(380,360)
        click(380,400)
        click(380,340)
        click(380,350)
        click(380,360)
        time.sleep(1)
        time.sleep(1)
        click(123,72)
        time.sleep(.5)
        click(708,280)
        time.sleep(.5)
        click(380,390)
        click(380,400)
        click(380,370)
        click(380,360)
        click(380,350)
        click(380,340)
        click(380,350)
        click(380,360)
        click(380,400)
        click(380,400)
        click(380,355)
        click(380,360)
        click(380,400)
        click(380,340)
        click(380,350)
        click(380,360)
        time.sleep(1)
        
        for x in range(2):
            click(227,68)
            time.sleep(.5)

        
        #sellhelms
        click(450,125)
        sellAll()
        #sellWep
        click(495,125)
        sellAll()  
        #click on armors
        click(526,125)
        sellAll()
        #click on shield
        click(566,125)
        sellAll()
        #repeat with rings:
        click(597,125)
        sellAll()
        #repeat with rings:
        click(637,125)
        sellAll()
        
        #gtfo, leaves inventory screen
        for x in range (2):
            click(29,72)
            click(29+xOff,72)
            click(29+xOff,72+yOff)
            click(29,72+yOff)
            click(29,72+yOff+yOff)
            time.sleep(.3)
    
    
    #only clear the inventory every 30 runs, change as necessary.
    if (invx%30) == 0:
        if (pyautogui.pixel(767,259)[0] == 247 and pyautogui.pixel(767,259)[1] == 222 and pyautogui.pixel(767,259)[2] == 129):
        #give time to move windows out of the way
        #if all alts are at home position, continue
        #for i in range(10):
            if ((pyautogui.pixel(767+xOff,259)[0] == 247 and pyautogui.pixel(767+xOff,259)[1] == 222 and pyautogui.pixel(767+xOff,259)[2] == 129)\
                and(pyautogui.pixel(767+xOff,259+yOff)[0] == 247 and pyautogui.pixel(767+xOff,259+yOff)[1] == 222 and pyautogui.pixel(767+xOff,259+yOff)[2] == 129)\
                and(pyautogui.pixel(767,259+yOff)[0] == 247 and pyautogui.pixel(767,259+yOff)[1] == 222 and pyautogui.pixel(767,259+yOff)[2] == 129)\
                and(pyautogui.pixel(767,259+yOff+yOff)[0] == 247 and pyautogui.pixel(767,259+yOff+yOff)[1] == 222 and pyautogui.pixel(767,259+yOff+yOff)[2] == 129)):
             #stopwatch ( snap to right half )
                
                
                #if (invx%3) == 0:
                print('inventory cleared!')
                invClear()
                invx = invx+1
    orderCheck = 0

    #change name for each host

    for i in pyautogui.locateAllOnScreen('reference.png'):
        orderCheck = orderCheck+1
    #start and run the bot:
    for i in pyautogui.locateAllOnScreen('continueButton.png'):
        contx = contx+1
        
        #WILL NOT RUN IF ALL BOTS ARE NOT RUNNING AND IN THE CORRECT POSITION.
        print(contx, ", ", i)
        if contx==5 and orderCheck == 1:
                time.sleep(.3)
                click(2523,864)
                time.sleep(0.3)
                hostMap()
                print(invx)
                x = 0
                while x==0:
                    if(pyautogui.pixel(51,49)[0] > 200):
                        time.sleep(.5)
                        inviteLobby()
                        x=x+1
                
                while(x==1):
                    
                    time.sleep(.5)
                    joinLobby()
                    #checks for joystick(in game)
                    z = 0 
                    while z <10:
                        l = 0
                        #if all the players in lobby, start
                        for i in pyautogui.locateAllOnScreen('gear.png'):
                            l = l+1
                            print(l)
                            print(i)
                        if l ==5:
                            split(1)
                            if ((pyautogui.pixel(767+xOff,259)[0] == 247 and pyautogui.pixel(767+xOff,259)[1] == 222 and pyautogui.pixel(767+xOff,259)[2] == 129)\
                        and(pyautogui.pixel(767+xOff,259+yOff)[0] == 247 and pyautogui.pixel(767+xOff,259+yOff)[1] == 222 and pyautogui.pixel(767+xOff,259+yOff)[2] == 129)\
                        and(pyautogui.pixel(767,259+yOff)[0] == 247 and pyautogui.pixel(767,259+yOff)[1] == 222 and pyautogui.pixel(767,259+yOff)[2] == 129)\
                        and(pyautogui.pixel(767,259+yOff+yOff)[0] == 247 and pyautogui.pixel(767,259+yOff+yOff)[1] == 222 and pyautogui.pixel(767,259+yOff+yOff)[2] == 129)):
                                click(2015,925)
                                x=x-1
                                break
                            
                            if tr==0:
                                tcount = 0
                                time.sleep(.2)
                                #stops share
                                click(560,21)

                                
                                clearShare()
                                startAllShare()
                                
                                click(560,21)
                                clearShare()
                                checkDead()
                                
                            checkDead()
                            
                            #exit the loop
                            z= z+100

                        #let the loop give players time to join
                        time.sleep(1)
                        z = z+1
                            
                    time.sleep(.1)
                    stopSharing()
                    logOut()
                    #click(2523,864)
                    invx = invx+1
                    tr = 0
                    print(tr)
                    x=x-1

    #RESTART IF BROKEN
    else:
        contx = 0
        ordercheck = 0
        time.sleep(1.2)
        tcount = tcount +1
        print("time down: ", tcount, " seconds")
        if tcount > 12:
            open_bluestacks_instances()
            tcount = 0;
    
                
                
                
        

            
            
                    


