from flask import Flask, render_template, request, json
import cassTest

app = Flask(__name__)


@app.route("/findSummoner", methods=['GET'])
def find_summoner():
    data = request.args
    name = data['name']
    print(name)
    cassTest.test()
    return name


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
