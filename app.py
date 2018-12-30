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
    month = request.args["month"]
    year = request.args["year"]
    month = int(month)
    year = int(year)

    # convert date to pandas 
    df = quandl.get_stock_ticker_df(symbol)
    df['Date'] = pd.to_datetime(df['Date'])

    # filter by year
    if year:
        year_mask = df['Date'].map(lambda x: x.year) == year
        df = df[year_mask]

    # filter by month
    if month:
        month_mask = df['Date'].map(lambda x: x.month) == month
        df = df[month_mask]

    y =  list(df['Close'])
    x =  list(df['Date'])

    p = bokeh.plotting.figure(title="Closing Prices of "+symbol, x_axis_label='Date', y_axis_label='Price', x_axis_type='datetime')
    p.line(x, y, legend="Closing Price.", line_width=2)

    script, html = bokeh.embed.components(p)
    return render_template("bokeh_graph.html", bokeh_script=script, bokeh_div=html)      

   # high = quandl.get_high(symbol)
    #low  = quandl.get_low(symbol)
    #last30 = quandl.get_close_price_data_1_mo(symbol)
    #last30_str = " ".join(list(map(lambda x: str(x), last30)))
    #return render_template('ticker.html', ticker=symbol, high=high, low=low, last30=last30)

@app.route('/ticker_input')
def ticker_input():
    return render_template('ticker_input.html')

@app.route('/plot')
def plot():
    df = quandl.get_stock_ticker_df('aapl') 
    y =  list(df['Close'].head(30))
    x =  list(pd.to_datetime(df['Date'].head(30)))

    p = bokeh.plotting.figure(title="closing prices", x_axis_label='date', y_axis_label='price', x_axis_type='datetime')
    p.line(x, y, legend="Temp.", line_width=2)

    script, html = bokeh.embed.components(p)
    return render_template("bokeh_graph.html", bokeh_script=script, bokeh_div=html)      


if __name__ == '__main__':
  app.run(port=33507)

