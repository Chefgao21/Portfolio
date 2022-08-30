from task_functions import *


assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'


assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('2', ["Quizzes", 25.5], 1) == True 
assert is_valid_index('Z', ["Quizze", 100], '1') == False


assert delete_item([], 1, 1) == 0
assert delete_item([1], '-2') == -1
assert delete_item([1, 2, 3], '2') == 3



the_menu = {
    "L" : "List",
    "A" : "Add",
    "U" : "Update",
    "D" : "Delete",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
}

all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022', 
        "done": 'no'
    }

]

list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}


priority_scale = {11: "The one and only"}
assert is_valid_priority('11', priority_scale) == True
assert is_valid_priority(11, priority_scale) == False

assert is_valid_completion('two toys') == False
assert is_valid_completion('one') == False
assert is_valid_completion('two toys yes') == True

assert load_tasks_from_csv(".cse", [], priority_scale) == -1
assert load_tasks_from_csv("space", [], priority_scale) == -1
assert load_tasks_from_csv("csv", [], priority_scale) == -1.

assert is_valid_name('bo') == False
assert is_valid_name('boo') == True

assert is_valid_date(["21", "01", "1970"]) == False
assert is_valid_date(["-2", "31", "2021"]) == False
assert is_valid_date(["1", "10", "2021"]) == True

assert is_valid_year(["1", "10", "2021"]) == True
assert is_valid_year(["1", "10", "900"]) == False

assert update_task(all_tasks, -1, 0, 1, 0, start_idx = 0) == -1
assert update_task([], 0, 'space', 1, 0, start_idx = 0) == 0


assert save_tasks_to_csv([],'.cse') == -1
assert save_tasks_to_csv([],'.space') == -1
assert save_tasks_to_csv([],'noise') == -1





