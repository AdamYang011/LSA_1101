import tkinter as tk 
import snake as snake
import SpaceShip as space
import os 


# window setting 
window = tk.Tk() 
window.title('聲控遊戲') 
window.geometry('1617x908')  # window size 
window.configure(background='black')  # background color 
 
# background image 
filename = tk.PhotoImage(file = "./img/GameStart_bk.png")
background = tk.Label(window, image = filename)  
background.place(x=0, y=0)

# get file
#snake_main = os.path.join("./Snake", "snake.py")
#space_main = os.path.join("./Space", "main_Main-Page-2.py")

#background.place(x=0, y=0, relwidth=1, relheight=1) 
 
Description = tk.Label(window, text="歡迎來到聲控遊戲,請選擇想要遊玩的遊戲",padx = 500, pady = 50, bg = "#141a2a",font='Helvetic 30 bold', fg = "#708ec0") 
#Description = tk.Label(window, text="歡迎來到聲控遊戲,請選擇想要遊玩的遊戲", width="50", height="10", bg = "#141a2a", font=100, fg = "#708ec0") 
Description.pack() 
photo1 = tk.PhotoImage(file = "./img/snake.png")
photo2 = tk.PhotoImage(file = "./img/SpaceShip.png")
photoimage = photo1.subsample(3,3)
photoimage2 = photo2.subsample(1,1)
snake_start_btn = tk.Button(window,relief="raised",text='開始貪食蛇', font='Helvetic 30 bold',image=photoimage,compound = 'left', padx=10,pady=10,command=snake.main,fg="blue",bg="skyblue") 
ship_start_btn = tk.Button(window, relief="raised",text='開始雷霆戰機', font='Helvetic 30 bold',image=photoimage2,compound = 'left', padx=15,pady=15,command=space.main,fg="blue",bg="skyblue") 


snake_start_btn.place(x=200,y=200) 
ship_start_btn.place(x=850,y=200) 
 
window.mainloop() 
