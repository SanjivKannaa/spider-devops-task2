from werkzeug.middleware.dispatcher import DispatcherMiddleware # use to combine each Flask app into a larger one that is dispatched based on prefix
from server1 import app as server1
from server2 import app as server2
from server3 import app as server3
application = DispatcherMiddleware(server1, {'/server2': server2}, {'/server3': server3})