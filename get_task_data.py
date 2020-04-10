from datetime import date

from planning import homework_planning


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
