from flask import Flask, render_template

app = Flask(__name__, template_folder="Templates")


@app.route("/")
def Hello():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
