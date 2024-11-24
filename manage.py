from gevent import monkey  # for handling concurrent I/O-bound tasks
monkey.patch_all()  # patches standard python libraries to make them async

import os
