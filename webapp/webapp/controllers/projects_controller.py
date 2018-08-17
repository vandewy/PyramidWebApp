import pyramid_handlers
import webapp.utils as utils
from webapp.controllers.base_controller import BaseController


class ProjectsController(BaseController):

    @pyramid_handlers.action(renderer='templates/projects/projects.pt')
    def index(self):
        return{}

    @pyramid_handlers.action(renderer='templates/radar_sim/radar_sim.pt')
    def radar_sim(self):
        return {}

    @pyramid_handlers.action(renderer='templates/tower_sim/tower_sim.pt')
    def tower_sim(self):
        return {}

    @pyramid_handlers.action(renderer='templates/this_website/this_website.pt')
    def this_website(self):
        return {}