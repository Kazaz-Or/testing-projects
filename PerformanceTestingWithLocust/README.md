A small project for load & performance testing using Locust framework.

Visualisation of the results is done with docker containers of both InfluxDB & Grafana.

Webapp that was used for testing - http://automationpractice.com/index.php


![6A924C8F-3E18-41AE-BAD5-13DA1031562B](https://user-images.githubusercontent.com/83350680/176703517-ee6e6460-22e3-464f-a8d4-7ad4411006b1.jpeg)


![4321F322-A1F7-472D-8608-52F1454F2656](https://user-images.githubusercontent.com/83350680/176703532-3246480c-7708-48ff-8ca4-9a029007c9d7.jpeg)


To run the tests:

```
locust -f locust_test_load.py --host http://automationpractice.com --logfile run.log
```

Then you can browse into localhost:8089 and configure the number of users/spawn rate.

To run local docker container of InfluxDB:

```
docker pull influxdb
docker run -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb:1.8.2

docker ps
``` 
Extract the ID of the container.
Exec into the container using the container ID.
```
docker exec -it <container-id> bash
```
Run inside the container influx service by running
```
influx
```

Example of SQL queries in the Influx container:

![D0B24348-1DFE-46C8-B774-4144BDAEA690](https://user-images.githubusercontent.com/83350680/176703672-e4d171c8-0bab-4dc5-9159-373c70afcddc.jpeg)




To run local docker container of Grafana:
```
docker pull grafana/grafana

docker run -d --name=grafana -p 3000:3000 grafana/grafana 
```

Browse localhost:3000 
and login with the default creds, (aka: admin, admin)

Eventually it's recommened to verify both containers are running:

```
$ docker ps                                                                                                                         
CONTAINER ID   IMAGE             COMMAND                  CREATED             STATUS             PORTS                    NAMES
f59b987f1dad   grafana/grafana   "/run.sh"                2 minutes ago       Up 2 minutes       0.0.0.0:3000->3000/tcp   grafana
dc4d85a44d40   influxdb:1.8.2    "/entrypoint.sh infl…"   About an hour ago   Up About an hour   0.0.0.0:8086->8086/tcp   angry_payne
```

Example of a very simple Grafana dashboard:

![CCF959F0-E9B9-48A9-BB05-4F5EFBFA0BFF](https://user-images.githubusercontent.com/83350680/176704560-f765fb59-2f71-4cfe-ae3b-2facc868e033.jpeg)
