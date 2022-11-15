from flask import Flask
from api.api import api_blueprint
from main.views import main_bp


app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_404(error):
    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):
    return "500 Internal Server Error"


if __name__ == '__main__':
    app.run(port=8000)

