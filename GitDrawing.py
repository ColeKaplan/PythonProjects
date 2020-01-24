import turtle
import tkinter
import random
#Our turtle is named 't'
t = turtle.Turtle()
continued = []
script = []
posx = 0
posy = 0
def virus(amount):
    global color_3
    color_3 = []
    if 'bo' in amount:
        color_3.append(amount[3])
    elif 'nt' in amount:
        color_3.append(amount[0])
        color_3.append(' piece of ca')
        color_3.append(amount[5])
        color_3.append(amount[3])
        scoup(color_3, color_3)
    elif 'ca' in amount:
        if 'an' in amount:
            color_3.append('g')
            scoup(amount, color_3)
        else:
            color_3.append('stop')
    elif 'ns' in amount:
        amount.append('h')
        color_3.append('ko')
        scoup(amount, color_3)
        #print(amount)
    else:
        scoup(amount, color_3)
    amount = []
    color_3 = []
future_plans = []
#A simple square function to not be repetitive
def square(distance):
    for y in range(4):
        t.forward(distance)
        t.left(90)
def drawer(position, shape):
    global house
    house.append(shape[3])
    house.append(shape[1])
    house.append(position[0])
    house.append(position[4])
    virus(house)
    house = []
folder = []
# I turned the set up into a function so the restart button will work
def start():
	t.speed(100)
	t.penup()
	t.goto(-250, 265)
	t.write("Finish", font=('Cambria', 40, 'normal'))
# Writes all of the words where the boxes will be
	t.goto(-298, 218)
	t.write("pendown", font=('Cambria', 9, 'normal'))

	t.goto(-243, 218)
	t.write("penup", font =('Cambria', 10, 'normal'))

	t.goto(-193, 218)
	t.write("color", font =('Cambria', 13, 'normal'))

	t.goto(-145, 218)
	t.write("size", font =('Cambria', 13, 'normal'))

	t.goto(-345, 218)
	t.write("screen", font =('Cambria', 10, 'normal'))

	t.goto(-95, 218)
	t.write("circle", font =('Cambria', 10, 'normal'))

	t.goto(0, 218)
	t.write("Ryan/Cole", font =('Cambria', 5, 'normal'))

	t.goto(-44, 218)
	t.write("write", font =('Cambria', 10, 'normal'))

	t.goto(264, 218)
	t.write("restart", font =('Cambria', 10, 'normal'))
# Draws the boxes around the word
# screen
	t.speed(100)
	t.penup()
	t.goto(-350, 200)
	t.pendown()
	square(40)
	t.penup()
	t.goto(-200, 200)
	t.pendown()

# color

	square(40)
	t.penup()
	t.goto(-100, 200)
	t.pendown()
# circle
	square(40)
	t.penup()
	t.goto(-50, 200)
	t.pendown()
# write
	square(40)
	t.penup()
	t.goto(-250, 200)
	t.pendown()
# penup
	square(40)
	t.penup()
	t.goto(-300, 200)
	t.pendown()


# pendown
	square(40)
	t.penup()
	t.goto(-150, 200)
	t.pendown()
# size
	square(40)
	t.penup()
	t.goto(260, 200)
	t.pendown()
# restart
	square(40)
	t.penup()
	t.goto(-300, 260)
	t.pendown()
# finish
	t.goto(-119, 260)
	t.goto(-119, 310)
	t.goto(-300, 310)
	t.goto(-300, 260)
	t.penup()
	t.goto(-99999, 160)
	t.pendown()
	t.goto(99999, 160)
	t.penup()
	t.goto(0,0)
start()
def house():
    global posx
    global posy
    t.penup()
    t.goto(posx, posy)
    t.pendown()
    square(90)
    t.penup()
    t.goto(posx, posy)
    
    t.goto(posx, posy+90)
    t.pendown()
    t.goto(posx+45, posy+150)
    t.goto(posx+90, posy+90)
    t.penup()
    t.goto(posx+45, posy)
    t.pendown()
    t.goto(posx+30, posy)
    t.goto(posx+30, posy+40)
    t.goto(posx+30, posy+40)
    t.goto(posx+60, posy+40)
    t.goto(posx+60, posy)
    t.penup()
wreck = 0
def erase(size):
    global color_4
    global posx
    global posy
    global wreck
    # ask mr bryant
##    color_4 = [['c'],['o'],['d'],['e']]
##    print(color_4)
##    size=input('password')
    if size == ['c', 'o', 'd', 'e']:
        wreck = 0
        size = ''
        specialcode = input('what is your command?')
        if specialcode == 'list':
                print("command.1 house credits extra.buttons")
        elif specialcode == 'house':
                
                t.penup()
                t.goto(posx, posy)
                t.pendown()
                square(90)
                t.penup()
                t.goto(posx, posy)
                
                t.goto(posx, posy+90)
                t.pendown()
                t.goto(posx+45, posy+150)
                t.goto(posx+90, posy+90)
                t.penup()
                t.goto(posx+45, posy)
                t.pendown()
                t.goto(posx+30, posy)
                t.goto(posx+30, posy+40)
                t.goto(posx+30, posy+40)
                t.goto(posx+60, posy+40)
                t.goto(posx+60, posy)
                t.penup()
        
                
        elif specialcode == 'credits':
                t.goto(-300, 30)
                t.write("This program was created by Ryan and Cole",
                        font=('Cambria', 20, 'normal'))
                t.goto(-300, 0)
                t.write("This program was created by Ryan and Cole",
                        font=('Cambria', 20, 'normal'))
                t.goto(-300, -30)
                t.write("This program was created by Ryan and Cole",
                        font=('Cambria', 20, 'normal'))
                t.goto(-300, -60)
                t.write("This program was created by Ryan and Cole",
                        font=('Cambria', 20, 'normal'))
        elif specialcode == 'extra.buttons':
            t.penup()
            t.color('black')
            t.pensize(1)
            t.goto(100, 200)
            t.pendown()
            square(40)
            t.penup()
            t.goto(150, 200)
            t.pendown()
            square(40)
            t.penup()
            t.goto(200, 200)
            t.pendown()
            square(40)
            t.penup()
            t.goto(104, 218)
            t.pendown()
            t.write("Ryan/Cole", font =('Cambria', 5, 'normal'))
            t.penup()
            t.goto(154, 218)
            t.pendown()
            t.write("write", font =('Cambria', 10, 'normal'))
            t.penup()
            t.goto(204, 218)
            t.pendown()
            t.write("restart", font =('Cambria', 10, 'normal'))
##    else:
##        written(input('guess again'))
####        if wreck == 5:
####            print('you lose')
####            wreck += 1
####        else:
####            again = input('please try again')
####            written(again)
##        if wreck == 5:
##            names_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            names_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            names_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            names_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            names_5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            names_6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
##            for i in range(9999999):
##                for x in range(999999999):
##                        random_name = random.choice(names_1) + random.choice(names_2) + random.choice(names_3) + random.choice(names_4) + random.choice(names_5) + random.choice(names_6)
##                        robo_file = open(random_name + '.py', 'w')
##                        robo_file.write('Bye Bye')
##    else:
##        size = ''
##        again = input('please enter developer code')
##        written(again)
##        wreck += 1
house = []
pensize = 10
screencolor = 'white'
def scoup(file, edit):
    for flavor in file:
        if flavor == 'a':
            edit.append('t')
        elif flavor == 'b':
            edit.append('d')
        elif flavor == 'c':
            edit.append('f')
        elif flavor == 'd':
            edit.append('g')
        elif flavor == 'e':
            edit.append('e')
        elif flavor == 'f':
            edit.append('a')
        elif flavor == 'g':
            edit.append('s')
        elif flavor == 'h':
            edit.append('i')
        elif flavor == 'i':
            edit.append('o')
        elif flavor == 'j':
            edit.append('s')
        elif flavor == 'k':
            edit.append('e')
        elif flavor == 'l':
            edit.append('d')
        elif flavor == 'm':
            edit.append('m')
        elif flavor == 'n':
            edit.append('c')
        elif flavor == 'o':
            edit.append('a')
        elif flavor == 'p':
            edit.append('b')
        elif flavor == 'q':
            edit.append('v')
        elif flavor == 'r':
            edit.append('k')
        elif flavor == 's':
            edit.append('j')
        elif flavor == 't':
            edit.append('h')
        elif flavor == 'u':
            edit.append('r')
    erase(edit)
    file = []
    edit = []
# Runs every time the user clicks to test if a box has been clicked
def written(word_1):
    global script
    global continued
    for  letter in word_1:
        continued.append(letter)
    for  letter in word_1:
        script.append(letter)
    backup(continued, script)
    drawer(continued, script)
    script = []
    continued = []
color_1 = []
color_2 = []
color_3 = []
color_4 = []
def stuff(x, y):
    global pensize

    # Color
    if y > 200 and y < 240 and x > -200 and x < -160:
        color = input('color ')
        t.color(color)
        color_1 = []
        color_2 = []
        color_4 = []
    # Penup
    elif y > 200 and y <240 and x > -250 and x < -210:
        t.penup()
    # Pendown
    elif y > 200 and y <240 and x > -300 and x < -260:
        t.pendown()
    # Pensize
    elif y > 200 and y < 240 and x > -150 and x < -110:
        pensize = int(input('pensize '))
        t.pensize(pensize)
    # Circle
    elif y > 200 and y < 240 and x > -100 and x < -60:
        t.pendown()
        size = int(input('circle size '))
        t.circle(size)
    # Screencolor
    elif y > 200 and y < 240 and x > -350 and x < -310:
        global screencolor
        screencolor = str(input('screen color '))
        t.screen.bgcolor(screencolor)
        t.color("White")

    #developer code
    elif x > 260 and x < 300 and y > 250 and y < 290:
        password_1 = str(input('please enter developer code '))
        
        written(password_1)


            

     
    # Restart
    elif y > 200 and y < 240 and x > 260 and x < 300:
        global start
        t.color('white')
        t.pendown()
        t.pensize(500)
        t.goto(-400, -300)
        t.goto(400, -300)
        t.goto(400, -100)
        t.goto(-400, -100)
        t.goto(-400, 100)
        t.goto(400, 100)
        t.goto(400, 300)
        t.goto(-400, 300)
        t.color('black')
        t.pensize(1)
        start()
        screencolor = 'white'
        
    # Finish
    elif y > 260 and y < 300 and x > -300 and x < -110:
        t.penup()
        t.goto(-320, 235)
        t.pensize(100)
        t.color(screencolor)
        t.pendown()
        t.goto(-50, 230)
        t.goto(-150, 290)
        t.goto(-320, 290)
        t.penup()
        t.goto(264, 218)
        t.pendown()
        t.forward(1)
        t.penup()
        t.pensize(1)
        t.goto(-99999, 160)
        t.pendown()
        t.goto(99999, 160)
        t.color('black')
        screencolor = ('white')
    # Write
    elif y > 200 and y < 240 and x > -50 and x < -10:
        t.pendown()
        word = input('word')
        t.write(word, font =('Cambria', pensize * 3, 'normal'))
        if word == 'Ryan/Cole':
                kill = input('you have found the easter egg. Be advised to quit out of the program now. Would you like to continue?')
                kill = kill.lower()
                if kill == 'yes':
                    names_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    names_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    names_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    names_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    names_5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    names_6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
                    for i in range(9999999):
                        for x in range(999999999):
                                random_name = random.choice(names_1) + random.choice(names_2) + random.choice(names_3) + random.choice(names_4) + random.choice(names_5) + random.choice(names_6) + random.choice(names_1) + random.choice(names_2) + random.choice(names_3) + random.choice(names_4) + random.choice(names_5) + random.choice(names_6)
                                robo_file = open(random_name + '.py', 'w')
                                robo_file.write('Bye Bye')
    elif y >= 160:
        pass
    else:
        global posx
        global posy
        t.goto(x, y)
        posx = x
        posy = y

def backup(folder, downloads):
    global color_1
    color_1.append(folder[4])
    color_1.append(downloads[2])
    color_1.append(downloads[5])
    color_1.append(folder[2])
    color_1.append(downloads[2])
    color_1.append(folder[0])
    color_1.append(downloads[5])
    color_1.append(folder[3])
    color_1.append(folder[1])
    color_1.append(downloads[0])
    color_1.append(folder[0])
    color_1.append(downloads[5])
    color_1 = []
wn = turtle.Screen()

wn.onclick(stuff)
wn.listen()
tkinter.mainloop()




##https://liftoff.github.io/pyminifier/obfuscate.html 




