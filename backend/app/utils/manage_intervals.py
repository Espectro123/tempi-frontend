import datetime
from app.utils.control_tk2000 import control_tk
from app.repositories.in_memory_experiment import InMemoryExperiment

def manage_interval_change(current_temperature):

    current_time = datetime.datetime.now().timestamp()

    temperature_interval_change = round((InMemoryExperiment.target_temperature - InMemoryExperiment.initial_temperature)/InMemoryExperiment.interval,1)

    if(current_time - InMemoryExperiment.last_interval_change >= 3600):
        
        # We have to change intervals
        if(InMemoryExperiment.interval_count >= InMemoryExperiment.interval):

            if InMemoryExperiment.interval_status == "heat":
                InMemoryExperiment.interval_status = "cool"
            else:
                InMemoryExperiment.interval_status = "heat"

        # We decreased or increased the temperature
        if InMemoryExperiment.interval_status == "heat":
            control_tk("SetUpTemperature", current_temperature, current_temperature+temperature_interval_change)
        else:
            control_tk("SetUpTemperature", current_temperature-temperature_interval_change, current_temperature)

        InMemoryExperiment.interval_count = InMemoryExperiment.interval_count+1
        InMemoryExperiment.last_interval_change+6
    
    
    
