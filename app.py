from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# functions
def get_stock_ticker_data(symbol):
	return "my symbol is %s" % symbol

# Routes
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/secret')
def secret():
	return "this is a secret"

@app.route('/myticker/<symbol>')
def myticker(symbol):
	return get_stock_ticker_data(symbol)

if __name__ == '__main__':
  app.run(port=33507)
