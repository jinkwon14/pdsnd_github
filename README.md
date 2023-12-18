
### Author: Jin Kwon 
### Date Created: 2023-12-18 

### US Bikeshare Data Analysis (project URL: [Udacity Proamming for Data Science in Python](https://learn.udacity.com/nanodegrees/nd104))

### Description
This project is designed to explore and analyze bikeshare data from three major cities in the United States: Chicago, New York City, and Washington. The Python script allows users to filter the data by city, month, and day of the week to uncover various statistics. It provides insights into travel times, station popularity, user demographics, and other aspects of bikeshare usage. The script employs Pandas and NumPy libraries for data manipulation and analysis.

### Files Used
- `bikeshare.py` (Main Python script)
- `chicago.csv` (Data for Chicago, excluded in `.gitignore`)
- `new_york_city.csv` (Data for New York City, excluded in `.gitignore`)
- `washington.csv` (Data for Washington, excluded in `.gitignore`)

### Features
The script includes the following functions:
- `get_filters()` - Asks the user to specify a city, month, and day to analyze.
- `load_data()` - Loads data for the specified city and filters by month and day if applicable.
- `time_stats()`, `station_stats()`, `trip_duration_stats()`, `user_stats()` - Functions to calculate and display statistics on the most frequent times of travel, popular stations, trip duration, and user information respectively.
- `convert()` - Helper function to convert seconds into a more readable duration format.
- `display_sample_data()` - Displays sample data upon user request.

### How to Run
Ensure you have Python 3.x installed along with Pandas and NumPy libraries. Run the script in a terminal or command prompt and follow the interactive prompts to analyze the bikeshare data.
```sh
# in terminal of your choice
python bikeshare.py
```

### Credits
This project was inspired by Udacity's Programming for Data Science with Python Nanodegree. Additional references and resources used in the development of this project include:
- Pandas Documentation: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
- NumPy Documentation: [https://numpy.org/doc/](https://numpy.org/doc/)
- Python Official Documentation: [https://docs.python.org/3/](https://docs.python.org/3/)