from tkinter_interface import Structures
import tkinter_interface
import tkinter as tk
canvas = tkinter_interface.canvas
entry = [['', '', ''], ['', '', ''], ['', '', '']]

class Interface_logic(Structures):
    def __init__(self, canvas):
        Structures.__init__(self, canvas)
        self.canvas = canvas
        self.move_ids = []
        self.xscore=0
        self.oscore=0
        self.winner_label = None
        self.clicks_enabled = True
        self.default_bg = self.canvas['bg'] if 'bg' in self.canvas.config() else '#353935'
        self.current_player = 'x'
    
    def reset_board(self):
        global entry
        for item in self.move_ids:
            self.canvas.delete(item)
        self.move_ids.clear()
        entry = [['', '', ''], ['', '', ''], ['', '', '']]
        print("Board reset!")
        self.canvas.config(bg=self.default_bg)
        self.clicks_enabled = True
        self.current_player = 'x'
        if self.winner_label:
            self.winner_label.destroy()
            self.winner_label = None
    def update_scoreboard(self):
        playerxscore.config(text=self.xscore)
        playeroscore.config(text=self.oscore)
    def show_winner(self, winner):
        if self.winner_label:
            self.winner_label.destroy()
        self.winner_label = tk.Label(self.canvas, text=f"{winner.upper()} wins!", bg='#353935', fg='white', font=('Sans Serif', 24, 'bold'), width=20)
        self.winner_label.place(x=0, y=0, relwidth=1)
        self.canvas.config(bg='#353935')
    def checkwin(self):
        global entry
        global winner
        winner = None
        for it in range(3):
            if entry[it][0] == 'x' and entry[it][1] == 'x' and entry[it][2] == 'x':
                winner = 'x'
            elif entry[0][it] == 'x' and entry[1][it] == 'x' and entry[2][it] == 'x':
                winner = 'x'
        if entry[0][0] == 'x' and entry[1][1] == 'x' and entry[2][2] == 'x':
            winner = 'x'
        if entry[2][0] == 'x' and entry[1][1] == 'x' and entry[0][2] == 'x':
            winner = 'x'

        for it1 in range(3):
            if entry[it1][0] == 'o' and entry[it1][1] == 'o' and entry[it1][2] == 'o':
                winner = 'o'
            elif entry[0][it1] == 'o' and entry[1][it1] == 'o' and entry[2][it1] == 'o':
                winner = 'o'
        if entry[0][0] == 'o' and entry[1][1] == 'o' and entry[2][2] == 'o':
            winner = 'o'
        if entry[2][0] == 'o' and entry[1][1] == 'o' and entry[0][2] == 'o':
            winner = 'o'

        if winner:
            print(f"{winner} won!")
            self.show_winner(winner)
            self.clicks_enabled = False
            if winner=='x':
                self.xscore=self.xscore+1
            elif winner=='o':
                self.oscore=self.oscore+1
            self.update_scoreboard()    
            self.canvas.after(1000, self.reset_board)
    def scorereset(self):
        playerxscore.config(text=self.xscore)  
        playeroscore.config(text=self.oscore)          
    def buttons(self):
        global reset
        reset = tk.Button(canvas, text="Reset", width=10,height=1,bg="#36454F", fg="#301934", activebackground="#28282B", activeforeground="grey",font=('Sans Serif',13,'bold'),command=self.reset_board)            
        canvas.create_window(400,100, window=reset)        
    def winnerscreen(self):
        global playeroscore
        global playerxscore
        playerxscore=tk.Label(canvas,text=self.xscore,bg='#353935',fg='grey',font=('Sans Serif',30,'bold'))
        playeroscore=tk.Label(canvas,text=self.oscore,bg='#353935',fg='grey',font=('Sans Serif',30,'bold'))
        playerxscore.place(x=44,y=415)
        playeroscore.place(x=44,y=486)    
    def place_x(self):
        def on_click(event):
            if not self.clicks_enabled or self.current_player != 'x':
                return
            grid_x0 = 135
            grid_y0 = 235
            pitch = 185  

            i = (event.x - grid_x0) // pitch
            j = (event.y - grid_y0) // pitch

            if 0 <= i <= 2 and 0 <= j <= 2:
                print(f"User clicked in grid cell: row={j}, column={i}")
                if entry[j][i] == '':
                    cross_id = Structures.cross(self, 15, i+1, j+1)
                    self.move_ids.append(cross_id)
                    entry[j][i] = 'x'
                    self.current_player = 'o'
                    self.checkwin()
                print(entry)
                return i, j
            else:
                print("Click outside grid")
                return None
        self.canvas.bind('<Button-1>', on_click)

    def place_o(self):
        def on_click(event):
            if not self.clicks_enabled or self.current_player != 'o':
                return
            grid_x0 = 135
            grid_y0 = 235
            pitch = 185  

            i = (event.x - grid_x0) // pitch
            j = (event.y - grid_y0) // pitch

            if 0 <= i <= 2 and 0 <= j <= 2:
                print(f"User clicked in grid cell: row={j}, column={i}")
                if entry[j][i] == '':
                    outer = Structures.circle(self, 60, i+1, j+1, fill='#151B1E')
                    inner = Structures.circle(self, 40, i+1, j+1, fill='#36454F')
                    self.move_ids.extend([outer, inner])
                    entry[j][i] = 'o'
                    self.current_player = 'x'
                    self.checkwin()
                print(entry)
                return i, j
            else:
                print("Click outside grid")
                return None
        self.canvas.bind('<Button-3>', on_click)
others=Structures(canvas)
if __name__=='__main__':
    

    logic = Interface_logic(canvas)
    logic.place_x()
    logic.place_o()
    logic.winnerscreen()
    logic.buttons()
    logic.reset_board()
    tkinter_interface.root.mainloop()
