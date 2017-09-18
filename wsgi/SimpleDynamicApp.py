# simpli dynamic wsgi app
# delwin

def dynaming_app(environ,start_response):
    headers = [
        ('Content-Type','text/plain'),
    ]

    if environ['REQUEST_METHOD'] == 'GET':
        status = '200 OK'
        body = 'Hello Word!'
    else:
        status = '405 Method Not Allowed'
        body = 'What are you trying to do?'
        headers.append(('Allow','GET'))
    header.append(('Content-Length',str(len(body))))
    start_response(status,headers)
    return [body]

          
