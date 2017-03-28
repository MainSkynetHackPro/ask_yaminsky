from cgi import urlparse, escape


def app(environ, start_response):
    get_data = urlparse.parse_qs(environ.get('QUERY_STRING', ''))

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    post_data = urlparse.parse_qs(request_body)

    if post_data:
        print 'POST: {0}'.format(post_data)

    if get_data:
        print 'GET: {0}'.format(get_data)

    form = '''
        <form action="/" method="POSt">
        <input name="text" type="test">
        <input type="submit">
        </form>
    '''
    start_response('200 OK', [('Content-Type', 'text/html')])
    return 'GET: {0}<br> POST: {1}<br>{2}'.format(get_data, post_data, form)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, app)
    srv.serve_forever()