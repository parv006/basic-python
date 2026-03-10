import pandas as pd
import seaborn as sns
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

root = tk.Tk()
root.geometry('1800x1100')
root.title('CSV analyst')

# Title and Entry
title = tk.Label(text='CSV analyst', font=('Sans Serif', 28, 'bold'), fg='grey')
title.pack()

url_text = tk.Label(text='enter your url below ⬇️⬇️', font=('Sans Serif', 12, 'bold'), fg='black')
url_text.place(x=700, y=70)

url = tk.Entry(width=63)
url.place(x=600, y=100)

exception_window_rectange=tk.Canvas(root,height=40,width=450)
exception_window_rectange.place(x=90,y=140)
exception_window_rectange.create_rectangle(5,5,450,40,outline='grey',width=2)
exception_window=tk.Label(text='any exception will be listed here ')
exception_window.place(x=100, y=150)

# Red rectangle for visual structure
canvas_border = tk.Canvas(root, width=900, height=350)
canvas_border.place(x=100, y=300)
canvas_border.create_rectangle(2, 3, 870, 300, outline="grey", width=5)

# Scrollable Canvas Setup
scroll_canvas = tk.Canvas(root, width=750, height=180)
scroll_canvas.place(x=150, y=350)

v_scrollbar = tk.Scrollbar(root, orient="vertical", command=scroll_canvas.yview)
v_scrollbar.place(x=900, y=350, height=180)

h_scrollbar = tk.Scrollbar(root, orient="horizontal", command=scroll_canvas.xview)
h_scrollbar.place(x=150, y=530, width=750)

scrollable_frame = tk.Frame(scroll_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: scroll_canvas.configure(
        scrollregion=scroll_canvas.bbox("all")
    )
)

scroll_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scroll_canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

label_list = []

x_options_string=tk.Label(text='x-axis attr. ⬇️')
x_options=tk.Listbox(root,selectmode=tk.SINGLE)
x_options.place(x=1200,y=110)
x_options_string.place(x=1200,y=90)

y_options_string=tk.Label(text='y-axis attr. ⬇️')
y_options=tk.Listbox(root,selectmode=tk.SINGLE)
y_options.place(x=1400,y=110)
y_options_string.place(x=1400,y=90)

seperator_text=tk.Label(text='enter the seperator⬇️ ')
seperator_entry=tk.Entry()
seperator_entry.place(x=700,y=250)
seperator_text.place(x=700,y=226)
selected_delimiter=','
def seperation_changer():
    global selected_delimiter
    selected_delimiter=str(seperator_entry.get())
def plot_heatmap(df):
    try:
        corr = df.corr(numeric_only=True)
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        sns.heatmap(corr, ax=ax, cmap="coolwarm", annot=True, fmt=".2f", cbar=True)
        ax.set_title("Correlation Matrix", fontsize=12)

        heatmap_canvas = FigureCanvasTkAgg(fig, master=root)
        heatmap_canvas.draw()
        heatmap_canvas.get_tk_widget().place(x=100, y=650, width=600, height=350)  
    except Exception as e:
        exception_window.config(text=f"Heatmap Error: {e}")
def fullscreen_heatmap():
    corr=df.corr(numeric_only=True)
    plt.figure(figsize=(20,12))
    sns.heatmap(corr,cmap='coolwarm',annot=True,fmt='.2g',cbar=True)
    plt.show()
def check_deliminer():
    with open(url.get()) as f:
            sample = f.read(2048)
    dialect = csv.Sniffer().sniff(sample)
    deli=str(repr(dialect.delimiter))
    delimiter1=tk.Label(text=f'delinimer : {deli}')
    delimiter1.place(x=800,y=150)
def generate_summary():
    global df
    try:
        with open(url.get()) as f:
            sample = f.read(2048)
        dialect = csv.Sniffer().sniff(sample)
        deli=str(repr(dialect.delimiter))
        delimiter1=tk.Label(text=f'delinimer : {deli}')
        delimiter1.place(x=700,y=180)
        df = pd.read_csv(url.get(),sep=selected_delimiter)
        summary_stats = df.describe()

        for lbl in label_list:
            lbl.destroy()
        label_list.clear()

        df_columns = df.columns.tolist()
        x_options.delete(0, tk.END)
        y_options.delete(0, tk.END)
        for column in df_columns:
            
            x_options.insert(tk.END, column)
            y_options.insert(tk.END, column)

        for i, line in enumerate(summary_stats.to_string().split('\n')):
            lbl = tk.Label(scrollable_frame, text=line, font=('Courier New', 10), anchor='w', justify='left')
            lbl.pack(anchor='w')
            label_list.append(lbl)
        plot_heatmap(df)

    except Exception as e:
        text1 = f'Exception: {e}'
        exception_window.config(text=text1)

def clear_screen():
    for lbl in label_list:
        lbl.destroy()
    label_list.clear()
    exception_window.config(text='any exception will be listed here')

def x_confirm():
    global choicex
    choicex=x_options.get(x_options.curselection())
    xx=tk.Label(text=str(choicex))
    xx.place(x=1230,y=300)
    print('runningx')
def y_confirm():
    global choicey
    choicey=y_options.get(y_options.curselection())
    yy=tk.Label(text=str(choicey))
    yy.place(x=1430,y=300)
    print('runningy')
def draw_scatter():
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.scatter(list(df[choicex]),list(df[choicey]))
    
    plot_canvas = FigureCanvasTkAgg(fig, master=root)
    plot_canvas.draw()
    plot_canvas.get_tk_widget().place(x=1000, y=400, width=780, height=600)
def draw_plot():
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.plot(list(df[choicex]),list(df[choicey]))
    
    plot_canvas = FigureCanvasTkAgg(fig, master=root)
    plot_canvas.draw()
    plot_canvas.get_tk_widget().place(x=1000, y=400, width=780, height=600)
def draw_hist():
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(111)
    plot.hist(x=list(df[choicex]) )
    
    plot_canvas = FigureCanvasTkAgg(fig, master=root)
    plot_canvas.draw()
    plot_canvas.get_tk_widget().place(x=1000, y=400, width=780, height=600)


# Buttons

check_deli=tk.Button(text='change seperator',command=seperation_changer)
check_deli.place(x=850,y=246)

fullscreen_button=tk.Button(text='fullscreen heatmap',command=fullscreen_heatmap)
fullscreen_button.place(x=100,y=1030)

summary_btn = tk.Button(text='Generate Summary of Data', command=generate_summary)
summary_btn.place(x=720, y=150)

x_sure_button=tk.Button(text='confirm X',command=x_confirm)
y_sure_button=tk.Button(text='confirm Y',command=y_confirm)
x_sure_button.place(x=1230,y=280)
y_sure_button.place(x=1430,y=280)
selected_options=tk.Label(text=f'x: {x_options.get(0)}' if x_options.size()>0 else 'No selection')
selected_options.place(x=1320,y=310)

clear_btn = tk.Button(text='Clear Text', command=clear_screen)
clear_btn.place(x=100, y=100)

graph_scatter=tk.Button(text='scatter',command=draw_scatter)
graph_plot=tk.Button(text='plot',command=draw_plot)
graph_histogram=tk.Button(text='histogram',command=draw_hist)
graph_scatter.place(x=1230,y=350)
graph_plot.place(x=1350,y=350)
graph_histogram.place(x=1470,y=350)

root.mainloop()
