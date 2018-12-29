from flask import Flask, render_template, request, redirect
import quandl

app = Flask(__name__)

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
	last30 = quandl.get_close_price_data_1_mo(symbol)
	last30_str = " ".join(list(map(lambda x: str(x), last30)))
	return render_template('ticker.html', ticker=symbol, high=high, low=low, last30=last30_str)

if __name__ == '__main__':
  app.run(port=33507)

