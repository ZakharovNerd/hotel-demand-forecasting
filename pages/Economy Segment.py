# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from heatmapcalendar import create_calendar_heatmap


LOGGER = get_logger(__name__)


def run():
    st.title("Calendar Heatmap")

    # Sample data (you can modify this part to accept user input or different data sources)
    values =  [ 24, 20, 16, 26, 28, 37, 30,
                23, 22, 24, 25, 24, 33, 30,
                26, 26, 27, 23, 27, 34, 20,
                28, 30, 24, 24, 31, 30, 31,
                24, 23]

    days_of_month = list(range(1, 31))

    # Creating the heatmap
    fig, ax = create_calendar_heatmap(values, days_of_month)

    # Displaying the heatmap in Streamlit
    st.pyplot(fig)

    st.title("Weather Forecast ")

    # Sample data (you can modify this part to accept user input or different data sources)
    values = [2.4, 4.5, 5.3, 2.2, 0.6, 3.1, 2.2, 0.9, 1.4, 5.3, 0.0, 2.7, 0.2, 3.3, 4.5, 2.2, 3.5, 0.3, 0.2, 4.5, 5.4, 0.1, 4.1, 0.9, 1.2, 3.0, 0.0, 4.4, 1.6, 0.3]

    days_of_month = list(range(1, 31))

    # Creating the heatmap
    fig, ax = create_calendar_heatmap(values, days_of_month)

    st.pyplot(fig)

if __name__ == "__main__":
    run()
