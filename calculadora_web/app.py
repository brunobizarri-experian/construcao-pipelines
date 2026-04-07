from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            match operacao:
                case "soma":
                    resultado = num1 + num2
                case "subtracao":
                    resultado = num1 - num2
                case "multiplicacao":
                    resultado = num1 * num2
                case "divisao":
                    resultado = num1 / num2
        except ZeroDivisionError:
            resultado = "Erro: divisão por zero"
        except ValueError:
            resultado = "Erro: valores inválidos"

    return render_template("index.html", resultado=resultado)


def create_app():
    return app
