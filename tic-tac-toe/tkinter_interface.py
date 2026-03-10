import tkinter as tk
import math as mt

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=900, bg="#353935")
canvas.pack()

# Add a variable to store the number of rounds
rounds_var = tk.StringVar(value="1")

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)
class Structures():
    def __init__(self,canvas):
        self.canvas=canvas
    def title_top(self):
        titletop=tk.Label(canvas,text='Tik Tac Toe')
        titletop.config(fg='#120321',bg='#28282B',font=('Sans Serif',30,'bold'))
        titletop.place(x=280,y=10)
    def main_playground(self):
        create_rounded_rectangle(canvas,135-20,235-20,530+135+20,530+235+20,fill='#151B1E')
        create_rounded_rectangle(canvas,135,235,530+135,530+235,fill='#36454F')
    def playground_sticks_x(self,x,):
        create_rounded_rectangle(canvas,135+170*x+15*(x-1),245,135+170*x+15*x,510+235,fill='#151B1E')
    def playground_sticks_y(self,y):
        create_rounded_rectangle(canvas,135+10,235+170*y+15*(y-1),135+10+510,235+170*y+15*y,fill='#151B1E')
    def cross(self,r,x,y):
        h=60-r*mt.sqrt(2)
        x0=160+r*(1-1/mt.sqrt(2))
        y0=255+r*(1-1/mt.sqrt(2))
        mapping = [0, 2, 2.3, 2.5]
        x1 = mapping[x]
        y1 = mapping[y]
        points=[
            (x0)+ 170*(x-1)+35*(x1-2),y0 + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2) + 170*(x-1)+35*(x1-2),y0 + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2)+h + 170*(x-1)+35*(x1-2),y0+h + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0 + 170*(y-1)+35*(y1-2),
            x0+r*2*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0 + 170*(y-1)+35*(y1-2),
            x0+2*r*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2) + 170*(y-1)+35*(y1-2),
            x0+2*r*mt.sqrt(2)+h + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2)+h + 170*(y-1)+35*(y1-2),
            x0+2*r*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0+2*r*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0+2*r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2)+2*h + 170*(x-1)+35*(x1-2),y0+2*r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2)+h + 170*(x-1)+35*(x1-2),y0+2*r*mt.sqrt(2)+h + 170*(y-1)+35*(y1-2),
            x0+r*mt.sqrt(2) + 170*(x-1)+35*(x1-2),y0+2*r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0 + 170*(x-1)+35*(x1-2),y0+2*r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0 + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2)+2*h + 170*(y-1)+35*(y1-2),
            x0+h + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2)+h + 170*(y-1)+35*(y1-2),
            x0 + 170*(x-1)+35*(x1-2),y0+r*mt.sqrt(2) + 170*(y-1)+35*(y1-2)]
        return canvas.create_polygon(points, fill='#151B1E', smooth=True)
    def circle(self,r,x,y,**kwargs):
        cx, cy = 155+75+175*(x-1),255+75+175*(y-1)
        return canvas.create_oval(cx - r, cy - r, cx + r, cy + r, **kwargs)    
    def upper_background(self):
        create_rounded_rectangle(canvas,1,-100,800,150,radius=200,fill='#28282B') 
    def scoreboard(self):
        
        playerx=tk.Label(canvas,text='X',bg='#353935',fg='grey',font=('Sans Serif',22,'bold'))
        playero=tk.Label(canvas,text='O',bg='#353935',fg='grey',font=('Sans Serif',24,'bold'))
        
        playerx.place(x=49,y=360)
        playero.place(x=44,y=550)
        create_rounded_rectangle(canvas,15,400,105,550,fill='#28282B')    
        create_rounded_rectangle(canvas,25,410,95,540,fill='#353935')    
        create_rounded_rectangle(canvas,15,470,105,480,fill='#28282B')   
    def difficulty_level(self):
        difficulty_text=tk.StringVar(root)
        difficulty_text.set(' difficulty ')
        options=['  normal  ','  hard  ']
        difficulty_dropdown=tk.OptionMenu(canvas,difficulty_text,*options)
        difficulty_dropdown.config(fg='grey',bg='#36454F', activebackground="#28282B", activeforeground="grey",font=('Sans Serif',12,'bold'),highlightthickness=0)
        menu = difficulty_dropdown["menu"]
        menu.config(bg='#36454F', fg='grey', activebackground='#28282B', activeforeground='grey',font=('Sans Serif',12,'bold'))
        difficulty_dropdown.place(x=550,y=85)
    def mode(self):
        global check_var
        check_var = tk.BooleanVar()
        def dynamic():
            if check_var.get()==True:
                checkbutton.config(text='     Bot     ')
            elif check_var.get()!=True:
                checkbutton.config(text='2 Players')    
        checkbutton = tk.Checkbutton(root, text="2 Players",variable=check_var,command=dynamic,bg='#36454F',font=('Sans Serif',12,'bold'),fg='grey',activebackground='#28282B', activeforeground='grey', selectcolor="grey")
        checkbutton.place(x=150,y=83)
    

tik_tac_toe_inner_rectancgle=Structures(canvas)
tik_tac_toe_inner_rectancgle.main_playground()
tik_tac_toe_inner_rectancgle.playground_sticks_x(1)
tik_tac_toe_inner_rectancgle.playground_sticks_x(2)
tik_tac_toe_inner_rectancgle.playground_sticks_y(1)
tik_tac_toe_inner_rectancgle.playground_sticks_y(2)
others=Structures(canvas)
others.upper_background()
others.difficulty_level()
others.title_top()
others.mode()
others.scoreboard()



