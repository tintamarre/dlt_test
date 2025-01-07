import typer

import dlt
import pandas as pd
from rich import print

app = typer.Typer()

@app.command()
def run():
    parquet_url = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/234002/exports/parquet?lang=fr&timezone=Europe%2FBrussels"
    data = pd.read_parquet(parquet_url)

    pipeline = dlt.pipeline(
        pipeline_name="quick_start", 
        destination="duckdb", 
        dataset_name="main"
    )
    load_info = pipeline.run(   
                            data, table_name="prix_immobilier_residentiel_belgique"
                            )

    print(load_info)

if __name__ == "__main__":
    app()
    