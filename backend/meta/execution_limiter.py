import time

def run_with_timeout(func, args=(), kwargs=None, timeout_sec=2.0):
    """
    Run a function with a time limit. Returns None if it times out.

    Args:
        func (callable): Function to run.
        args (tuple): Positional args for func.
        kwargs (dict): Keyword args for func.
        timeout_sec (float): Max allowed execution time.

    Returns:
        Any or None: Result if completed, or None if timeout occurred.
    """
    import threading

    result = [None]
    kwargs = kwargs or {}

    def wrapper():
        result[0] = func(*args, **kwargs)

    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout=timeout_sec)

    if thread.is_alive():
        return None
    return result[0]
