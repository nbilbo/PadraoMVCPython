import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from typing import Any, Dict


class PeopleRegisterView(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.__back_button = ttk.Button(self)
        self.__back_button.configure(text='Voltar para inicio')
        self.__back_button.pack(side=tk.TOP, anchor=tk.W)

        title_label = ttk.Label(self)
        title_label.configure(text='Cadastrar Nova Pessoa')
        title_label.configure(font=('Arial', 20, 'bold'))
        title_label.configure(anchor=tk.CENTER)
        title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        name_label = ttk.Label(self)
        name_label.configure(text='Determine o nome da pessoa')
        name_label.configure(anchor=tk.CENTER)
        name_label.pack(side=tk.TOP, fill=tk.X)

        self.__name_entry = ttk.Entry(self)
        self.__name_entry.configure(justify='center')
        self.__name_entry.pack(side=tk.TOP, fill=tk.X)

        age_label = ttk.Label(self)
        age_label.configure(text='Determine a idade da pessoa')
        age_label.configure(anchor=tk.CENTER)
        age_label.pack(side=tk.TOP, fill=tk.X)

        self.__age_entry = ttk.Entry(self)
        self.__age_entry.configure(justify='center')
        self.__age_entry.pack(side=tk.TOP, fill=tk.X)

        height_label = ttk.Label(self)
        height_label.configure(text='Determine a altura da pessoa')
        height_label.configure(anchor=tk.CENTER)
        height_label.pack(side=tk.TOP, fill=tk.X)

        self.__height_entry = ttk.Entry(self)
        self.__height_entry.configure(justify='center')
        self.__height_entry.pack(side=tk.TOP, fill=tk.X)

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

        self.__register_button = ttk.Button(self)
        self.__register_button.configure(text='Cadastrar')
        self.__register_button.pack(side=tk.BOTTOM, fill=tk.X)

    def get_person_informations(self) -> Dict[str, str]:
        name = self.get_name()
        age = self.get_age()
        height = self.get_height()

        return {'name': name, 'age': age, 'height': height}

    def get_name(self) -> str:
        return self.__name_entry.get()

    def get_age(self) -> str:
        return self.__age_entry.get()

    def get_height(self) -> str:
        return self.__height_entry.get()

    def get_register_button(self) -> ttk.Button:
        return self.__register_button

    def get_back_button(self) -> ttk.Button:
        return self.__back_button

    def set_name(self, name: str) -> None:
        self.__name_entry.delete(0, tk.END)
        self.__name_entry.insert(tk.END, name)

    def set_age(self, age: str) -> None:
        self.__age_entry.delete(0, tk.END)
        self.__age_entry.insert(tk.END, age)

    def set_height(self, height: str) -> None:
        self.__height_entry.delete(0, tk.END)
        self.__height_entry.insert(tk.END, height)

    def set_output(self, message: str) -> None:
        self.__output.configure(state=tk.NORMAL)
        self.__output.delete(0.0, tk.END)
        self.__output.insert(tk.END, message)
        self.__output.configure(state=tk.DISABLED)

    def clear_fields(self) -> None:
        self.set_name('')
        self.set_age('')
        self.set_height('')

    def clear_output(self) -> None:
        self.set_output('')

    def registry_person_success(self, message: Dict[Any, Any]) -> None:
        success_message = f"""
            Usuario cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["name"] }
                Idade: { message["attributes"]["age"] }
                Altura: { message["attributes"]["height"] }
        """
        self.set_output(success_message)

    def registry_person_fail(self, error: str) -> None:
        fail_message = f"""
            Falha ao cadastrar usuario!

            Erro: { error }
        """
        self.set_output(fail_message)
