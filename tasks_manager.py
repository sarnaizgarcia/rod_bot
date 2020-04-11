from datetime import date

from planning import homework_planning


def get_daily_tasks():
    """ Creates a list with the subjects to work in a day

    Returns
    -------
    list
        A list of the subjects to work the current day

    """
    today = str(date.today())
    daily_tasks = list()
    for x in homework_planning.get(today):
        if homework_planning.get(today).get(x).get('done') == False:
            daily_tasks.append(x)
    return daily_tasks


def get_task_data(key, subject):
    """ Gets a the value from the key of a task of a certain subject

    Parameters
    ----------
    key: str
        The key whose value we want to get

    subject: str
        One of the existing subjects

    Returns
    -------
    str
        A string with the data required
    """
    today = str(date.today())
    task_data = homework_planning.get(
        today).get(subject).get(key)
    return task_data


def remove_subject(daily_tasks, subject):
    """ Removes a subject from a list of subjects

    Parameters
    ----------
    list
        A list of subjects
    str
        Subject to remove

    Returns
    -------
    list
        A list with the subject removed
    """
    # TODO: Hay que cambiar el estado de la tarea y renombrar las funciones

    daily_tasks.remove(subject)
    return daily_tasks


def modify_task_state():
    """ Changes the 'done' key of a task from False to True

    Parameters
    ----------
    ???

    Returns
    -------
    ???
    """
    pass
