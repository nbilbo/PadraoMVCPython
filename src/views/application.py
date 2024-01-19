import tkinter as tk
import tkinter.ttk as ttk
from typing import Tuple

from src.views.first_view import FirstView
from src.views.people_finder_view import PeopleFinderView
from src.views.people_register_view import PeopleRegisterView


class Application(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.__pages_container = ttk.Frame(self)
        self.__pages_container.configure(padding=10)
        self.__pages_container.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

        self.__first_view = FirstView(self.__pages_container)
        self.__people_register_view = PeopleRegisterView(self.__pages_container)
        self.__people_finder_view = PeopleFinderView(self.__pages_container)
        self.__inital_state()

    def __inital_state(self) -> None:
        def apply_direct_font_changes(widget: tk.Misc, font: Tuple[str, int, str]) -> None:
            if isinstance(widget, (tk.Text, ttk.Entry)):
                widget.configure(font=font)
            for children in widget.winfo_children():
                apply_direct_font_changes(children, font)

        style = ttk.Style()
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        style.configure('.', font=('arial', 16, 'normal'))
        apply_direct_font_changes(self, ('arial', 16, 'normal'))

        self.title('Aplicacao')
        self.geometry('510x510+0+0')

    def __clear_pages_container(self) -> None:
        for children in self.__pages_container.winfo_children():
            children.pack_forget()

    def go_to_first_view(self) -> None:
        self.__clear_pages_container()
        self.__first_view.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def go_to_people_register_view(self) -> None:
        self.__clear_pages_container()
        self.__people_register_view.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def go_to_people_finder_view(self) -> None:
        self.__clear_pages_container()
        self.__people_finder_view.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

    def get_first_view(self) -> FirstView:
        return self.__first_view

    def get_people_register_view(self) -> PeopleRegisterView:
        return self.__people_register_view

    def get_people_finder_view(self) -> PeopleFinderView:
        return self.__people_finder_view
