import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # this uses the Palmer Penguin dataset

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

penguins_df.describe()
penguins_df.head()
penguins_df.tail()

# Listing all column names in the DataFrame
column_names = penguins_df.columns.tolist()
print(column_names)


ui.page_opts(title="Waddle Analytics and Tuxedo Tally'24", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip", color='sex')

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill", color_discrete_sequence=['#FF5333'])  # Specific color
