from django.apps import AppConfig

class TodoappConfig(AppConfig):
    name = 'todoapp'

    def ready(self) -> None:
        import todoapp.signals
        
        
