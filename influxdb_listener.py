from locust import events
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os

# InfluxDB 연결 설정
influx_client = InfluxDBClient(
    url=os.environ.get('INFLUXDB_URL', 'http://localhost:8086'),
    token=os.environ.get('INFLUXDB_TOKEN', 'your-token'),
    org=os.environ.get('INFLUXDB_ORG', 'your-org')
)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
bucket = os.environ.get('INFLUXDB_BUCKET', 'your-bucket')

@events.request.add_listener
def my_request_handler(request_type, name, response_time, response_length, exception, **kwargs):
    point = Point("locust_requests") \
        .tag("request_type", request_type) \
        .tag("name", name) \
        .field("response_time", response_time) \
        .field("response_length", response_length)

    if exception:
        point.field("exception", str(exception))

    write_api.write(bucket=bucket, record=point)
    # print(f"Data sent to InfluxDB: {request_type} {name} {response_time}ms")

print("InfluxDB listener has been initialized.")