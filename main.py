from flask import Flask
from threading import Lock
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

foo: int = 0
foo_lock: Lock = Lock()

bar: [int] = []
bar_lock: Lock = Lock()


@swag_from(
    {
        "responses": {
            "200": {
                "description": "A list of integers",
            }
        },
    }
)
@app.route("/", methods=["POST"])
def bar_post():
    """Adds 1 to bar"""
    with bar_lock:
        bar.append(1)
    return bar


@swag_from(
    {
        "responses": {
            "200": {
                "description": "An integer incremented by 1",
            }
        },
    }
)
@app.route("/", methods=["PUT"])
def foo_put():
    """Increments foo by 1"""
    global foo
    with foo_lock:
        foo += 1
    return f"{foo}"


@swag_from(
    {
        "responses": {
            "200": {
                "description": "0",
            }
        },
    }
)
@app.route("/", methods=["DELETE"])
def foo_delete():
    """Sets foo to 0"""
    with foo_lock:
        global foo
        foo = 0
    return foo


@swag_from(
    {
        "responses": {
            "200": {
                "description": "A string containing the values of foo and bar",
            }
        },
    }
)
@app.route("/", methods=["GET"])
def index_get():
    """Returns a string containing the values of foo and bar"""
    with foo_lock:
        with bar_lock:
            return f"Foo: {foo} \n Bar: {bar}"


if __name__ == "__main__":
    app.run(debug=True)
