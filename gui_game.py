import PySimpleGUI as sg
import time
import random
from playsound import playsound
import threading

#Defining variables for counting number of tries and score
i=0
score=0



#Defining methods for playing sounds independent of the main thread
def lost():
    threading.Thread(target=playsound, args=('C:/Users/soham/Desktop/gui game/lost.mp3',), daemon=True).start()
def win():
    threading.Thread(target=playsound, args=('C:/Users/soham/Desktop/gui game/victory.mp3',), daemon=True).start()



# Define the window's contents
sg.theme('Material2')
layout = [[sg.Text('This is the classic rock,paper and scissors game\nYou have to select your choice to play\nHave fun!', font='Helvetica 10', text_color='black', background_color='white')],
          [sg.Text('author:soham Chakraborty & Akhil Boddul')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('rock',button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename='C:/Users/soham/Desktop/gui game/stone.png', image_size=(50, 50), image_subsample=10, border_width=0), 
               sg.Button('paper', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename='C:/Users/soham/Desktop/gui game/paper.png', image_size=(50, 50), image_subsample=10, border_width=0),
               sg.Button('scissors', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename='C:/Users/soham/Desktop/gui game/cut.png', image_size=(50, 50), image_subsample=10, border_width=0) , 
               sg.Button('score')]]


# Create the window
window = sg.Window('Rock, paper and scissors game', layout)



# Display and interact with the Window using an Event Loop
while True:
    sample_set = {'rock', 'paper', 'scissors'}
    item = random.choice(tuple(sample_set))

    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED:
        window['-OUTPUT-'].Update("your score is "+str(score)+"/"+str(i-1))
        time.sleep(2)
        break

    elif event==item:
        window['-OUTPUT-'].Update("TIE")
        

    elif event=='rock' and item=='paper':
        window['-OUTPUT-'].Update("COMPUTER WON")
        i+=1
        lost()
        
    elif event=='paper' and item=='scissors':
        window['-OUTPUT-'].Update("COMPUTER WON")
        i+=1
        lost()
        
    
    elif event=='scissors' and item=='rock':
        window['-OUTPUT-'].Update("COMPUTER WON")
        i+=1
        lost()
        

    elif event=='rock' and item=='scissors':
        window['-OUTPUT-'].Update("YOU WIN")
        score+=1
        i+=1
        win()

    elif event=='paper' and item=='rock':
        window['-OUTPUT-'].Update("YOU WIN")
        
        score+=1
        i+=1
        win()

    elif event=='scissors' and item=='paper':
        window['-OUTPUT-'].Update("YOU WIN")
        
        score+=1
        i+=1
        win()
    
    elif event=='score':
        window['-OUTPUT-'].Update("your score is "+str(score)+"/"+str(i))

window['-OUTPUT-'].Update("GAME ENDED")

# if score>i:
#     window['-OUTPUT-'].Update("Congratulations you beat the pc")
# else:
#     window['-OUTPUT-'].Update("The pc won try again!")
        

        


    

# For removing window from the screen
window['-OUTPUT-'].Update("BYE.....")
time.sleep(3)
window.close()