from flask import Flask, render_template, request, redirect
import quandl
import bokeh.plotting
import bokeh.resources
import bokeh.embed
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

    high = quandl.get_high(symbol)
    low  = quandl.get_low(symbol)
    last30 = quandl.get_close_price_data_1_mo(symbol)
    last30_str = " ".join(list(map(lambda x: str(x), last30)))
    return render_template('ticker.html', ticker=symbol, high=high, low=low, last30=last30)

@app.route('/ticker_input')
def ticker_input():
    return render_template('ticker_input.html')

@app.route('/plot')
def plot():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = bokeh.plotting.figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend="Temp.", line_width=2)

    script, div = bokeh.embed.components(p)
    return render_template("bokeh_graph.html", script=script, div=div)      


if __name__ == '__main__':
  app.run(port=33507)

