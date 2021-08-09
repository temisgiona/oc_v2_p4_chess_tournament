from flask_restful import reqparse
import enum
 
class SensorData:
    sensorData_args = reqparse.RequestParser()
    sensorData_args.add_argument("id", type=str)
    sensorData_args.add_argument("user", type=str)
    sensorData_args.add_argument("timestamp", type=str, help="Timestamp is missing", required=True)
    sensorData_args.add_argument("temperature", type=float, help="Temperature is missing", required=True)
    sensorData_args.add_argument("pressure", type=float, help="Pressure is missing", required=True)
    sensorData_args.add_argument("humidity", type=float, help="Humidity is missing", required=True)


class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

class Content(db.Model):
    gender = db.Column(db.Enum(Gender), nullable=False)

def init_db():
    db.session.add(Content("THIS IS SPARTAAAAA!!!!", Gender['male']))
    db.session.add(Content("What is your favorite scary movie ?", Gender['female']))