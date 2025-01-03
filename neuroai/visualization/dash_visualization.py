import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np

# Create a basic Dash app
app = dash.Dash(__name__)

# Simulate some neuron data for interactive visualization
time_steps = 100
num_neurons = 5
activations = np.random.rand(time_steps, num_neurons)

# Create the Plotly figure
fig = go.Figure(data=go.Heatmap(z=activations.T, colorscale='Viridis'))
fig.update_layout(title='Neuron Activity Over Time', xaxis_title='Time Steps', yaxis_title='Neurons')

# Define the layout of the app
app.layout = html.Div([
    html.H1("NeuroAI Framework Visualization"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
