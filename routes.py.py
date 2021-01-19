from flask import Flask

@app.route('/home')
@app.route('/')
def hello_world():
    return '''
    <h1> Whato to Eat Today </h1>
    '''