import pyramid_handlers
import webapp.utils as utils
from webapp.controllers.base_controller import BaseController


class ThiswebsiteController(BaseController):

    @pyramid_handlers.action(renderer='templates/this_website/this_website.pt')
    def index(self):

        return {}

