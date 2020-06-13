import tkinter as tk
from tkinter import font as tkFont
import analyzer
import trainer
import constants


def main():
    root = tk.Tk()
    root.title('Аналізатор емоційного забарвлення текстів')
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=constants.HEIGHT, width=constants.WIDTH)
    canvas.pack()

    bg_image = tk.PhotoImage(file=constants.BG_IMAGE)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    frame_title = tk.Frame(root, bg=constants.FRAME_BG)
    frame_title.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.2)

    title_font = tkFont.Font(family='Fixedsys', size=28)
    title = tk.Label(frame_title, text="ВІТАЄМО\nв аналізаторі\nемоційного\nзабарвлення\nтекстів!", bg=constants.FRAME_BG,
                     font=title_font, fg=constants.FONT_COLOR, justify='left')
    title.place(relwidth=0.5, relheight=1)

    frame_button = tk.Frame(frame_title, bg=constants.FRAME_BG)
    frame_button.place(relwidth=0.5, relheight=0.8, relx=0.5, rely=0.1)

    button_font = tkFont.Font(family='Helvetica', size=14)

    button_test = tk.Button(frame_button, text="ТРЕНУВАТИ модель", bg=constants.BUTTON_1, bd=1, fg=constants.FONT_COLOR, font=button_font,
                            highlightbackground='#003347', command=trainer.create_trainer_window)
    button_test.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.25)

    button_train = tk.Button(frame_button, text="АНАЛІЗУВАТИ текст", bg=constants.BUTTON_2, bd=1, fg=constants.FONT_COLOR, font=button_font,
                             highlightbackground='#661d07', command=analyzer.create_analyzer_window)
    button_train.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.55)

    # ################
    frame_executors = tk.Frame(root, bg=constants.FRAME_BG)
    frame_executors.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.95)

    label_font = tkFont.Font(family='Helvetica', size=12)
    label = tk.Label(frame_executors, text='Створено Анастасією Мудрой(ІС-61) та Анастасією Коваленко(ІС-63)',
                     fg='#dbdbdb', bg=constants.FRAME_BG, font=label_font)
    label.place(relwidth=1, relheight=1)

    root.mainloop()

main()