
def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print('==========================')
    print('What would you like to do?')
    for i in menu:
        print(i, '-', menu[i])
    print('==========================')

def get_written_date(date_list):
    """
    param: date_list(list of strings) - represents a date
    using digits to denote the month
    The function converts the date in the form
    month(in letters) date, year
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    
    monthnum = int(date_list[0])
    daynum = int(date_list[1])
    year = (date_list[2]) 
    month = (month_names[monthnum])
    return (f'{month} {daynum}, {year}')


def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() 
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that the provided index
    idx is a valid positive index that can retrieve
    an element from in_list. """

    if idx.isdigit():
        idx = int(idx)
        idx -= start_idx
        if idx >= 0 and idx < len(in_list):
            return True
    return False


def print_task(task, priority_map, name_only = False):
    """
    param: task (dict) - a dictionary object that is expected
            to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
    - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
            (displayed as a written-out date)
    - "done": a string representing whether a task is completed or not

    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed for the
            priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.

    returns: None; only prints the task values

    Helper functions:
    - get_written_date() to display the 'duedate' field
    """
    print(task['name'])
    if name_only != True:
        if task['info'] != '':
            print(f"  * {task['info']}")
        x = task['duedate'].split('/')
        print(f"  * Due: {get_written_date(x)}", end = '  ')
        print(f"(Priority: {priority_map[task['priority']]})")
        end = task['done']
        print(f"  * Completed? {end}")
        

def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-" * 42)
    for tasks in task_list: 
        if show_idx == True:
              print(f"{start_idx}.", end=" ")
              start_idx = start_idx+1
        if completed == "all":
            print_task(tasks, priority_map, name_only)
        elif tasks["done"] == completed:
            print_task(tasks, priority_map, name_only)


def delete_item(in_list, idx, start_idx = 0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.

    returns:
    If the input list is empty, return 0.
    If idx is not of type string or start_idx is not an int, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.

    Helper functions:
    - is_valid_index()
    """
    if not in_list:
        return 0

    elif (type(start_idx) != int) or (type(idx) != str):
        return None
   
    elif is_valid_index(idx, in_list, start_idx) == False:
        return -1
    else:
        idx = int(idx)-start_idx
        return in_list.pop(int(idx))



def is_valid_name(string):
    """
    param: str(user input)
    The function first checks if the input
    is of type string.
    If it is of type string,
    it then checks if the length is between 3 and 25 inclusive.
    
    Returns:
    False if not of type str or wrong not between 3 and 25 inclusive.
    True if of type str and between 3 and 25 inclusive.
    """
    if type(string) == str:
        if 3 <= len(string) <= 25:
            return True
        else:
            return False
    else:
        return False

def is_valid_month(date_list):
    """
    param: date_list(a list of 3 strings that represents a date
    in the form (month, day, year))
    The function first checks if the input
    is of type string.
    If it is of type string,
    it then checks if it is a digit.
    If it is a digit, it then checks if it
    is greater than 0 and less than or equal to 12
    
    Returns:
    False if not of type str or wrong not between 3 and 25 inclusive.
    True if of type str, a digit, and is greater than 0
    and less than or equal to 12
    """
    if type(date_list[0]) == str:
        if 1 <= int(date_list[0]) <= 12:
            return True
    else:
        return False

def is_valid_day(date_list):
    """
    param: date_list(a list of 3 strings that represents a date
    in the form (month, day, year))
    
    The function first checks if the input
    contains a valid month number(between 1 and 12 inclusive)
    It then checks if date_list[1] is of type str and a digit.
    It then checks if the day is less than or equal to the
    corresponding month's days

    Returns:
    False if date_list[0] isn't a valid month, or if date_list[1] isn't type str,
    or if date_list[1] isn't less than or equal to the corresponding month's days
    True if date_list[0] is a valid month, date_list[1] is type str, a digit,
    and less than or equal to the corresponding month's days

    Helper functions:
    is_valid_month()
    """

    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    days = 0
    if is_valid_month(date_list) == True:
        days = num_days[int(date_list[0])]
        if 0 < int(date_list[1]) <= days:
            return True
        else:
            return False

def is_valid_year(date_list):
    """
    param: date_list(a list of 3 strings that represents a date
    in the form (month, day, year))
    The function checks if the input
    is of type string and if it is greater than 1000
    
    Returns:
    False if either conditions of the if statement returns false
    True if both conditions of the if statement returns true
    """
    if type(date_list[2]) == str:
        if int(date_list[2]) > 1000:
            return True
        else:
            return False

def is_valid_date(date_list):
    """
    param: date_list(a list of 3 strings that represents a date
    in the form (month, day, year))
    the function checks if is_valid_year(date), is_valid_day(date),
    is_valid_month(date) all return true
    
    returns:
    True if all helper functions return true
    False if any of them return false

    Helper functions:
    is_valid_year()
    is_valid_day()
    is_valid_month()
    """
    if (is_valid_year(date_list) == True) and (is_valid_day(date_list) == True) and (is_valid_month(date_list) == True):
        return True
    else:
        return False


def is_valid_priority(string, dictionary):
    """
    param: string, dictionary
    The function first check if string is of type str
    or if dictionary is of type dict.
    If both true, it then checks if the integer value of
    string ia a key in dictionary.

    returns:
    True if string is type str and contains 'yes' or 'no'
    False if either string isn't type str or dictionary isn't type dict
    Also if the integer value of string isn't a key in dictionary
    """
    
    if type(string) != str or type(dictionary) != dict:
        return False
    else:
        if string.isdigit() == True:
            if int(string) in dictionary.keys():
                return True
        else:
            return False

def is_valid_completion(string):
    """
    param: string(user input)
    The function first check if string is of type str.
    If true, it then checks if the string contains 'yes' or 'no'

    returns:
    True if string is type str and contains 'yes' or 'no'
    False if either string isn't type str or doesn't contain 'yes' or 'no'
    """
    if type(string) == str:
        if 'yes' in string or 'no' in string:
            return True
        else:
            return False
    else:
        return False

def get_new_task(cats, dictionary):
    """
    param: cats (a list of strings)
    param: dictionary(contains mapping between the keys to categories)
    The functions first checks if there are 5 strings in cats
    It then checks if any of them aren't type str
    It then checks is_valid_completion(cats[4]), is_valid_name(cats[0]),
    is_valid_priority(cats[2], dictionary), and is_valid_date(cats[3]).
    If they all return true, a new dictionary is created where
    the five strings in cats are matched with the corresponding
    keys, name, infor, priority, duedate, done

    Returns:
    If there aren't five strings in cats,
    the number of strings is returned
    If any of the helper functions return False,
    a tuple with the correspnding type and value is returned
    
    helper functions:
    is_valid_completion()
    is_valid_name()
    is_valid_priority()
    is_valid_date()
    
    """
    if len(cats) != 5:
        return len(cats)
    for value in cats:
        if type(value) != str:
            return (type(value), value)
    if len(cats) == 5:
        if is_valid_name(cats[0]) == False:
            return ('name', cats[0])
        if is_valid_priority(cats[2], dictionary) == False:
            return ('priority', cats[2])
        if is_valid_date(cats[3]) == False:
            return ('duedate', cats[3])
        if is_valid_completion(cats[4]) == False:
            return ('done', cats[4])
        else:
            dic = {}
            dic['name'] = str(cats[0])
            dic['info'] = str(cats[1])
            dic['priority'] = int(cats[2])
            dic['duedate'] = str(cats[3])
            dic['done'] = str(cats[4])
            return dic

def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an 
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    if str(idx).isdigit():
        idx = int(idx)
        idx -= start_idx
        if idx >= 0 and idx < len(in_list):
            return True
    return False


def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    new_idx = int(idx) - start_idx
    if info_list == []:
        return 0
    elif is_valid_index(idx, info_list) == False:
        return -1
   
    if field_key == "name":
        if is_valid_name(field_info) == True:
            task = info_list[new_idx]
            task[field_key] = field_info
            info_list[new_idx] = task
            return info_list[new_idx]
        else:
            if is_valid_name(field_info) == False:
                return field_key
         
    elif field_key == "info":
         task = info_list[new_idx]
         task[field_key] = field_info
         info_list[new_idx] = task
         return info_list[new_idx]
      
    elif field_key == "priority":
        if is_valid_priority(field_info, priority_map) == True:
            task = info_list[new_idx]
            task[field_key] = field_info
            info_list[new_idx] = task
            return info_list[new_idx]
        else:
            return field_key
      
    elif field_key == "duedate":
        if is_valid_date(field_info) == True:
            task = info_list[new_idx]
            task[field_key] = field_info
            info_list[new_idx] = task
            return info_list[new_idx]
        else:
            if is_valid_date(field_info) == False:
                return field_key
      
    elif field_key == "done":
        if is_valid_completion(field_info) == True:
            task = info_list[new_idx]
            task[field_key] = field_info
            info_list[new_idx] = task
            return info_list[new_idx]
        else:
            if is_valid_completion(field_info) == False:
                return field_key
    else:
        return -2
        

def load_tasks_from_csv(filename, in_list, priority_map):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_list (list) - A list of task dictionary objects to which
            the tasks read from the provided filename are appended.
            If in_list is not empty, the existing tasks are not dropped.
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed by the helper function.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new task using the `get_new_task()` function.
    - If the function `get_new_task()` returns a valid task object,
    it gets appended to the end of the `in_list`.
    - If the `get_new_task()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid task data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_task().

    Helper functions:
    - get_new_task()
    """
    import csv
    import os
    if filename[-4:] != '.csv':
        return -1
    if not os.path.isfile(filename):
        return None
    new = []
    with open(filename, 'r') as csvfile:
        csv = csv.reader(csvfile, delimiter = ',')
        num = 1
        for row in csv:
            task = get_new_task(row, priority_map)
            if type(task) != dict:
                new.append(num)
            else:
                in_list.append(task)
            num += 1
    return new
    

def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """

    import csv
    if filename[-4:] == '.csv':
        with open(filename,'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            new = []
            for task in tasks_list:
                new.append(task)
                csv.writer(new)
    else:
        return -1
