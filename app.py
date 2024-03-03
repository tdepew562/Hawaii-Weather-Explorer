import datetime as dt
import os
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create Flask app
app = Flask(__name__)

# Create engine to connect to SQLite database
engine = create_engine("sqlite:///C:/Users/Thomas/Desktop/Finished Projects/Project 10 Finished/Resources/hawaii.sqlite")

# Reflect the database tables
Base = automap_base()
Base.prepare(engine)

# Manually reflect each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Define routes
@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return JSON representation of precipitation data for the last 12 months."""
    session = Session(engine)
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    start_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= start_date).all()
    session.close()
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return JSON list of stations."""
    session = Session(engine)
    stations = session.query(Station.station).all()
    session.close()
    station_list = [station[0] for station in stations]
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return JSON list of temperature observations for the last year of the most active station."""
    session = Session(engine)
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    most_recent_date = session.query(func.max(Measurement.date)).filter(Measurement.station == most_active_station).scalar()
    start_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= start_date).all()
    session.close()
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in tobs_data]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temp_start(start):
    """Return JSON list of min, max, and avg temperatures from start date to end of dataset."""
    session = Session(engine)
    temps = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
    temp_list = [{"start_date": start, "end_date": "last_date_in_dataset", "min_temp": min_temp, "max_temp": max_temp, "avg_temp": avg_temp} for min_temp, max_temp, avg_temp in temps]
    return jsonify(temp_list)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start, end):
    """Return JSON list of min, max, and avg temperatures from start date to end date."""
    session = Session(engine)
    temps = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temp_list = [{"start_date": start, "end_date": end, "min_temp": min_temp, "max_temp": max_temp, "avg_temp": avg_temp} for min_temp, max_temp, avg_temp in temps]
    return jsonify(temp_list)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)




