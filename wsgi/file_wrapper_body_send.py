# delwin

FILE = "/tmp/hello.txt"
def simple_app(environ, start_response):
    status = "200 OK"
    fd = open(FILE)
    headers = [
        ("Server", "EP2010 Server"),
        ("Content-Length", str(os.path.getsize(FILE))),
        ("Content-Type", "text/plain"),
    ]
    start_response(status, headers)
    if "wsgi.file_wrapper" in environ:
        return environ['wsgi.file_wrapper'](fd, 1024)
    else:
        return iter(lambda: fd.read(1024), "")
