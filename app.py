from flask import Flask, render_template, request, redirect
import quandl
import bokeh.plotting
import bokeh.resources
import bokeh.embed
import pandas as pd
# from bokeh.embed import components

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

@app.route('/ticker')
def ticker():
    symbol = request.args["symbol"]

    month = quandl.get_month(symbol)
    stock_ticker_symbol  = quandl.get_stock_ticker_symbol(symbol)
    last30 = quandl.get_close_price_data_1_mo(symbol)
    last30_str = " ".join(list(map(lambda x: str(x), last30)))
    return render_template('ticker.html', ticker=symbol, high=high, low=low, last30=last30)

@app.route('/ticker_input')
def ticker_input():
    return render_template('ticker_input.html')

@app.route('/plot')
def plot():
    df = quandl.get_stock_ticker_df('stock_ticker_symbol') 
    y =  list(df['Close'].head(30))
    x =  list(pd.to_datetime(df['Date'].head(30)))

    p = bokeh.plotting.figure(title="Stock Closing Price", x_axis_label='Date', y_axis_label='Price', x _axis_type='datetime')
    p.line(x, y, legend="Temp.", line_width=2)

    script, html = bokeh.embed.components(p)
    return render_template("bokeh_graph.html", bokeh_script=script, bokeh_div=html)      


if __name__ == '__main__':
  app.run(port=33507)

