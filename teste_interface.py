from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Teste da Tela')
window_width = 220
window_height = 480

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# posicionando a janela no centro
x = (screen_width /2) - (window_width /2) # largura 
y = (screen_height /2) - (window_height /2) # altura
window.geometry(f"{window_height}x{window_width}+{int(x)}+{int(y)}") # (X)+(Y) coordenates

btn1 = Button(window, text="Selecionar arquivo",padx=15,pady=7.5)
btn1.pack(pady=20, padx=20)

window.mainloop()