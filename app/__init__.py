from app.view import View
from app.controller import Controller


class App(View, Controller):
    """
    Implementation of the application.

    This class glues together the logic, controllers, and views of the app.

    The app is subdivided using a Model-View-Controller architecture, with files logically co-located according to this structure.
    - As such, files relating to business logic is found in the `logic` folder.
    - Files relating to the controller are found in the `controllers` folder.
    - Files relating to the view are found in the `view` folder.

    """

    def __init__(self):
        super().__init__()

    def start(self):
        pass

    def exit(self):
        pass
