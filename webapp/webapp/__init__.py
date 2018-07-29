from pyramid.config import Configurator
import webapp.controllers.home_controller as home_ctrl

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_routing(config)
    cfg_settings = config.get_settings()
    db_file = cfg_settings.get('db_file')

    config.scan()
    return config.make_wsgi_app()


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_handler('root', '/', handler=home_ctrl.HomeController, action='index')
    config.add_handler('home_controller', '/home/{action}', handler=home_ctrl.HomeController)
    config.add_handler('home_controller/', '/home/{action}/', handler=home_ctrl.HomeController)
    config.add_handler('home_controller_id/', '/home/{action}/{id}', handler=home_ctrl.HomeController)
    


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')