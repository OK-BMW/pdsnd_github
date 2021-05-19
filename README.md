[comment]: <> (>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.)

### Date Created
* README.md: 18.05.2021
* Git repo (remote): 18.05.2021
* Git repo (local): 18.05.2021

### Analysis of US Bikeshare Data
The project provides an interactive Python script which allows a basic analysis of US Bikshare data.

### Description

#### About Bikeshare Project
Cyclehop - a private bike share company - offers a bike-sharing system ([bikeshare.com](https://www.bikeshare.com/)).
Their bikes provides data from every ride (date, start time, end time, start location, end location, anonymized user information).
Data obtained from various cities can be downloaded and analysed ([bikeshare.com/data](https://www.bikeshare.com/data/)).
These data are analysed in this project.

#### Interactive Python Script
Python is used to analyse bikeshare data.
Here, most common day, most common start and end station, trip duration and other key measurements are computed. 
A list of the computed measurements is given below.
The computations are done within a script. In addition, the script interacts with the user through the commnand line. The user can select the city of interest, the month of interest and day of week of interest.
The script has been tested using data sets obtaiend from New York City, Washington and Chicago.
The script has been written using Anaconda/Spyder for Python. Further developments should be done using Anaconda/Spyder for Python. 

#### Measurements:
* Date and location:
 * Most common month
 * Most common day of week
 * Most common start hour
 * Most common start station
 * Most common end station
 * Most common trip
* Travel time:
 * Total travel time
 * Mean travel time
* User infromation:
 * Counts of user types
 * Counts of gender
 * User birth information: Earliest birth
 * User birth information: Most recent birth
 * User birth information: Most common birth

#### About Python Script
Follwoing python libraries are used:
* time
* pandas
* numpy

The script contains the following functions:
* Function "Get Filters from User": get_filters()
* Function "Load Data": load_data(city, month, day)
* Function "Display Data": display_data(df)
* Function "Most Common": most_common(dfc, name)
* Function "Time Statstics": time_stats(df)
* Function "Travel Statstics": station_stats(df):
* Function "User Statstics": user_stats(df):
* Function "Main Program": main():

#### Backlog: 
* [#0001]: Test Python script on data sets obtained from other cities then test data sets
* [#0002]: Add graphs as output from Python script
* [#0003]: Create a GUI (instead of command line interaction)

#### How do I contribute?
You would like to help me writing audits, fixing bugs, improving and adding measurements and making the script more useful! I would love it to get in contact with you on GitHub.
Here is the guidline:

1. Fork my GitHub repository https://github.com/OK-BMW/pdsnd_github.git
1. Clone your (forked) repository to your computer
1. Create a branch with the name improvement-"function name" (i.e. improvement-get_filters) or the name new-function-"function_name" (i.e. new-function-make_boxplots)
1. Switch to the branch and maker your improvements or create a new function (Here, I strongly recommend that you use Anaconda/Spyder)
1. Test carefully your improvement or new function without violating the entire script sequence
1. Send me a pull request

Further details regarding contributing will follow.

### Files Used
The follwoing files are traked by version control:
* README.md
* .gitignore
* bikeshare.py

### Credits

#### Git and GitHub
* Get Git on your computer: https://git-scm.com/downloads
* My remote repo on GitHub (forked from original repo): https://github.com/OK-BMW/pdsnd_github.git
* Original remote repo on GitHub: https://github.com/udacity/pdsnd_github.git

#### Python and Anaconda
* Get Python on your computer: https://www.python.org/downloads/
* Get Python/Anaconda on your computer (recommended): https://www.anaconda.com/products/individual

#### Bikeshare Project
* About: https://www.bikeshare.com/
* Data: https://www.bikeshare.com/data/

#### Usefull Links
* Preview of Markdown code: https://markdownlivepreview.com/
* Generate a bashrc file: http://bashrcgenerator.com/
* Git commit styleguide: https://udacity.github.io/git-styleguide/
