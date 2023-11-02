### Date created
1st November, 2023

### Project Title
Explore US Bikeshare Data

### Description
**Bike Share Data**

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I used data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington DC.

**The Datasets**

All three of the data files contain the same core six (6) columns:

-Start Time (e.g., 2017-01-01 00:07:57)
-End Time (e.g., 2017-01-01 00:20:53)
-Trip Duration (in seconds - e.g., 776)
-Start Station (e.g., Broadway & Barry Ave)
-End Station (e.g., Sedgwick St & North Ave)
-User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

-Gender
-Birth Year

### Files used
-chicago.csv
-new_york_city.csv
-washington.csv

### Credits
-Udacity Introduction to Python Programming course notes and videos

-https://stackoverflow.com/questions/51603690/extract-day-and-month-from-a-datetime-object

-https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month.html

-https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html

-https://stackoverflow.com/questions/36341484/get-day-name-from-weekday-int

-https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.hour.html

-https://github.com/juliaobenauer/us-bikeshare-data-project/blob/master/bikeshare_2.py

-https://github.com/khaledimad/Explore-US-Bikeshare-Data/blob/master/bikeshare_2.py

