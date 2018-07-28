from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    cfg_settings = config.get_settings()
    db_file = cfg_settings.get('db_file')

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('projects', '/projects')
    config.scan()
    return config.make_wsgi_app()
