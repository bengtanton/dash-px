import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

tips = px.data.tips()
dataSet=pd.read_csv('X&Y.csv')
#col_options = [dict(label=x, value=x) for x in tips.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
server = app.server
   fig = px.scatter(tips, x="total_bill", y="tip", color="size", facet_col="sex",
          color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
        fig.show()

#app.layout = html.Div(
 #   [
  #      html.H1("Plotly Express in Dash with Tips Dataset"),
        
       # fig = px.scatter(tips, x="total_bill", y="tip", color="size", facet_col="sex",
        #   color_continuous_scale=px.colors.sequential.Viridis, render_mode="webgl")
        #fig.show()
        #html.Div(
                     #[
             #  html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
              #  for d in dimensions
            #],
            #style={"width": "25%", "float": "left"},
        #),
        #dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
   # ]
#)


#@app.callback(Output("graph", "figure"))
#def make_figure(x, y):
 #   return px.scatter(
  #      dataSet,
   #     x=x,
    #    y=y,
     #   height=700,
    #)

if __name__ == "__main__":
    app.run_server(debug=True)
