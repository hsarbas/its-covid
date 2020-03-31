from flask import Flask


class CovidDb(Flask):
    def __init__(self):
        super(CovidDb, self).__init__(__name__)
        self.add_url_rule('/hello/', '/', self.hello_world)
        self.add_url_rule('/', '/', self.hello_world)
        self.register_error_handler(404, self.my_404)

    def hello_world(self):
        return f'Hello World!'

    def my_404(self, error):
        # render custom error 404 page
        return f'ERROR 404: Page not found!', 404


if __name__ == '__main__':
    app = CovidDb()
    app.run()
