import pyramid_handlers
from webapp.controllers.base_controller import BaseController


class RobotxtController(BaseController):

    @pyramid_handlers.action(renderer='templates/robot/robot.txt)')
    def index(self):

        return {}