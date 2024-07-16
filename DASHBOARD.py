import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64

app = dash.Dash(__name__)

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
    html.H1('Dashboard of Plots'),
    html.Div([
        html.H2('Box Plot of BMI by Diabetes_012'),
        html.Img(src=encode_image('Images\\BoPlot-BMI vs Target.png'))
    ]),
    html.Div([
        html.H2('Bar Plot of BMI by Diabetes_012'),
        html.Img(src=encode_image('Images\BarPlot-BMI vs Target.png'))
    ]),
    html.Div([
        html.H2('Stacked Bar plot of individuals with Diabetes, if they have BP or Cholestrol'),
        html.Img(src=encode_image('Images\\StackedBar.png'))
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)