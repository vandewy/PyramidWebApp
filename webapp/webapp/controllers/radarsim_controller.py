import pyramid_handlers
import json
import webapp.utils as utils
from webapp.controllers.base_controller import BaseController

class RadarsimController(BaseController):

    @pyramid_handlers.action(renderer='templates/radar_sim/radar_sim.pt')
    def index(self):
        return {}