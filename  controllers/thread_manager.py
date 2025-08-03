
import threading

def run_in_thread(target, *args, **kwargs):
    """Run a target function in a separate thread."""
    thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=True)
    thread.start()
    return thread