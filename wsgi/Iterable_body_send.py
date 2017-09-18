# delwin

def simple_app(environ, start_response):
    status = "200 OK"
    body = ["Hello", " ", "world", "!"] # list
    headers = [
        ("Server", "EP2010 Server"),
        ("Content-Length", str(len("".join(body)))),
        ("Content-Type", "text/plain"),
    ]
    # Send the headers:
    start_response(status, headers)
    # Now send the body, without brackets:
    return body
