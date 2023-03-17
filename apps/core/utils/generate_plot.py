from plotly.offline import plot
import plotly.graph_objs as go


def generate_plot():
    fig = go.Figure()
    scatter = go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 2, 3], mode='lines', name='test', opacity=0.8)
    fig.add_trace(scatter)
    return plot(fig, output_type='div')
