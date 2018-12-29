from flask import Flask, render_template, request, redirect
import quandl

app = Flask(__name__)

# functions
def get_stock_ticker_data(symbol):
	return "my max price: %s\n\nmy min price:%s" % (quandl.get_high(symbol), quandl.get_low(symbol))

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

@app.route('/ticker/<symbol>')
def ticker(symbol):
	high = quandl.get_high(symbol)
	low  = quandl.get_low(symbol)
	return render_template('ticker.html', ticker=symbol, high=high, low=low)
	# return get_stock_ticker_data(symbol)

if __name__ == '__main__':
  app.run(port=33507)

