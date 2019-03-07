from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure



app = Flask(__name__)


@app.route('/')
def homepage():
    title = 'home'

    #First Plot
    from graphs import call_bar_graph
    p1 = call_bar_graph()

    #Second Plot
    from graphs import call_year_graph
    p2 = call_year_graph()

    script, div = components(p1)
    script2, div2 = components(p2)

    return render_template('index.html', title = title, script = script,
    div = div,script2 = script2,div2 = div2)

if __name__ == '__main__':
    app.run()
