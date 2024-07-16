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
    html.H1('Dashboard of Plots', style={'color': 'Brown', 'text-align':'center', 'font-size':'100px', 'text-decoration':'underline'}),
    html.Div([
        html.H2('Box Plot of BMI by Diabetes_012', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\\BoPlot-BMI vs Target.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'140px'
        })
    ]),
    html.Div([
        html.H2('Bar Plot of BMI by Diabetes_012', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\BarPlot-BMI vs Target.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'150px'
        })
    ]),
    html.Div([
        html.H2('Stacked Bar plot of individuals with Diabetes, if they have BP or Cholestrol', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\\StackedBar.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'220px'
        })
    ]),
    html.Div([
        html.H2('Histogram distribution of age', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\\Hist-Age.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'390px'
        })
    ]),
    html.Div([
        html.H2('Histogram of BMI(Body mass index)', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\\Hist-BMI.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'390px',
        })
    ]),
    html.Div([
        html.H2('Distribution of Physical-Health of Diabetic Individuals', style={'text-align':'center'}),
        html.Img(src=encode_image('Images\\Physical-Health.png'), style = {
            'padding': '20px',
            'margin': '10px',
            'border': '1px solid #ccc',
            'background-color': 'grey',
            'margin-left':'390px'
        })
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
