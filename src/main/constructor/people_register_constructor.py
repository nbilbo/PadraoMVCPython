from src.controllers.people_register_controller import PeopleRegisterController
from src.views.application import Application
from src.views.people_register_view import PeopleRegisterView


class PeopleRegisterConstructor:
    def __init__(self, application: Application, people_register_view: PeopleRegisterView) -> None:
        self.__application = application
        self.__people_register_view = people_register_view

        register_button = self.__people_register_view.get_register_button()
        register_button.configure(command=self.handle_register)

        back_button = self.__people_register_view.get_back_button()
        back_button.configure(command=self.handle_back)

    def handle_back(self) -> None:
        self.__application.go_to_first_view()
        self.__people_register_view.clear_fields()
        self.__people_register_view.clear_output()

    def handle_register(self) -> None:
        new_person_informations = self.__people_register_view.get_person_informations()
        people_register_controller = PeopleRegisterController()
        response = people_register_controller.register(new_person_informations)

        if response['success']:
            self.__people_register_view.registry_person_success(response['message'])
            self.__people_register_view.clear_fields()
        else:
            self.__people_register_view.registry_person_fail(response['error'])
