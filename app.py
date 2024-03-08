from pathlib import Path

import pandas as pd
import seaborn as sns

from shiny import reactive
from shiny.express import render, ui


@reactive.calc
def dat():
    mtscars_df = Path(__file__).parent / "mtcars.csv"
    mtscars_df = pandas.read_csv(mtscars_df)
    return mtscars_df


with ui.navset_card_underline():

    with ui.nav_panel("Data frame"):
        @render.data_frame
        def frame():
            # Give dat() to render.DataGrid to customize the grid
            return dat()

    with ui.nav_panel("Table"):
        @render.table
        def table():
            return dat()

# title of the project
ui.page_opts(title="Tallgrass Analytics: Cars", fillable=True)








# Add a Shiny UI sidebar for user interaction

# Use the ui.sidebar() function to create a sidebar

# Set the open parameter to "open" to make the sidebar open by default
ui.sidebar(open='open')

# Use a with block to add content to the sidebar


# Use the ui.h2() function to add a 2nd level header to the sidebar
#   pass in a string argument (in quotes) to set the header text to "Sidebar"

# Use ui.input_selectize() to create a dropdown input to choose a column
#   pass in three arguments:
#   the name of the input (in quotes), e.g., "selected_attribute"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) 
#   e.g. ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

# Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
#   pass in two arguments:
#   the name of the input (in quotes), e.g. "plotly_bin_count"
#   the label for the input (in quotes)

# Use ui.input_slider() to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you like

# Use ui.hr() to add a horizontal rule to the sidebar

# Use ui.a() to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes), e.g. "GitHub"
#   a keyword argument href= the URL for the hyperlink (in quotes), e.g. your GitHub repo URL
#   a keyword argument target= "_blank" to open the link in a new tab

# When passing in multiple arguments to a function, separate them with commas.   














   # @render_plotly
  #  def plot1():
   #     return px.histogram(px.data.tips(), y="tip", color='sex')

 #   @render_plotly
 #   def plot2():
 #       return px.histogram(px.data.tips(), y="total_bill", color_discrete_sequence=['#FF5333'])  # Specific color
