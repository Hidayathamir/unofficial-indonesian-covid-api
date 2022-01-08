# unofficial-indonesian-covid-api

Unofficial Indonesian Covid Api to know about current status of covid cases in Indonesia. Official api : https://data.covid19.go.id/public/api/update.json

docs & live : [https://incovapi.deta.dev/docs](https://incovapi.deta.dev/docs)

![documentation](README_assets/docs.png)

# How To Run Locally
1. Install requirements.
```
pip install -r requirements.txt
```
2. Run local server.
```
uvicorn main:app
```
3. Open browser and go to the url [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

# Docker Version
Docker version can be found [here](https://hub.docker.com/r/hidayathamir/unofficial-indonesian-covid-api). You need to know how to run docker image and map docker host port to port 8000 in the container.

# API Contract
1. GET `https://<host>:<port>/api/v1/`. Entry point for all API, provide general information of covid cases.
2. GET `https://<host>:<port>/api/v1/yearly?since=<year>&upto=<year>`. Provide yearly data of total covid cases.
3. GET `https://<host>:<port>/api/v1/yearly/<year>`. Provide yearly data of total covid cases of the year provided in `<year>`.
4. GET `https://<host>:<port>/api/v1/monthly?since=<year>-<month>&upto=<year>-<month>`. Provide monthly data of total covid cases.
5. GET `https://<host>:<port>/api/v1/monthly/<year>`. Provide monthly data of total covid cases in the year provided in `<year>`.
6. GET `https://<host>:<port>/api/v1/monthly/<year>/<month>`. Provide monthly data of total covid cases in the month and year provided in `<year>` and
`<month>`.
7. GET `https://<host>:<port>/api/v1/daily?since=<year>-<month>-<date>&upto=<year>-<month>-<date>`. Provide daily data of covid cases.
8. GET `https://<host>:<port>/api/v1/daily/<year>`. Provide daily data of covid cases in the year provided in `<year>`.
9. GET `https://<host>:<port>/api/v1/daily/<year>/<month>`. Provide daily data of covid cases in the year and month provided in `<year>` and `<month>`.
10. GET `https://<host>:<port>/api/v1/daily/<year>/<month>/<date>`. Provide daily data of covid cases on the day provided in `<year>`, `<month>` and, `<date>`.

# Current Limitations, Potential Issues, Future Ideations
This project doesn't use any database, for every request it doing request to official api to get data and then use it to send response to user. If the official api makes changes to their api, then maybe this project will crash. <br>
Also, I don't know if the official api has some kind of limit on how many requests, if any then this project can't handle more requests than the limit. <br>
For future improvements I am looking for using database. then do daily update from official api.

# Note For Nodeflux
I create this project to complete the assignment `Software Engineer Internship Technical Assessment - Batch 2`. When I deployed the project to [deta](https://www.deta.sh/) I just found out that I made some kind of mistake. On your instructions you asked to do like this `?since=2020.03.02`, but I do this `?since=2020-03-02`. I think it doesn't matter, since our goal is to test my ability.<br>
I also chose to use the `/api/v1` prefix because I thought it would be good to version-ing the api so that it is scalable.
