import tkinter as tk
import tkinter.ttk as ttk


class FirstView(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        title_label = ttk.Label(self)
        title_label.configure(text='Bem Vindo(a)')
        title_label.configure(font=('Arial', 20, 'bold'))
        title_label.configure(anchor=tk.CENTER)
        title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.__register_person_button = ttk.Button(self)
        self.__register_person_button.configure(text='Cadastrar Pessoa')
        self.__register_person_button.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.__search_person_button = ttk.Button(self)
        self.__search_person_button.configure(text='Buscar Pessoa')
        self.__search_person_button.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def get_register_person_button(self) -> ttk.Button:
        return self.__register_person_button

    def get_search_person_button(self) -> ttk.Button:
        return self.__search_person_button
