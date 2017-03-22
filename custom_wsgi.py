def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print()
    return [b'Hello, Finn the human!']

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('', 8081, app)
        print('Serving on port 8081...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')