### Create your models:

    ## Requirements
        -Tasks:
            - content
            - creation_date
            - deadline
            - satatus
            - completed_on

        -Task_List
            - name
            - contains ids of tasks


### Task Table

id | content | creation_date | deadline | task_list_id | status | completed_on

### Task_list

id | name | created_at

- makemigrations -> It creates a script in respect of the changes made to models.py (sql)
- migrate -> It runs this script

### How to work on database models?
- Queryset from pythons(refer documentation)
- python3 manage.py shell
- from trello_app.models import *
## creating object
    task_list_1 = TaskList(name="College")
    task_list.name
    task_list_1.save()