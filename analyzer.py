import tkinter as tk
from tkinter import font as tkFont, filedialog
import constants
import pandas as pd


def output_file_content(content):
    global frame_analyzer
    text_output = tk.Text(frame_analyzer, pady=10, padx=20, bg=constants.FRAME_BG, fg=constants.FONT_COLOR)
    text_output.insert(tk.END, content)

    text_output.place(rely=0.5, relheight=0.45, relwidth=0.9, relx=0.05)

def processing_data(data):
    ##     WRITE RESULTS TO SCV FILE WITH NAME filename
    ##     THEN OPEN THIS FILE AND OUTPUT ALL CONTENT
    #     content = pd.read_csv('results/' + filename)

    content = data # just stub
    pd.set_option('display.max_rows', None)
    output_file_content(content)

def choose_file():
    chosen_filename = filedialog.askopenfile(initialdir='/models', title='Select file', filetypes=[("csv files","*.csv"),("all files","*.*")])
    df = pd.read_csv(chosen_filename)

    processing_data(df)


def read_text():
    global text_input
    input_content = text_input.get("1.0",tk.END)

    processing_data(input_content)


def create_analyzer_window():
    global frame_analyzer
    global text_input

    analyzer_window = tk.Toplevel()
    analyzer_window.resizable(False, False)

    canvas_analyzer = tk.Canvas(analyzer_window, height=constants.HEIGHT, width=constants.WIDTH)
    canvas_analyzer.pack()

    bg_analyzer_image = tk.PhotoImage(file=constants.BG_IMAGE)
    bg_analyzer_label = tk.Label(canvas_analyzer, image=bg_analyzer_image)
    bg_analyzer_label.image = bg_analyzer_image
    bg_analyzer_label.place(relwidth=1, relheight=1)

    frame_analyzer = tk.Frame(analyzer_window, bg=constants.FRAME_BG)
    frame_analyzer.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    title_font = tkFont.Font(family='Helvetica', size=18)

    label = tk.Label(frame_analyzer, font=title_font, fg=constants.FONT_COLOR, bg=constants.FRAME_BG, justify='left', text='Завдяки даному додатку ви можете визначити емоційне забарвлення  \nтекстів. Для цього введіть необхідний текст в поле вводу \nчи завантажте csv-файл.')
    label.place(relwidth=1, relheight=0.2, rely=0.05)

    text_input = tk.Text(frame_analyzer, wrap='word', pady=10, padx=10)
    text_input.place(relwidth=0.43, relheight=0.1, rely=0.3, relx=0.05)

    button_font = tkFont.Font(family='Helvetica', size=14)

    process_text_button = tk.Button(frame_analyzer, text='ЗЧИТАТИ текст', command=read_text, bg=constants.BUTTON_1, bd=1, fg=constants.FONT_COLOR, font=button_font,
                            highlightbackground='#003347')
    process_text_button.place(relwidth=0.2, relheight=0.1, rely=0.3, relx=0.5)

    label_input = tk.Label(frame_analyzer, text='або', fg=constants.FONT_COLOR, bg=constants.FRAME_BG)
    label_input.place(relwidth=0.05, relheight=0.1, rely=0.3, relx=0.7)

    choose_file_button = tk.Button(frame_analyzer, text='ОБРАТИ файл', command=choose_file, bg=constants.BUTTON_2, bd=1, fg=constants.FONT_COLOR, font=button_font,
                             highlightbackground='#661d07')
    choose_file_button.place(relwidth=0.2, relheight=0.1, rely=0.3, relx=0.75)





