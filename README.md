# get**answers**

### A Website to Source Answers to Your Burning Questions

* `https://boiling-savannah-6958.herokuapp.com/` homepage on web
* `localhost/` homepage in local deployment

### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [Python's site](https://www.python.org/) for details.

* Copy this repo to your computer; the below assumes you have kept the default folder name as `question-box`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* This app is set up to run on PostgreSQL. It is set it up to have a local (development) database named `questionbox` with a user of `questionbox` and a password of `password`. The database name, user, and password can all be configured to your preferences in the `question-box/questionbox/questionbox/settings.py` file. If you do not have PostgreSQL on your machine, follow [these instructions](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).

* **Running the site** requires more command line. Navigate to `question-box/questionbox` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

## About This Site

### Homepage / Questions
Located at `host/` and also `host/questions`, where `host` is the location of your server (usually `localhost:8000` if using Django's `runserver`). Shows all questions on the site, arranged to show newest questions at the top.

### Question Pages
Located at `host/questions/[question_id]`, where `host` is the location of your Django server. Shows all worms created/modified on the site within the last 30 days, arranged by number of clicks.


### Most Popular Worms – All-Time
Located at `localhost/popall`, where `localhost` is the location of your Django server. Shows all worms on the site, arranged by number of clicks.

### Most Popular Birds – All-Time
Located at `localhost/popbirds`, where `localhost` is the location of your Django server. Shows all birds on the site, arranged by number of clicks over their entire worm collection.


### Bird Pages
Users on this site are referred to as "birds." Located at `localhost/birds/bird_id`, where `localhost` is the location of your django server and `bird_id` is the user_id. These are more easily accessed through the interface by logging in (to see your own bird page) or by clicking on another bird's name.

Logged in birds can see:

 * All of their worms, arranged by creation/modified date.

 * The popularity of the worms created/modified within the last 30 days.


### Worm Pages
Located at `localhost/worms/worm_id`, where `localhost` is the location of your Django server and `worm_id` is the number associated with that worm. These are more easily accessed through the interface by clicking on the info buttons throughout the site.
