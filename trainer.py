import tkinter as tk
from tkinter import font as tkFont, filedialog
import constants

global filename_w2v
global filename_neural

def load_file():
    return filedialog.askopenfilename(title='Select file', filetypes=[("all files","*.*")])


def load_model(posy, type):
    global frame_trainer
    global filename_w2v
    global filename_neural

    filepath = load_file() + ''
    filename = filepath.split('/')[-1]

    label_font = tkFont.Font(family='Helvetica', size=18)

    label = tk.Label(frame_trainer, text=filename, fg=constants.FONT_COLOR, bg=constants.FRAME_BG, font=label_font, justify='left')
    label.place(relheight=0.1, rely=posy, relx=0.5, relwidth=0.4)
    if type == 1:
        filename_w2v = filepath
    else:
        filename_neural = filepath


def train_neural():
    global filename_w2v
    global filename_neural

    print(filename_w2v, filename_neural)

    # TRAIN NEURAL HERE
    print('just stub')


def create_trainer_window():
    global frame_trainer

    trainer_window = tk.Toplevel()
    trainer_window.resizable(False, False)

    canvas_trainer = tk.Canvas(trainer_window, height=constants.HEIGHT, width=constants.WIDTH)
    canvas_trainer.pack()

    bg_trainer_image = tk.PhotoImage(file=constants.BG_IMAGE)
    bg_trainer_label = tk.Label(trainer_window, image=bg_trainer_image)
    bg_trainer_label.image = bg_trainer_image
    bg_trainer_label.place(relwidth=1, relheight=1)

    frame_trainer = tk.Frame(trainer_window, bg=constants.FRAME_BG)
    frame_trainer.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    title_font = tkFont.Font(family='Helvetica', size=18)

    label = tk.Label(frame_trainer, font=title_font, fg=constants.FONT_COLOR, bg=constants.FRAME_BG, justify='left',
                     text='Тут можна завантажити дані, щоб тренувати нейронну мережу')
    label.place(relwidth=1, relheight=0.2, rely=0.05)

    button_font = tkFont.Font(family='Helvetica', size=14)

    button_w2v = tk.Button(frame_trainer, text='ЗАВАНТАЖИТИ модель Word2Vec', bg=constants.BUTTON_1, bd=1, fg=constants.FONT_COLOR, font=button_font,
                            highlightbackground='#003347', command=lambda:load_model(0.3, 1))
    button_w2v.place(relheight=0.1, rely=0.3, relx=0.05, relwidth=0.4)

    button_neural = tk.Button(frame_trainer, text='ЗАВАНТАЖИТИ модель нейронки', bg=constants.BUTTON_1, bd=1, fg=constants.FONT_COLOR, font=button_font,
                            highlightbackground='#003347', command=lambda:load_model(0.45, 2))
    button_neural.place(relheight=0.1, rely=0.45, relx=0.05, relwidth=0.4)

    button_train = tk.Button(frame_trainer, text='ТРЕНУВАТИ нейронку', bg=constants.BUTTON_2, bd=1, fg=constants.FONT_COLOR, font=button_font,
                            highlightbackground='#661d07', command=train_neural)
    button_train.place(relheight=0.1, rely=0.6, relx=0.05, relwidth=0.4)


