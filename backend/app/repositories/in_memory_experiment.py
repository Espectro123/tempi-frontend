import datetime
from app.utils.read_temperature import read_temperature
from app.utils.control_tk2000 import turn_down_tk2000, set_temperature

class InMemoryExperiment:

    # Temperature at which the experiment start
    initial_temperature = 0.0
    
    # Max temperature the experiment will reach. 
    target_temperature = 0.0
    
    # Current temperature set on the machine
    current_temperature = 0.0
    
    # The duration of the experiment
    experiment_duration = 0
    
    # Experiment start time
    experiment_start = 0
    
    # The time at which the experiment started
    interval_start_time = 0
    
    # How many hours the change interval will alst
    interval_duration = 0
    
    # Current interval of the experiment
    interval_count = 1
    
    # Clicks per interval
    clicks_per_interval = 0
    
    # Click interval. How much time between clicks
    clicks_interval = 0
    
    time_of_last_click = 0
    
    # After the start, we need to reach the initial temperature before starting the experiment
    experiment_ready = False
    
    # Determinate if the experiment have finish or not
    experiment_finish = False

    @classmethod
    def set_up_experiment(cls,experiment_duration, initial_temperature, target_temperature,interval):
        cls.experiment_duration = experiment_duration
        cls.initial_temperature = initial_temperature
        cls.target_temperature = target_temperature
        cls.current_temperature = initial_temperature
        cls.interval_duration = interval
        
        if cls.initial_temperature > cls.target_temperature:
            cls.clicks_per_interval = round(((cls.initial_temperature - cls.target_temperature)*2),1)
        else:
            cls.clicks_per_interval = round(((cls.target_temperature - cls.initial_temperature)*2),1)
        
        cls.clicks_interval = round(((cls.interval_duration*60)/cls.clicks_per_interval),1)
    
    @classmethod
    def is_experiment_ready(cls):
        if cls.experiment_ready == False:
            temperature = read_temperature(1)
            print("The water temperature is: ", temperature)

            #If we are cooling
            if temperature < cls.initial_temperature:
                print("We are heating the water.... wait for a bit")
                if temperature + 0.6 >= cls.initial_temperature:
                    print("EXPERIMENT READY")
                    cls.experiment_ready = True
                    cls.interval_start_time = datetime.datetime.now().timestamp()
                    cls.experiment_start = datetime.datetime.now().timestamp()
                        
            #If we are heating
            if temperature > cls.initial_temperature:
                print("We are cooling the water.... wait for a bit")
                if temperature - 0.6 <= cls.initial_temperature:
                    print("EXPERIMENT READY")
                    cls.experiment_ready = True
                    cls.interval_start_time = datetime.datetime.now().timestamp()
                    cls.experiment_start = datetime.datetime.now().timestamp()     
            
        return cls.experiment_ready
    
    
    @classmethod
    def update_interval_count(cls):
        
        cls.interval_count = cls.interval_count + 1
        print("Interval count: ", cls.interval_count)
        
        aux = cls.initial_temperature
        cls.initial_temperature = cls.target_temperature
        cls.target_temperature = aux
        print("Initial temperature: ", cls.initial_temperature)
        print("Target temperature: ", cls.target_temperature)
        cls.time_of_last_click = datetime.datetime.now().timestamp()
        # The experiment must end
        if cls.interval_count > round(cls.experiment_duration/cls.interval_duration,1):
            turn_down_tk2000()
            cls.experiment_finish = True
    
    @classmethod
    def control_intervals(cls):
        
        # Current temperature of the water
        current_water_temperature = int(read_temperature(1))
        print("Current water_temperature: ", current_water_temperature)
        
        # Current time
        current_time = datetime.datetime.now().timestamp()
        print("Current time: ", current_time)
        
        # Time difference in minutes
        time_difference = round((current_time - cls.experiment_start)/60,1)
        time_difference_in_hours = round(time_difference/60,2)
        print("Time difference: ", time_difference , " Time difference_in_hours: ", time_difference_in_hours)
        
        # If true, experiment finish, turn down mahcine
        if time_difference_in_hours >= cls.experiment_duration:
            turn_down_tk2000()
            cls.experiment_finish = True


        if cls.experiment_finish != True and cls.time_of_last_click != 0:
            
            # Time difference for clciks
            time_difference_clicks = round((current_time - cls.time_of_last_click)/60,1)
            print("Time difference clicks: ", time_difference_clicks)
            
            # If true, we need to start a new interval
            print("More math: ", time_difference_in_hours/cls.interval_duration)
            if time_difference_in_hours/cls.interval_duration > cls.interval_count:
                print("We need to start a new interval!!!!")
                cls.update_interval_count()
                cls.current_temperature = cls.initial_temperature
                
            elif time_difference_clicks >= cls.clicks_interval:
                # We need to do another tick
                print("We need to do anothir click!!!")
                if cls.initial_temperature > cls.target_temperature:
                    # We are cooling the water
                    set_temperature(cls.current_temperature,cls.current_temperature-0.5)
                    cls.current_temperature = cls.current_temperature-0.5
                    print("Current temperature: ", cls.current_temperature)
                    cls.time_of_last_click = datetime.datetime.now().timestamp()
                    print("New time for last click: ", cls.time_of_last_click)
                    
                elif cls.initial_temperature < cls.target_temperature:
                    # We are heating the water
                    set_temperature(cls.current_temperature, cls.current_temperature+0.5)
                    cls.current_temperature = cls.current_temperature+0.5
                    print("Current temperature: ", cls.current_temperature)
                    cls.time_of_last_click = datetime.datetime.now().timestamp()
                    print("New time for last click: ", cls.time_of_last_click)
                    
        elif cls.time_of_last_click == 0:
            if cls.initial_temperature > cls.target_temperature:
                print("We are cooling the water")
                # We are cooling the water
                set_temperature(cls.current_temperature,cls.current_temperature-0.5)
                cls.current_temperature = cls.current_temperature-0.5
                print("Current temperature: ", current_temperature)
                cls.time_of_last_click = datetime.datetime.now().timestamp()
                print("New time for last click: ", cls.time_of_last_click)
                    
            elif cls.initial_temperature < cls.target_temperature:
                print("We are heating the water")
                # We are heating the water
                set_temperature(cls.current_temperature, cls.current_temperature+0.5)
                cls.current_temperature = cls.current_temperature+0.5
                print("Current temperature: ", cls.current_temperature)
                cls.time_of_last_click = datetime.datetime.now().timestamp()
                print("New time for last click: ", cls.time_of_last_click)
        





