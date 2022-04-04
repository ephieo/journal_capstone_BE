# JOURNAL APP

### Backend Repo:

https://github.com/ephieo/journal_capstone_BE

### How to run :

Clone repo locally :

- `git clone https://github.com/ephieo/journal_capstone_BE.git`
- `cd journal_capstone_BE/`

Set up requirements :

- `pip install -r requirements.txt`
- `python3 manage.py runserver`

You can view the api view via the links below :

#### Make sure the server is running

- http://127.0.0.1:8000/posts/
- http://127.0.0.1:8000/quotes/

### Versions :

- Python 3.9.10
- Django 3.0.5
- graphene 2.1.8

- How to install python :
  https://realpython.com/installing-python/

### Accessing Django administration GUI :

- Make sure the server is running

- access this site : http://127.0.0.1:8000/admin/journal_app/posts/

* Login : journal
* Password : capstone

### Test Query examples using Insomnia :

Run this POST GraphQL query :

`mutation { addPost(title:"hiiiiiii",content:"byyyyyye"){ post{title,content} } }`

via this url :

- http://127.0.0.1:8000/graphql

Run this GET GraphQL query :

`query{allPosts{ id content date }}`

via this url :

- http://127.0.0.1:8000/posts/

### Project Description :

#### Requirements

Build a full-stack journaling application with a twist.

- A user can add and delete multiple entries a day;
- A user can view the saved entries (the entries should be saved to a database);
- A user can view the quote of the day from an API of your choice above the entries;
- A user can save the quote of the day
- A user can view the saved quotes of the day.

In a technology of your choice, please prepare and present the UI design ideas (wireframes) to
the client on Slack, apply it according to their feedback.
The app should work locally, don’t deploy it.
The client has strict budgeting rules and the crafters can’t bill for additional features that weren’t
listed in the requirements above. Please fill the timesheet with the tasks that you’ve completed
as you progress through.
If in doubt about the scope of the project, reach out to the client on Slack.

#### Stack

- Python backend
- GraphQL
- React frontend

The remaining stack is at your discretion. Pick the web framework, GraphQL support (if needed)
and database technology. Feel free to use any additional libraries eg. components libraries.

### Developr - Ephrathah Oyedoh
