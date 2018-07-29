from pyramid.config import Configurator
import webapp.controllers.home_controller as home_ctrl
import webapp.controllers.contact_controller as contact_ctrl
import webapp.controllers.mail_sent_controller as sent_ctrl

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

    add_controller_routes(config, home_ctrl.HomeController, 'home')
    add_controller_routes(config, contact_ctrl.ContactController, 'contact')
    add_controller_routes(config, sent_ctrl.MailSentController, 'mail_sent')


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id/', '/' + prefix + '/{action}/{id}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')