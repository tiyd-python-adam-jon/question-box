# get**answers**

### A Website to Source Answers to Your Burning Questions

* Website location: **`https://boiling-savannah-6958.herokuapp.com/`**
* Local deployment location: `localhost:[PORT]/` where `[PORT]` is usually `5000` for heroku local and `8000` for Django

## About This Site

### Homepage / All Questions
Located at `host/` and also `host/questions/`, where `host` is the location of the server (usually `localhost:8000` if using Django's `runserver`; `https://boiling-savannah-6958.herokuapp.com/` if accessing on the web). Shows all questions on the site, arranged to show newest questions at the top.

### Question Pages
Located at `host/questions/[question_id]/`, where [question_id] is the numerical id of a question. Shows the question, all provided answers, and an answer form to submit your own answer.

### To Ask or Answer, You Must Be Logged In
There are benefits of creating an account beyond being able to ask and answer questions—as you interact with the site, you will accrue points for your actions:
 * Asking a question gives you 5 points
 * If your answer is upvoted, you will get 10 points
 * If your answer is downvoted, you will lose 5 points
 * If you downvote another's answer, you will lose 1 point (to discourage trolling)

### Question Form
Located at `host/questions/form`. This is where you post new questions for people to answer.

### Login, Logout, Registration
Located in the navbar at the top of every page; login and registration links show only if not already logged in; logout shows only if logged in.


<!--
### Profile Pages
Located at `host/profiles/[profile_id]`, where `profile_id` is the numerical id of the profile. These are more easily accessed through the interface by clicking on a person's name or, for logged in users, view their own page by clicking on their name on the navbar.
-->

### System Requirements

* To run locally, you will need to have **Python&nbsp;3** installed on your machine. See [Python's site](https://www.python.org/) for details.

* Clone this repo onto your computer; the below assumes you have kept the default folder name as `question-box`.

* You will need to make sure that you have a virtual environment running Python&nbsp;3 in the folder that you made in the above step. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* Using your favorite command line program (e.g., Terminal on Mac&nbsp;OS&nbsp;X), install the requirements file in your virtual environment: `pip install -r requirements.txt`.

* This app is set up to run on PostgreSQL. It is set it up to have a local (development) database named `questionbox` with a user of `questionbox` and a password of `password`. The database name, user, and password can all be configured to your preferences in the `question-box/questionbox/questionbox/settings.py` file. If you do not have PostgreSQL on your machine, [follow these instructions](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).

* **Running the site with Django** requires more command line. Navigate to `question-box/questionbox` and enter `python manage.py runserver` This will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.

* **Running the site with your own heroku local/web** requires that you have your machine set up with [heroku and heroku toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [create a heroku account](https://signup.heroku.com/).
 * Once you have these installed and have a heroku account, navigate to the `question-box` directory and run the following commands:
 ```
 $ heroku create
 $ heroku config:set DJANGO_SETTINGS_MODULE=questionbox.heroku_settings
 $ heroku config:set PYTHONPATH=questionbox
 $ heroku config:set SECRET_KEY=`python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(50)]))'`
 ```

 * Now, create a new file in the `question-box` directory called `.env` with the following contents where `[your_secret_key]` is replaced with the secret key used in your own heroku server from the previous step:
 ```
 DATABASE_URL=postgres:///questionbox
 DJANGO_SETTINGS_MODULE=questionbox.heroku_settings
 PYTHONPATH=questionbox
 SECRET_KEY=[your_secret_key]
 ```

 * Next, navigate to the `question-box` directory and run the following commands to first, collect the static files (e.g., css files), and then deploy heroku locally (usually located at `localhost:5000`). Again, this will take over the current command-line program's window until you stop the server. Kill the process by pressing `Ctrl+C` or quitting the command-line program entirely.
 ```
 $ python questionbox/manage.py collectstatic
 $ heroku local web
 ```

 * Once this is working, you can deploy and then view online by running the following:
 ```
 $ git push heroku master
 $ heroku ps:scale web=1
 $ heroku run questionbox/manage.py migrate
 $ heroku open
 ```
