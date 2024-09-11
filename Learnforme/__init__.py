# apps.py
from django.apps import AppConfig

class LearnformeConfig(AppConfig):
    name = 'Learnforme'

    def ready(self):
        import Learnforme.signals