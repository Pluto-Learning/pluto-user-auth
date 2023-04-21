import multiprocessing

bind = "0.0.0.0:2000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 30
keepalive = 2
graceful_timeout = 30
max_requests = 1000
max_requests_jitter = 50
preload_app = True