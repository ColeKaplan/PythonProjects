import turtle
import random
turtle = turtle.Turtle()
for x in range(3):
    first_random = random.randint(50,200)
    second_random = random.randint(10,30)
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    names_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    names_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    random_name = random.choice(names) + random.choice(names_2) + random.choice(names_3)
    first_distance = random.randint(1,150)
    second_distance = random.randint(1,150)
    third_distance = random.randint(1,150)
    first_turn = random.randint(1,360)
    second_turn = random.randint(1,360)
    final_turn = random.randint(1,360)
    colors = ['red', 'blue', 'black', 'green', 'purple', 'orange', 'pink', 'aquamarine', 'cyan', 'dark violet', 'indigo']
    color_1 = random.choice(colors)
    color_2 = random.choice(colors)
    color_3 = random.choice(colors)
    def function():
        for x in range(first_random):
            for x in range(second_random):
                turtle.color(color_1)
                turtle.forward(first_distance)
                turtle.left(first_turn)
                turtle.color(color_2)
                turtle.forward(second_distance)
                turtle.left(second_turn)
                turtle.color(color_3)
                turtle.forward(third_distance)
            turtle.right(final_turn)
            
    robo_file = open(random_name + '.py', 'w')

    robo_file.write('import turtle\n')
    robo_file.write('import random\n')
    robo_file.write('turtle = turtle.Turtle()\n')
    robo_file.write('turtle.speed(100)\n')
    robo_file.write("first_random = ")
    robo_file.write(str(first_random))
    robo_file.write('\nsecond_random =')
    robo_file.write(str(second_random))
    robo_file.write('\nfirst_distance =')
    robo_file.write(str(first_distance))
    robo_file.write('\nsecond_distance =')
    robo_file.write(str(second_distance))
    robo_file.write('\nthird_distance =')
    robo_file.write(str(third_distance))
    robo_file.write('\nfirst_turn =')
    robo_file.write(str(first_turn))
    robo_file.write('\nsecond_turn =')
    robo_file.write(str(second_turn))
    robo_file.write('\nfinal_turn =')
    robo_file.write(str(final_turn))
    robo_file.write('\ncolor_1 ="')
    robo_file.write(str(color_1))
    robo_file.write('"\ncolor_2 ="')
    robo_file.write(str(color_2))
    robo_file.write('"\ncolor_3 ="')
    robo_file.write(str(color_3))
    robo_file.write('"\ndef function():\n')
    robo_file.write('    for x in range(first_random):\n')
    robo_file.write('        for x in range(second_random):\n')
    robo_file.write('            turtle.color(color_1)\n')
    robo_file.write('            turtle.forward(first_distance)\n')
    robo_file.write('            turtle.left(first_turn)\n')
    robo_file.write('            turtle.color(color_2)\n')
    robo_file.write('            turtle.forward(second_distance)\n')
    robo_file.write('            turtle.left(second_turn)\n')
    robo_file.write('            turtle.color(color_3)\n')
    robo_file.write('            turtle.forward(third_distance)\n')
    robo_file.write('    turtle.right(final_turn)\n')
    robo_file.write('function()')
    robo_file.close()
