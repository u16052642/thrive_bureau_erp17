import warnings
import thrive.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "thrive.service.wsgi_server.application to thrive.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return thrive.http.root(environ, start_response)
