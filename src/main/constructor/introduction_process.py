from src.main.constructor.application_constructor import ApplicationConstructor
from src.main.constructor.first_view_constructor import FirstViewConstructor
from src.main.constructor.people_finder_constructor import PeopleFinderConstructor
from src.main.constructor.people_register_constructor import PeopleRegisterConstructor
from src.views.application import Application


def introduction_process():
    application = Application()
    application.go_to_first_view()
    ApplicationConstructor(application)

    first_view = application.get_first_view()
    FirstViewConstructor(application, first_view)

    people_register_view = application.get_people_register_view()
    PeopleRegisterConstructor(application, people_register_view)

    people_finder_view = application.get_people_finder_view()
    PeopleFinderConstructor(application, people_finder_view)

    return application
