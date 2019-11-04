#------------------------------------------------------------------------------
#Program Name: project.py
#Student Name: Jayden Geisler
#------------------------------------------------------------------------------
#Program Purpose: Make a logix game 
#------------------------------------------------------------------------------


from graphics import *
from random import *
from math import *


#Global variables

# global window
win = None
win = GraphWin ('project', 500,500)
# size of board
size = 10

#color of the original board picked at the main menu
color_1 = None

#color of the secondary color picked at the main menu
color_2 = None

# how many times the board is shuffled at the start
difficulty = None

# list of the hexagons
board = []

# list of 'W' and 'B' to determin the colors for inisiating the winning function
color = []

# other objects that get printed on the board, use is to earase it when menu is called
board_objects = []

# a list of numbers that flips to reverse the clicks that where taken to solve the puzz;e
solution = []

#counting object number that changes and gets reprinted 
num_obj = Text(Point(425,210),'0')

#all pixles that overlap in the x directions
overlap = 0

# a global string that has all the objects in the menu so it can be quickly earased when the game is called            
menu_objects = []

# variable that keeps track of how many times the loop of going back to the main menu has happend so that the window will close properly 
quit_looper = 0

#Function:     creats a list of the overlaping pixles on the hexagons 
#Syntax:       overlap = overlap_sections(size)
#Paramaters:   size: size of the board (int)
#Return value: a: A list of overlaping pixles (list of int)

def overlap_sections(size):
    a = []
    for i in range(size+1):
        q = 10 + 30*i
        for j in range(11):
                a.append(q+j)    
    return a 
overlap = overlap_sections(size)

#Function:     makes a hexabon object but does not draw it 
#Syntax:       hexagon = make_hexagon(x,y)
#Paramaters:   x: x pixle that the far left corner is located 
#              y: y pixle that is the location of the far left corner
#Return value: h: a object that is in the shape of a hexagon

def make_hexagon(x,y):
    global win, color_1
    
    h = Polygon([Point(x,y),Point(x+10,y-20),Point(x+30,y-20),Point(x+40,y),Point(x+30,y+20),Point(x+10,y+20)])
    
    h.setFill(color_1)
   
    return h 



#Function:     prints the playing screen, that includes all the hexagons and buttons on the right side
#Syntax:       None
#Paramaters:   length: length of the hexagon board (int)
#Return value: None

def make_board(length):
    global win, board, color, board_objects
    # resets the board and color lists when it is recalled when you go to the main menu
    board = []
    color = []
    # restart button draw
    button = Rectangle(Point(400,100),Point(450,150))
    restart = Text(Point(425,125),"restart")
    button.draw(win)
    restart.draw(win)
    board_objects.append(button)
    board_objects.append(restart)
    
    # counter
    counter_name = Rectangle(Point(400,175),Point(450,225))
    count = Text(Point(425,190),"Count:")
    counter_name.draw(win)
    count.draw(win)
    board_objects.append(counter_name)
    board_objects.append(count)
    
    # quit button
    quit_square = Rectangle(Point(400,25), Point(450,75))
    quit = Text(Point(425,50), 'Quit')
    quit_square.draw(win)
    quit.draw(win)
    board_objects.append(quit_square)
    board_objects.append(quit)
    
    # solution button
    solution_square = Rectangle(Point(400,250), Point(450,300))
    solution = Text(Point(425,275), 'Solution')
    solution_square.draw(win)
    solution.draw(win)
    board_objects.append(solution_square)
    board_objects.append(solution)
    
    # menu button
    menu_square = Rectangle(Point(400,325),Point(450,375))
    menu_text = Text(Point(425,350),'main\nmenu')
    menu_square.draw(win)
    menu_text.draw(win)
    board_objects.append(menu_square)
    board_objects.append(menu_text)

    for i in range(length//2):
        for j in range(length):
            h = make_hexagon(10+i*60,40+j*40)
            h.draw(win)
            board.append(h)
            color.append('W')
        for k in range(length):
            he = make_hexagon(40+i*60,60+k*40)
            he.draw(win)
            board.append(he)
            color.append('W') 
            

#Function:     this is only used when clicked in a overlap section, it cuts down the x and y to a smaller graph that has 4 possibilities(4 sloped sides to a hexagon) then puts it throught the equation of the slope and determins if it is the upper hexagon or the lower hexagon
#Syntax:       block = what_hex(x_pix,y_pix)
#Paramaters:   x_pix: x pixle of the click (int)
#              y_pix: y pixle of the click (int)
#Return value: block: what block was clicked 
#              -1: if not block was clicked


def what_hex(x_pix,y_pix):
    #point that devide hexagons into four quadrents each having there own points
    x_point = x_pix//30
    y_point = (y_pix//20)-1
    #larger graph on the y side to help determin the block set up
    large_y = (y_pix-20)//40
    #gets x and y in terms of small graph to find out if it is above or below the hexagon line
    x = x_pix % 10
    y = y_pix % 20
    #odd and odd
    # x odd and y odd
    if (x_point % 2) == 1 and (y_point % 2) == 1: # works great
        
        if y < (-2*x+20):
            #gets block number if up slope
            block = ((10*(x_point-1))+(y_point-large_y-1))
            return block
        elif y > (-2*x+20):
            #gets blobk number if down slope 
            block = (10*(x_point-1))+(y_point-large_y-1)+10
            return block
        
    # x even y odd        
    if (x_point % 2) == 0 and (y_point % 2) == 1: # works great
        
        if y < (2*x):
            block =  ((10*x_point)+large_y)
            return block
        elif y > (2*x):
            block = (10*x_point)+large_y-10
            return block
        
    #even and even        
    if (x_point % 2 == 0) and (y_point % 2 == 0): # mostly works
        
        if y < (-2*x+20):
            #upper block
            block = ((10*(x_point-1))+y_point-(large_y+1))
            return block
        elif y > (-2*x+20):
            #lower block
            block = (10*(x_point-1))+y_point-(large_y+1)+11
            return block
        
    #x is odd y is even 
    if (x_point % 2 == 1) and (y_point % 2 == 0): # works
        
        if y > (2*x):
            block = ((10*(x_point)) + (y_point-large_y-1)-9) 
            return block
        elif y < (2*x):
            block = (10*(x_point)) + (y_point-large_y-1) 
            return block
    else:
        return -1

#Function:    this function determins if it is in overlap and if its not it has a equation to determin the block that has been clicked
#Syntax:      None
#Paramaters:  pix: a pixle object of a click
#Return value:None
    
def check_hex(pix):
    global win, overlap, not_overlap, solution
    if pix.x in overlap:
        
        block = what_hex(pix.x,pix.y)
        flip_blocks(block)
        solution.append(block)
    elif pix.x not in overlap:
        
        if ((pix.x+14)//30) % 2 == 0: # means its a low block
            block = (((pix.x+15)//30-1) *10) + (pix.y//40-1)
            # if center line is suppose to not change then this line must be deleted
           # change_color(block)
            flip_blocks(block)
            solution.append(block)
        else:# high block
            
            block = ((((pix.x+15)//30)-1) *10) + ((pix.y-20)//40)
            # if center line is suppose to not change then this line must be deleted
            #change_color(block)
            flip_blocks(block)
            solution.append(block)
            
  
#Function:     changes the color of a single block and changes the color list
#Syntax:       change_color(block) 
#Paramaters:   block: the number in the board list that was clicked (int)
#Return value: None

def change_color(block):
    global win, board, color, color_1, color_2
    if color[block] == 'W':
        color[block] = 'B'
        board[block].setFill(color_2)
    else:
        color[block] = 'W'
        board[block].setFill(color_1) 
        

#Function:     determins if it is a edge or not and flips the appropriet blocks 
#Syntax:       flip(block)
#Paramaters:   block: the center block that was clicked (int)
#Return value: None

    
def flip_blocks(block):
    global size, win, board, color, color_1, color_2
    #edge blocks
        #left edge            top edge            right edge                     bottom edge
    if len(str(block)) == 1 or block % 10 == 0 or block//((size-1)*size) == 1 or block % size == (size-1) or block == 0:
        # corners 
        if block == 0:
            change_color(10)
            change_color(1)
        elif block == size*(size-1)+(size-1): 
            change_color(block-1)
            change_color(block -10)
        elif block == (size-1): 
            change_color(block -1)
            change_color(block + 9)
            change_color(block +10)
        elif block == (size-1)*size:
            change_color(block -10)
            change_color(block - 9)
            change_color(block +1)
        # edges, 4 cases 8 scenarios
        # top edge
        if block % 10 == 0 and block != 0 and block != size*(size-1)+(size-1) and block != (size-1) and block != (size-1)*size:
            block_first_num = str(block)[0] 
            if int(block_first_num) % 2 == 1:
                change_color(block -10)
                change_color(block -9)
                change_color(block +1)
                change_color(block +11)
                change_color(block +10)
            else:
                change_color(block -10)
                change_color(block +1)
                change_color(block +10)    
        #right edge
        elif block//((size-1)*size) == 1 and block != 0 and block != size*(size-1)+(size-1) and block != (size-1) and block != (size-1)*size:
            change_color(block -10)
            change_color(block -9)
            change_color(block +1)
            change_color(block -1)
            
        # bottom edge    
        elif block % size == (size-1) and block != 0 and block != size*(size-1)+(size-1) and block != (size-1) and block != (size-1)*size:
            block_first_num = str(block)[0]
            if int(block_first_num) % 2 == 0:
                change_color(block -10)
                change_color(block -11)
                change_color(block -1)
                change_color(block +9)
                change_color(block +10)
            else:
                change_color(block -10)
                change_color(block -1)
                change_color(block +10)
        # left edge
        elif len(str(block)) == 1 and block != 0 and block != size*(size-1)+(size-1) and block != (size-1) and block != (size-1)*size:
            change_color(block +10)
            change_color(block +9)
            change_color(block +1)
            change_color(block -1)



    else:
        block_first_num = str(block)[0]
        if int(block_first_num) % 2 == 0:
            change_color(block -1)
            change_color(block +9)
            change_color(block +10)
            change_color(block -10)
            change_color(block -11)
            change_color(block +1)
        elif int(block_first_num) % 2 == 1:
            change_color(block -1)
            change_color(block +10)
            change_color(block +11)
            change_color(block -9)
            change_color(block -10)
            change_color(block +1)




#Function:     shuffles board
#Syntax:       shuffle_board(diff)
#Paramaters:   diff: the amount of artifical clicks that happen
#Return value: None

def shuffle_board(diff):
    global board, solution 
    
    for i in range(diff):
        randy = randint(0,len(board)-1)
        solution.append(randy)
        #change_color(randy)
        flip_blocks(randy)

 
#Function:     clears the board to one color and then re shuffles it
#Syntax:       restart_button(diff)
#Paramaters:   diff: the amount that it shuffles again 
#Return value: None
    
def restart_button(diff):
    global win, board, color, difficulty
    for i in range(len(color)):
        if color[i] == 'B':
            change_color(i)
    solution = []        
    shuffle_board(difficulty) 
    
#Function:     solves the puzzle when you cant
#Syntax:       solver()
#Paramaters:   None
#Return value: None

def solver():
    global solution
    for i in reversed(solution):
        flip_blocks(i)
    solution = [] 
    
    
#Function:      determins if click was inside or outside the board 
#Syntax:        edge(pix)
#Paramaters:    pix: a set of pixles from the click
#Return value:  returns -1 if click was outside board, returns the block number if inside board  

def edge(pix):
    global board, size
    block = what_hex(pix.x,pix.y)
    

    # left edge
    
    if pix.x > 10 and pix.x < 20 and block < 0 or block == None:
        
        return -1
        
    # right edge 
    
    if pix.x > 310 and pix.x < 320 and block == -1 or block > 99 or block == None:
        
        return -1
    
    # top edge 
    
    if pix.y > 20 and pix.y < 40 and block % 10 != 0 or block == None:
    
        return -1
    
    # botom edge
    
    if pix.y > 420 and pix.y < 440 and block % 10 != 9 or block == None:
        
        return -1
    
    else:
        return block
 

#Function:     navagates the playing screen and all the buttons 
#Syntax:       play()
#Paramaters:   None
#Return value: None
    
def play():
    global win, solution, board, board_objects, quit_looper
    move = -1
    click_counter = 0
    
    while move == -1:
        
        if quit_looper != 0:
            break
        pix = win.getMouse()
        
    
        
        # click within board 
        if pix.x > 10 and pix.x < 320 and pix.y > 20 and pix.y < 440:
            # check if click was on a blank edge 
            if edge(pix) == -1:
                move = -1
            else:
                click_counter += 1
                check_hex(pix)
                counter(click_counter)
                temp = winning("You have won the game")
                if temp == -1:
                    break
       
        #restart button   
        if pix.x//50 == 8 and pix.y//51 == 2:
            click_counter = 0
            solution = []
            restart_button(1)
            
            
        #quit button
        if pix.x//50 == 8 and (pix.y+ 25)//50 == 1:
            quit() 
            move = 1
            quit_looper += 1
            break
        #solution button
        if pix.x//50 == 8 and (pix.y)//50 == 5:
            click_counter = 0
            solver()
            temp = winning("You have sorta\nwon the game")
            if temp == -1:
                break 
            
        #main menu button
        if pix.x//50 == 8 and (pix.y+25)//50 == 7:
            click_counter = 0
            eraser(board)
            eraser(board_objects)
            play_game()
            break
        else:
            move = -1
            

       
        
               



#Function:     changes the number counter
#Syntax:       counter(number)
#Paramaters:   number: the number of clicks that have happend 
#Return value: None

def counter(number):
    global win, num_obj, board_objects
    
    num_obj.undraw()
    num_obj = Text(Point(425,210),str(number))
    num_obj.draw(win)
    board_objects.append(num_obj)
        

#Function:     closes the window
#Syntax:       quit()
#Paramaters:   None
#Return value: None

def quit():
    global win
    win.close()
    

#Function:     determins a win by checking the color list to see if its all the same letter
#Syntax:       winning(string)
#Paramaters:   string: the global color string that is a list of 'W' and 'B' depending of what color the block is
#Return value: None

def winning(string):
    global color, board, board_objects, quit_looper
    win_white = 0
    win_black = 0
    for colo in color:
        if colo == 'W':
            win_white += 1 
        if colo == 'B':
            win_black += 1
            
    if win_black == 100 or win_white == 100:
        winner = GraphWin("WINNER", 150,200)
        the_w = Text(Point(75,25),string)
        the_w.draw(winner)
        restart_square = Rectangle(Point(25,50),Point(125,75))
        restart = Text(Point(75,62),"Restart")
        restart_square.draw(winner)
        restart.draw(winner)
        quit_square = Rectangle(Point(25,100),Point(125,125))
        quit_temp = Text(Point(75,112),"Quit")
        quit_square.draw(winner)
        quit_temp.draw(winner)
        
        menu_square = Rectangle(Point(25,150),Point(125,175))
        menu_text = Text(Point(75,162),'Main Menu')
        menu_square.draw(winner)
        menu_text.draw(winner)
        
        click = -1
        while click == -1:
               
            pix = winner.getMouse()
            
            
            #restart button 
            if (0 < (pix.x//25) < 5) and (pix.y//25) == 2:
                winner.close()
                restart_button(1)
                break
            
            #quit button
            if (0 < (pix.x//25) < 5) and (pix.y//25) == 4:
                winner.close()
                quit()
                quit_looper += 1 
                return -1
            #main menu 
            if (0 < (pix.x//25) < 5) and (pix.y//25) == 6:
                winner.close()
                eraser(board)
                eraser(board_objects)
                play_game() 
                break
            else:
                click == -1

   


#Function:     prints main menu
#Syntax:       print_main_menu()
#Paramaters:   None
#Return value: None

def print_main_menu():

    global win, menu_objects, solution
    
    solution = []
           
    title = Text(Point(250,60),"LOGIX\nby\nJayden Geisler")
    title.setSize(30)
    title.draw(win)
    
    menu_objects.append(title)
    #prints 9 squares
    square_list = []
    k = 50
    for j in range(3):
        for i in range(3):
            square_list.append(Rectangle(Point(k,200+i*100),Point(k+50,250+i*100)))
               
        k = k + 100
        
    for i in square_list:
        i.draw(win)
        menu_objects.append(i)
    #color the first six
    
    square_list[0].setFill('orange')
    square_list[1].setFill('green')
    square_list[2].setFill('purple')
    square_list[3].setFill('blue')
    square_list[4].setFill('red')
    square_list[5].setFill('pink')
    
    color_1 = Text(Point(75,175),"Color 1\npick one")
    color_1.draw(win)
    menu_objects.append(color_1)
    color_2 = Text(Point(175,175),"Color 2\npick one")
    color_2.draw(win)
    menu_objects.append(color_2)
    difficulty = Text(Point(275,175),"difficulty\npick one")
    difficulty.draw(win)
    menu_objects.append(difficulty)
    
    # diff numbers
    ten = Text(Point(275,225),"Easy")
    ten.draw(win)
    menu_objects.append(ten)
    twenty = Text(Point(275,325),"Medium")
    twenty.draw(win)
    menu_objects.append(twenty)
    fifty = Text(Point(275,425),"Hard")
    fifty.draw(win)
    menu_objects.append(fifty)
    
    #play button
    player = Rectangle(Point(350,300),Point(450,350))
    play = Text(Point(400,325),"Play!!")
    play.draw(win)
    player.draw(win)
    menu_objects.append(play)
    menu_objects.append(player)


#Function:     navagates the main menu
#Syntax:       nav_main_menu()
#Paramaters:   None
#Return value: None
    
def nav_main_menu():
    global win, color_1, color_2, difficulty, menu_objects
    collum_1 = None
    collum_2 = None
    collum_diff = None
    color_1 = None
    color_1 = None
    difficulty = None
    
    click = -1
    while click == -1:
        pix = win.getMouse()
        
        # orange
        if pix.x//50 == 1 and pix.y//50 == 4:
            color_1 = "orange"
            if collum_1 == None:
                collum_1 = Text(Point(75,225),"Orange")
                collum_1.draw(win)
            else:
                collum_1.undraw()
                collum_1 = Text(Point(75,225),"Orange")
                collum_1.draw(win)
        # green square    
        if pix.x//50 == 1 and pix.y//50 == 6:
            color_1 = "green"
            if collum_1 == None:
                collum_1 = Text(Point(75,325),"Green")
                collum_1.draw(win)
            else:
                collum_1.undraw()
                collum_1 = Text(Point(75,325),"Green")
                collum_1.draw(win)
        #purp        
        if pix.x//50 == 1 and pix.y//50 == 8:
            color_1 = "purple"
            if collum_1 == None:
                collum_1 = Text(Point(75,425),"Purple")
                collum_1.draw(win)
            else:
                collum_1.undraw()
                collum_1 = Text(Point(75,425),"Purple") 
                collum_1.draw(win)
                
        #blue        
        if pix.x//50 == 3 and pix.y//50 == 4:
            color_2 = "blue"
            if collum_2 == None:
                collum_2 = Text(Point(175,225),"Blue")
                collum_2.draw(win)
            else:
                collum_2.undraw()
                collum_2 = Text(Point(175,225),"Blue") 
                collum_2.draw(win)
        #red        
        if pix.x//50 == 3 and pix.y//50 == 6:
            color_2 = "red"
            if collum_2 == None:
                collum_2 = Text(Point(175,325),"Red")
                collum_2.draw(win)
            else:
                collum_2.undraw()
                collum_2 = Text(Point(175,325),"Red") 
                collum_2.draw(win)
        #pink        
        if pix.x//50 == 3 and pix.y//50 == 8:
            color_2 = "pink"
            if collum_2 == None:
                collum_2 = Text(Point(175,425),"Pink")
                collum_2.draw(win)
            else:
                collum_2.undraw()
                collum_2 = Text(Point(175,425),"Pink") 
                collum_2.draw(win) 
                
        #difficulty
        
        #easy
        if pix.x//50 == 5 and pix.y//50 == 4:
            difficulty = 10
            if collum_diff == None:
                collum_diff = Text(Point(275,215),"~")
                collum_diff.draw(win)
            else:
                collum_diff.undraw()
                collum_diff = Text(Point(275,215),"~") 
                collum_diff.draw(win)             

        #medium    
        if pix.x//50 == 5 and pix.y//50 == 6:
            difficulty = 25
            if collum_diff == None:
                collum_diff = Text(Point(275,315),"~")
                collum_diff.draw(win)
            else:
                collum_diff.undraw()
                collum_diff = Text(Point(275,315),"~") 
                collum_diff.draw(win)              
        #hard   
        if pix.x//50 == 5 and pix.y//50 == 8:
            difficulty = 50
            if collum_diff == None:
                collum_diff = Text(Point(275,415),"~")
                collum_diff.draw(win)
            else:
                collum_diff.undraw()
                collum_diff = Text(Point(275,415),"~") 
                collum_diff.draw(win)
        #play button        
        if (pix.x//50 == 7 or pix.x//50==8) and pix.y//50 == 6:
            if difficulty == None or color_1 == None or color_2 == None:
                error = Text(Point(400,250),"Please select your options")
                error.draw(win)
                win.getMouse()
                error.undraw()
            else:
                menu_objects.append(collum_1) 
                menu_objects.append(collum_2)                
                menu_objects.append(collum_diff) 
                eraser(menu_objects)
                click = 1
                return [color_1, color_2, difficulty]
        else:
            click = -1
            
#
#Function:     eara ses a list of objects
#Syntax:       eraser(list_of_objects)
#Paramaters:   list_of_objects: a list of graphical objects that are drawin already
#Return value: None

def eraser(list_of_objects):
    
    for i in list_of_objects:
        i.undraw()
        

#Function:     plays the game
#Syntax:       play_game()
#Paramaters:   None
#Return value: None

def play_game():
    global difficulty
    print_main_menu()
    nav_main_menu()
    
    make_board(10)
    shuffle_board(difficulty)
    play()
    

play_game()

