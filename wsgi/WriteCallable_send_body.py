# delwin

def simple_app(environ, start_response):
    status = "200 OK"
    body = "Hello world!" # string
    headers = [
        ("Server", "EP2010 Server"),
        ("Content-Length", str(len(body))),
        ("Content-Type", "text/plain"),
    ]
    # Send the headers and get the writer:
    write = start_response(status, headers)
    # Now send the body:
    write(body)
    # Continue “writing” if necessary...
