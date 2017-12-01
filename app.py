from flask import Flask, send_file
import cassiopeia as cass
from Run_keras import buildModel

import views.summoner
import views.predict

app = Flask(__name__)

app.register_blueprint(views.summoner.summoner_api, url_prefix="/summoner")
app.register_blueprint(views.predict.predict_api, url_prefix="/predict")


@app.route("/")
def main():
    return send_file('static/app/index.html')


@app.before_first_request
def cass_setup():
    cass.apply_settings("cassSettings.json")
    buildModel()


if __name__ == "__main__":
    app.run(debug=True)
