import pyramid_handlers
import json
import webapp.utils as utils
from webapp.controllers.base_controller import BaseController


class TowersimController(BaseController):

    @pyramid_handlers.action(renderer='templates/tower_sim/tower_sim.pt')
    def index(self):
        d = dict()
        d['video'] = "../../static/img/tower_concept.mp4"
        d['foo'] = 1
        d['bar'] = 2
        d['get_video'] = self.get_video

        return d

    def get_video(self):
        return "tower_vid: video_name"


