import plotly.express as px
import dash
impost pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

    #tips = px.data.tips()
dataSet = pd.read_csv('X&Y.csv')
    #col_options = [dict(label=x, value=x) for x in tips.columns]
#col_options = [dict(label=x, value=x) for x in dataSet.columns]
    #dimensions = ["x", "y", "color", "facet_col","facet_row"]
#dimensions = ["x", "y"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server

app.layout = html.Div(
    [
        html.H1("Testing Plotly Express in Dash with my own Dataset"),
        html.Div(
            [
                #html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                #for d in dimensions
                fig = px.line(dataSet, x = 'X', y = 'Y', title='Apple Share Prices over time (2014)')
                fig.show()
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)

####### Callback
@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y):  #, 
                #color, 
                #facet_col,
                #facet_row
               ):
    return px.scatter(
        #tips,
        dataSet,
        x=x,
        y=y,
        #color=color,
        #facet_col=facet_col,
        #facet_row=facet_row,
        height=700,
    )
'''
if __name__ == "__main__":
    app.run_server(debug=True)
