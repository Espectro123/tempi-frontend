import datetime

class InMemoryExperiment:

    experiment_duration = 0
    initial_temperature = 0.0
    target_temperature = 0.0

    last_interval_change = 0.0
    interval = 0
    interval_count = 0
    interval_status = ""

    first_check = True

    @classmethod
    def first(cls):
        cls.last_interval_change = datetime.datetime.now().timestamp()+9999
        
        if cls.initial_temperature > cls.target_temperature:
            cls.interval_status = "cool"
        else:
            cls.interval_status = "heat"
        
        cls.first_check = False
