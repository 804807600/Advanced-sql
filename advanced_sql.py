# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'


import pandas as pd
import datetime as dt
from datetime import datetime
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import desc
engine = create_engine("sqlite:///
")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
# Find most recent date
last_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
last_date
# Design a query to retrieve the last 12 months of precipitation data and plot the results

one_year_ago=dt.datetime(2017,8,23)-dt.timedelta(days=365)

from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def home():
    """List all api routes available"""
    return(f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"Convert the query results to a Dictionary using date as the key and prcp as the value.<br/>"
        f"/api/v1.0/stations<br/>"
        f"Return a JSON list of stations from the dataset.<br/>"
        f"/api/v1.0/tobs<br/>"
        f"Return a JSON list of Temperature Observations (tobs) for the previous year.<br/>"
        f"/api/v1.0/start<br/>"
        f"When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.<br/>"
        f"/api/v1.0/start/end<br/>"
        f"When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.<br/>")


    
if __name__=="__main__":
    app.run(debug=True)