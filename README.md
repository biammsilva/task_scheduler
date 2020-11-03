# Task Scheduler

# Build and up application:
    docker-compose up

# Creating a super user:
    docker-compose run web python manage.py createsuperuser

# Schedule a single task:
* Go to http://localhost:8000/admin/django_celery_beat/periodictask/add/
* Set a:
    * Name;
    * Task;
    * Clocked schedule with the chosen date and the time;
    * Set the flag One-off-task;
    * In the "Arguments" section, set in "Keyword Arguments": {"url": "http://your-url.com"}

## Used resources:
* Python 3.8;
* Django with django admin to view and manage schedules;
* Celery for schedule tasks;
* Radis for caching;
* PostgreSql for storaging;

## Tests:

I hadn't time to write the tests, but if I had, I would use this examples bellow:

https://docs.celeryproject.org/en/stable/userguide/testing.html