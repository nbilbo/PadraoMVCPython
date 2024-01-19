from src.controllers.people_finder_controller import PeopleFinderController
from src.views.application import Application
from src.views.people_finder_view import PeopleFinderView


class PeopleFinderConstructor:
    def __init__(self, application: Application, people_finder_view: PeopleFinderView) -> None:
        self.__application = application
        self.__people_finder_view = people_finder_view

        back_button = self.__people_finder_view.get_back_button()
        back_button.configure(command=self.handle_back)

        find_button = self.__people_finder_view.get_find_button()
        find_button.configure(command=self.handle_find)

    def handle_back(self) -> None:
        self.__application.go_to_first_view()
        self.__people_finder_view.clear_fields()
        self.__people_finder_view.clear_output()

    def handle_find(self) -> None:
        people_finder_controller = PeopleFinderController()
        person_finder_informations = self.__people_finder_view.get_person_finder_informations()
        response = people_finder_controller.find_by_name(person_finder_informations)

        if response['success']:
            self.__people_finder_view.find_person_success(response['message'])
        else:
            self.__people_finder_view.find_person_fail(response['error'])


def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()

    person_finder_informations = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(person_finder_informations)

    if response['success']:
        people_finder_view.find_person_success(response['message'])
    else:
        people_finder_view.find_person_fail(response['error'])
