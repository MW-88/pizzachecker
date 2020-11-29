import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


kind_of_pizza ="salami pizza"

@app.route('/', methods=['GET'])
def home():
    text = "<h1>The pizza checker </h1><p>Dit is een voorbeeld API path </p>"
    return text

@app.route('/differentpath', methods=['GET'])
def differentpath():
    text = "<h1>This is a different path</p>"
    return text

@app.route('/pizzachecker', methods=['GET'])
def pizzachecker():

    if 'pineapple' in kind_of_pizza:
        text = "<h1>Dit is geen echte pizza </p>"
    else:
        text ="<h1>Dit is wel een echte pizza </p>"   
    return text


app.run()