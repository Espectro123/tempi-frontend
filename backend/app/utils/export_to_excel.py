import pandas as pd

def export_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("tempi_experiment.xlsx", index=False)
