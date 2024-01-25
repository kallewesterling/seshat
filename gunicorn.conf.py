import multiprocessing

# The socket to bind
bind = '0.0.0.0:8000'

# The number of worker processes for handling requests
# Since you have 8 CPUs, you might want to start with 8 workers (1 per CPU)
workers = 8

# The number of worker threads for handling requests
# This depends on your application's I/O behavior and your specific use case.
# If your application is I/O-bound, you can increase this number.
threads = 2

# Max number of requests per worker before restarting the worker
# This can help prevent memory leaks from affecting the system over time.
max_requests = 1000

# The type of workers to use
worker_class = 'sync'  # or 'gevent' for async workers

# The maximum number of simultaneous clients
# This setting is only used when worker_class is set to gevent
worker_connections = 1000

# How long to keep an idle worker running
keepalive = 2

# Logging
errorlog = '-'
loglevel = 'info'
accesslog = '-'
