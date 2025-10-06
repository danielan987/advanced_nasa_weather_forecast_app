# Long-term Weather Forecasting App by Future Clouds

## Summary
Many people schedule their trips months in advance but worry about how the weather might affect their trips. 

An app that provides long-term weather predictions for a user's trip location. This is made possible by leveraging 40 years of NASA Earth data to forecast weather patterns 365 days into the future. This app also provides additional analyses on historical data, trends, and seasonality. Providing users a  their trip. 



## Project Demonstration
https://1drv.ms/p/c/460e9917ad8d3df0/ETg2DnHyyJFEqU0xyWeFO6UBm2CD49flAYEC6VWQzxJ5jQ

## Project Details

### Challenge
It is challenging to predict the weather many months in advance. So we often hope for the best that the weather won't be too hot or cold, too humid or dry, or it won't rain or snow too much. As a result, many trips, particularly outdoor trips, have been ruined by unexpected bad weather.   

### Solution
A user-friendly app that can visualize a long-term weather forecast and other weather analyses at any location on Earth. Users only need to select their trip location and do not need to already decide on potential dates. This app can help them choose the exact optimal dates within the upcoming year for their trip. 

### Methodology Overview 

This app was designed to be lightweight for fast analyses. It was developed using only one programming language (Python) on Streamlit. An automated Prophet model from Meta was also used to generate the analyses. 

This app was also designed to be accessible for people worldwide. By using OpenStreetMap for the map, users can zoom in and see the name of each region in its native language. English was used for labels in the app. However, they are accompanied by emojis to support non-English speaking users. This makes it easier for all users to identify their exact trip location. So the app can send the correct longitude and latitude data to the NASA POWER API to retrieve the weather data. 

<img width="209" height="498" alt="Screenshot 2025-10-05 at 8 27 26 PM" src="https://github.com/user-attachments/assets/1b57b82b-4f32-4439-9531-1190700bbda5" />

### Data

Modern-Era Retrospective analysis for Research and Applications, Version 2 (MERRA-2) data from 1981 to the present day can be retrieved by the NASA POWER API. 

Many MERRA-2 weather data products could have been selected for this app. However, the 3 products selected for this app were the following:  

* "PRECTOTCORR": Bias Corrected Total Precipitation
* "T2M": 2-meter Air Temperature
* "QV2M": 2-meter Specific Humidity
   
The most significant weather variables that affect people's trip experiences are precipitation, temperature, and humidity near Earth's surface. These variables also interact to impact trip experiences. For example, precipitation below zero degrees Celsius results in snow. So to keep this app lightweight, separate weather variables for rain and snow were not included. Furthermore, to support accurate long-term forecasting, wind speeds and other weather variables that fluctuate relatively hour-by-hour as opposed to day-to-day were not included in this app. Spatial resolution is approximately 50 km in the latitudinal direction for MERRA-2. However, temperature, humidity, and precipitation should generally be the same across this distance. The data sometimes includes '-999' values. These will all be converted to nulls before being analyzed. 

### Data Analysis and Visualization

Prophet, an automated additive model, was used to analyze the MERRA-2 data. This model accounts for non-linear trends using a piecewise linear model and accounts for seasonal cycles using a Fourier series that decomposes the cycle into a series of sine and cosine terms. This model is used to forecast future weather data 365 days into the future. This was visualized using Matplotlib on top of a grey-shaded area displaying the range of possible values that fall within a 95% interval. 

As long as the forecasted values on the trip's date don't move above or below the dashed lines that indicate the weather isn't ideal, users can be confident that they do not have to worry about the weather for their trip. 

The full historical weather data from 1980 to today for that location is also visualized. This historical data is decomposed to visualize the general trend without the fluctuations. It is also decomposed to visualize how seasonality impacts this location's weather. Specifically, how much the weather data fluctuates based on the day of the year. 


### Developer Guide

Developers can follow this guide to add more data products, update the dashed lines based on their ideal weather preferences, and make other customizations for their own use cases. 

1. Fork this repository.
<img width="143" alt="Screenshot 2025-04-30 at 11 45 18 AM" src="https://github.com/user-attachments/assets/77cba18e-1052-4355-948f-0adbb2a84ed9" />

2. Go to Streamlit Cloud and create an account or log-in: https://share.streamlit.io/
<img width="1482" alt="Screenshot 2025-04-30 at 11 12 28 AM" src="https://github.com/user-attachments/assets/ff1779ad-8490-4fe6-abaf-02a2adea8a6c" />

3. Click on "Create app" then "Deploy a public app from GitHub"
<img width="1522" alt="Screenshot 2025-04-30 at 11 42 14 AM" src="https://github.com/user-attachments/assets/615446ed-2694-4114-ade1-f994c449bf4a" />

<img width="1081" alt="Screenshot 2025-04-30 at 11 18 21 AM" src="https://github.com/user-attachments/assets/30b56274-92eb-4dcd-b5c4-332f0c3995fc" />

4. Select appropriate parameters before deploying.
<img width="869" height="724" alt="Screenshot 2025-10-04 at 3 10 21 PM" src="https://github.com/user-attachments/assets/e79c041c-8cc6-4f17-8411-8e47f37061f8" />

<img width="1045" height="712" alt="Screenshot 2025-10-04 at 10 50 06 AM" src="https://github.com/user-attachments/assets/292a007c-6319-4b32-b505-985e68aa9517" />

### User Guide
1. Open the Long-term Weather Forecasting App: https://longtermweatherforecastingapp987.streamlit.app/

2. Zoom in and select a location on a map. 
<img width="1213" alt="Screenshot 2025-04-29 at 9 19 48 PM" src="https://github.com/user-attachments/assets/5b106ef8-2626-4e37-b7d8-f4b8908ba868" />
<img width="740" alt="Screenshot 2025-04-30 at 11 54 03 AM" src="https://github.com/user-attachments/assets/d68e738d-c765-4495-b03c-2316c19a0164" />

3. View results.

5. Export data (Optional).


## NASA Data 
https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/

## Space Agency Partner and Other Data
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Prophet](https://facebook.github.io/prophet/)
* [Requests](https://pypi.org/project/requests/)
* [Folium](https://python-visualization.github.io/folium/latest/)
* [Streamlit](https://streamlit.io/)
* [Leaflet](https://leafletjs.com/)
* [OpenStreetMap](https://www.openstreetmap.org/about)
* [Certifi](https://pypi.org/project/certifi/)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [NASA POWER API](https://power.larc.nasa.gov/)
* [Excel](https://power.larc.nasa.gov/)
* [Pexels](https://www.pexels.com/)
