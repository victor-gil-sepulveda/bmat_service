from optparse import OptionParser
from flask import Flask
from bmatservice.service.rest.api import setup_rest_api


def run_flask_server(host="127.0.0.1", port=5000, debug=False):
    app = Flask(__name__) # create the application instance :)

    app.config.from_object(__name__) # Load config

    # Load default config and override config from an environment variable
    app.config.update(dict(
        SECRET_KEY='super secret key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    setup_rest_api(app)

    app.run(
        debug=debug,
        host=host,
        port=port,
        threaded=True # warning!
    )

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-o", "--host", dest="host",
                      default="0.0.0.0", help="Host IP address.")
    parser.add_option("-p", "--port", dest="port", type="int",
                      default=5000, help="Port to listen.")

    (options, args) = parser.parse_args()

    run_flask_server(options.host, options.port)
