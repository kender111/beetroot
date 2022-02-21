# p = 'pending'
# i = 'in progress'
# d = 'done'
import time

count_id = 0

def create_new_task():
    user_title = input('Enter task title: ')
    user_description = input('Please enter description for current task (optional): ')
    user_priority = int(input('Enter priority number from 1 to 10: '))
    # user_status = input('Enter status of the current task (pending - p, in progress - i, done - d): ')
    while True:
        user_due_date = input('Enter due_date DD.MM.YYYY: ')
        try:
            valid_date = time.strptime(user_due_date, '%m.%d.%Y')
            break
        except ValueError:
            print('Invalid date! Please, enter correct due date DD.MM.YYYY')
    new_task = {'id': count_id + 1, 'title': user_title, 'description': user_description,
                'priority': user_priority, 'status': 'pending',
                'due_date': user_due_date}
    # print(new_task)
    return new_task
