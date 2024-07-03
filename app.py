from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/blog/<pk>")
def blog(pk):
    return render_template(f"blog{pk}.html")


@app.route("/user/<username>")
def hello(username):
    return render_template("calculate.html")


@app.route("/calculate")
def calculate():
    return render_template("calculate.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    a1 = request.form.get("a1")
    a2 = request.form.get("a2")
    action = request.form.get("action")
    a1, a2 = int(a1), int(a2)
    match action:
        case "add":
            result = a1 + a2
        case "sub":
            result = a1 - a2
        case "mul":
            result = a1 * a2
        case "div":
            result = a1 / a2
        case "mod":
            result = a1 % a2
        case "sbs":
            result = a1 ** a2

    return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)

