import flask
app = flask.Flask('app')

@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/engine.js')
def enginejs():
    return flask.render_template('engine.js')
@app.route('/favicon.ico')
def favicon():
    return flask.redirect('/static/favicon.ico')

app.run(host='0.0.0.0', port=8080)