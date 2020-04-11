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


def remove_subject(daily_tasks, subject):
    """ Removes a subject from the list of subjects

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

