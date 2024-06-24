include .env
export

venv-activate:
	source ./venv/bin/activate
venv-deactivate:
	deactivate
locust-run:
	locust -f scenario1-v3.py --host=http://localhost:8080/api/v1 --pyexec "python -c \"import influxdb_listener\""
locust-run-item:
	locust -f item_count.py --host=http://localhost:8080/api/v1
monitoring-up:
	docker-cmpose up -d
locust-run-influxdb:
#	INFLUXDB_URL=
#	INFLUXDB_TOKEN=
#	INFLUXDB_ORG=
#	INFLUXDB_BUCKET=
	locust -f influxdb_listener.py,scenario1-v3.py \
	--host=http://localhost:8080/api/v1

