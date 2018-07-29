import pyramid_handlers
from webapp.controllers.base_controller import BaseController


class ContactController(BaseController):

    @pyramid_handlers.action(renderer='templates/contact/contact.pt')
    def index(self):
        return{}