from app import app

@app.route('/')
def root():
  return "hello world"

@app.route('/cole')
def cole():
  return "Fuck that dude"