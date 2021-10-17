from typing import List
from h2o_wave import Q, main, app, ui

_id = 0

# A simple class that represents a to-do item.
class TodoItem:
    def __init__(self, text):
        global _id
        _id += 1
        self.id = f'todo_{_id}'
        self.text = text
        self.done = False


@app('/todo', mode='multicast')
async def serve(q: Q):
    if q.args.new_todo:  # Display an input form.
        new_todo(q)
    elif q.args.add_todo:
        add_todo(q)
    else:  # Show all items.
        show_todos(q)
    await q.page.save()


def show_todos(q: Q):
    # Get items for this user.
    todos: List[TodoItem] = q.user.todos

    # Create a sample list if we don't have any.
    if todos is None:
        q.user.todos = todos = [TodoItem('Do this'), TodoItem('Do that'), TodoItem('Do something else')]

    # If the user checked/unchecked an item, update our list.
    for todo in todos:
        if todo.id in q.args:
            todo.done = q.args[todo.id]

    # Create done/not-done checkboxes.
    done = [ui.checkbox(name=todo.id, label=todo.text, value=True, trigger=True) for todo in todos if todo.done]
    not_done = [ui.checkbox(name=todo.id, label=todo.text, trigger=True) for todo in todos if not todo.done]

    # Display list
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('To Do'),
        ui.button(name='new_todo', label='New To Do...', primary=True),
        *not_done,
        *([ui.separator('Done')] if len(done) else []),
        *done,
    ])


def add_todo(q: Q):
    # Insert a new item
    q.user.todos.insert(0, TodoItem(q.args.text or 'Untitled'))

    # Go back to our list.
    show_todos(q)


def new_todo(q: Q):
    # Display an input form
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('New To Do'),
        ui.textbox(name='text', label='What needs to be done?', multiline=True),
        ui.buttons([
            ui.button(name='add_todo', label='Add', primary=True),
            ui.button(name='show_todos', label='Back'),
        ]),
    ])