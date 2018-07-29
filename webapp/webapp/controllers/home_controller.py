import pyramid_handlers
import webapp.utils as utils
from webapp.controllers.base_controller import BaseController


class HomeController(BaseController):


    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return{'value' : 'index.pt'}

    @pyramid_handlers.action(renderer='templates/home/projects.pt')
    def projects(self):
        pass