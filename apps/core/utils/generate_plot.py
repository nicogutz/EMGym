from plotly.offline import plot
import plotly.express as px


def generate_plot(df):
    fig = px.line(df,
                  template='seaborn',
                  markers=True,
                  title="Exertion for exercise",

                  labels={
                      "data_count": "1/60 Seconds",
                      "_value": "Exertion",
                  },

                  )
    fig.update_layout(yaxis_range=[0.1, 1])

    return plot(fig, output_type='div')
