# simple static wsgi app
# delwin

def simple_app(environ,start_response):
    status = '200 OK'
    body = 'Hello wors'
    headers = [
        ('Server','EP2010 Server'),
        ('Content-Length',str(len(body))),
        ('Content-Type','text/plain'),]
    # send the headers
    start_response(status,header)
    # now send the body:
    return [body]

