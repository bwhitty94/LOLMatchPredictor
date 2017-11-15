from flask import Flask, send_file
import cassiopeia as cass

import views.summoner

app = Flask(__name__)


app.register_blueprint(views.summoner.summoner_api, url_prefix="/summoner")


@app.route("/")
def main():
    return send_file('static/app/index.html')


@app.before_first_request
def cass_setup():
    cass.apply_settings("cassSettings.json")


if __name__ == "__main__":
    app.run(port="8080")
