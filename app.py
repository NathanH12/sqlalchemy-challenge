from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

precipitation_df = pd.read_csv("C:/Users/natha/OneDrive/Documents/Data Analytics Classwork/Week 10 AdvSQL/Module10SQLalchemy/Resources/hawaii_measurements.csv")
stations_df = pd.read_csv("C:/Users/natha/OneDrive/Documents/Data Analytics Classwork/Week 10 AdvSQL/Module10SQLalchemy/Resources/hawaii_stations.csv")

@app.route("/")
def home():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    precipitation_data_dict = precipitation_df.groupby("date").agg({"prcp": "sum"}).to_dict()["prcp"]
    return jsonify(precipitation_data_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations_list = stations_df.to_dict(orient="records")
    return jsonify(stations_list)


if __name__ == "__main__":
    app.run(debug=True)

