
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """return sum of a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)
    


@app.route('/sub')
def sub_nums():
    """subtract b from a and return difference"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)



@app.route('/mult')
def mult_nums():
    """multiply a and b and return product"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route('/div')
def div_nums():
    """divide a by b and return quotient"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

