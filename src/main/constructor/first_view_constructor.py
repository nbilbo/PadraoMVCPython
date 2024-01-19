from src.views.application import Application
from src.views.first_view import FirstView


class FirstViewConstructor:
    def __init__(self, application: Application, first_view: FirstView) -> None:
        self.__application = application
        self.__first_view = first_view

        register_person_button = self.__first_view.get_register_person_button()
        register_person_button.configure(command=self.handle_go_to_people_register_view)

        search_person_button = self.__first_view.get_search_person_button()
        search_person_button.configure(command=self.handle_go_to_people_finder_view)

    def handle_go_to_people_register_view(self) -> None:
        self.__application.go_to_people_register_view()

    def handle_go_to_people_finder_view(self) -> None:
        self.__application.go_to_people_finder_view()
