import customtkinter as ctk
from customtkinter import *

app = ctk.CTk()
app.geometry('700x500')

class pagina_modelo():
    def __init__(self, largura, altura, borda, cor_borda, curvatura):
        frame = CTkFrame(
            self.largura= largura,
            height=50,
            border_width=1,
            border_color='white',
            corner_radius=10
        )
        frame.pack(pady=10)

frame = pagina_modelo(100,50,1,'white',10)
fram2 = pagina_modelo()
        
app.mainloop()