#Memory Game

import simplegui
import random

cards1 = [1, 2, 3, 4, 5, 6, 7, 8]
cards2 = [1, 2, 3, 4, 5, 6, 7, 8]
turns = 0

# helper function to initialize globals
def new_game():
    global cards
    global exposed
    global turns
    global state
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    
    cards = cards1 + cards2
    random.shuffle(cards)
    
    exposed = [False, False, False, False, False, False,
               False, False, False, False, False, False,
               False, False, False, False]

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global turns
    global tmp
    global tmp1
    global tmp2
    x1 = 0
    x2 = 50

    for i in range(0,16):
        if pos[0] >= x1 and pos[0] < x2:
            if exposed[i] == False:   
                exposed[i] = True
                tmp = i
        x1 += 50
        x2 += 50  
    
    if state == 0:  
        tmp1 = tmp
        turns = 1
        label.set_text("Turns = " + str(turns))
        state = 1
    elif state == 1:
        if tmp <> tmp1:
            tmp2 = tmp
            state = 2
    else:
        if tmp <> tmp2:
            if not cards[tmp1] == cards[tmp2]:
                exposed[tmp1] = False
                exposed[tmp2] = False
            tmp1 = tmp
            turns += 1
            label.set_text("Turns = " + str(turns))
            state = 1
                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed

    x = 0
    for card in cards:
        canvas.draw_line((0+x, 0), (0+x, 100), 1, 'Red')
        canvas.draw_text(str(card), (6+x, 75), 72, 'White')
        x += 50
    x = 0

    for expose in exposed:
        if expose == False:
            canvas.draw_line((25+x, 0), (25+x, 100), 48, 'Green')    
        x += 50
             
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
