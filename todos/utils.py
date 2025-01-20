def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None

def search_id(search_id, lists):
    for lst in lists:
        if lst['id'] == search_id:
            return lst
    return None

def error_for_todo(todo):
    if not 1 <= len(todo)<= 100:
        return "The title must be between 1 and 100 characters"
    else: 
        return None

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item['title'].lower())
    incomplete_items = [item for item in sorted_items if not select_completed(item)]
    complete_items = [item for item in sorted_items if select_completed(item)]

    return incomplete_items + complete_items