from service import app
import os
import _thread


def startServer(port):
    app.run(host='0.0.0.0', port=int(port))


if __name__ == '__main__':
    ports = os.getenv('API_MIRROR_PORTS', app.config['PORTS'])

    # Type of 'ports' will depend on source:
    #   1. single value from config.py will be int
    #   2. comma-separated list from config.py will be tuple
    #   3. single/multi value from env will be string

    # Handles case 1
    if isinstance(ports, int):
        startServer(ports)
    else:
        # Handles case 3
        if not isinstance(ports, tuple):
            ports = ports.split(',')

        if len(ports) > 1:
            # Debugger only works in main thread, and must be disabled
            # if spawning multiple threads
            app.debug = False

            # Spawn new thread for all but one port
            for port in ports[0:-1]:
                _thread.start_new_thread(startServer, (port,))

        # Start server in main thread for remaining (or only) port
        startServer(ports[-1])
