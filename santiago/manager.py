import santiago

class DoManager(object):
    def __init__(self, client_id, api_key):
        self.api_key=api_key
    def __getattr__(self, name):
        if hasattr(santiago, name) and hasattr(getattr(santiago, name), "__call__"):
            return lambda *args, **kwargs: getattr(santiago, name)(api_key=self.api_key, *args, **kwargs)
        else:
            raise AttributeError
