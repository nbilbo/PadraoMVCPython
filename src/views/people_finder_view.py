import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from typing import Dict


class PeopleFinderView(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.__back_button = ttk.Button(self)
        self.__back_button.configure(text='Voltar para inicio')
        self.__back_button.pack(side=tk.TOP, anchor=tk.W)

        title_label = ttk.Label(self)
        title_label.configure(text='Buscar Pessoa')
        title_label.configure(font=('Arial', 20, 'bold'))
        title_label.configure(anchor=tk.CENTER)
        title_label.pack(side=tk.TOP, fill=tk.X)

        name_label = ttk.Label(self)
        name_label.configure(text='Determine o nome da pessoa para busca')
        name_label.configure(anchor='center')
        name_label.pack(side=tk.TOP, fill=tk.X)

        self.__name_entry = ttk.Entry(self)
        self.__name_entry.configure(justify=tk.CENTER)
        self.__name_entry.pack(side=tk.TOP, fill=tk.X)

        self.__output_container = ttk.Frame(self)
        self.__output_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, pady=10)

        self.__output = tk.Text(self.__output_container)
        self.__output.configure(width=1, height=1)
        self.__output.configure(state=tk.DISABLED)
        self.__output.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.__output_scroller = ttk.Scrollbar(self.__output_container, orient=tk.VERTICAL)
        self.__output_scroller.pack(side=tk.LEFT, fill=tk.BOTH)

        self.__output_scroller.configure(command=self.__output.yview)
        self.__output.configure(yscrollcommand=self.__output_scroller.set)

        self.__find_button = ttk.Button(self)
        self.__find_button.configure(text='Buscar')
        self.__find_button.pack(side=tk.BOTTOM, fill=tk.X)

    def get_back_button(self) -> ttk.Button:
        return self.__back_button

    def get_find_button(self) -> ttk.Button:
        return self.__find_button

    def get_name(self) -> str:
        return self.__name_entry.get()

    def get_person_finder_informations(self) -> Dict[str, str]:
        name = self.get_name()

        return {'name': name}

    def set_output(self, message: str) -> None:
        self.__output.configure(state=tk.NORMAL)
        self.__output.delete(0.0, tk.END)
        self.__output.insert(tk.END, message)
        self.__output.configure(state=tk.DISABLED)

    def set_name(self, name: str) -> None:
        self.__name_entry.delete(0, tk.END)
        self.__name_entry.insert(tk.END, name)

    def clear_output(self) -> None:
        self.set_output('')

    def clear_fields(self) -> None:
        self.set_name('')

    def find_person_success(self, message: Dict) -> None:
        success_message = f"""
            Usuario encontrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["infos"]["name"] }
                Idade: { message["infos"]["age"] }
                Altura: { message["infos"]["height"] }
        """
        self.set_output(success_message)

    def find_person_fail(self, error: str) -> None:
        fail_message = f"""
            Falha ao encontrar usuario!

            Erro: { error }
        """
        self.set_output(fail_message)
