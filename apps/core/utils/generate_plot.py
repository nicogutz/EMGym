from plotly.offline import plot
import plotly.express as px


def generate_plot(df):
    fig = px.line(df, template='seaborn', markers=True)
    return plot(fig, output_type='div')
