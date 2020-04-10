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
        daily_tasks.append(x)
    return daily_tasks

