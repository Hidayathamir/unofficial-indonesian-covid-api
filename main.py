from fastapi import FastAPI, Path, Query, Response, status

from src import api

desc = "**Unofficial Indonesian Covid Api** to know about current status of covid cases in Indonesia. Official api : https://data.covid19.go.id/public/api/update.json"
tags_metadata = [
    {
        "name": "root",
        "description": "Root of the api, just want to ask user to go to this documentation.",
    },
    {
        "name": "index",
        "description": "General information of covid cases.",
    },
    {
        "name": "yearly",
        "description": "List the data by yearly.",
    },
    {
        "name": "monthly",
        "description": "List the data by monthly.",
    },
    {
        "name": "daily",
        "description": "List the data by daily.",
    },
]
app = FastAPI(
    title="Unofficial Indonesian Covid Api",
    description=desc,
    version="0.0.2",
    contact={
        "name": "Hidayat",
        "url": "https://github.com/Hidayathamir",
        "email": "hidayathamir@gmail.com",
    },
    openapi_tags=tags_metadata,
)


@app.get("/", tags=["root"])
async def root():
    res = {
        "message": "Go to https://incovapi.deta.dev/docs for the documentation on how to use this api"
    }
    return res


@app.get("/api/v1/", tags=["index"])
async def index():
    json_data = api.get_json_data()
    res = api.index(json_data)
    return res


@app.get("/api/v1/yearly", tags=["yearly"])
async def yearly(
    response: Response,
    since: str = Query(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="Since what year?",
    ),
    upto: str = Query(
        ...,
        example="2022",
        max_length=4,
        min_length=4,
        description="Until what year?",
    ),
):
    df = api.get_df()
    _, res = api.yearly(df, since, upto)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/yearly/{year}", tags=["yearly"])
async def yearly_y(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
):
    df = api.get_df()
    _, res = api.yearly_y(df, year)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/monthly", tags=["monthly"])
async def monthly(
    response: Response,
    since: str = Query(
        ...,
        example="2020-06",
        max_length=7,
        min_length=7,
        description="Since what year-month?",
    ),
    upto: str = Query(
        ...,
        example="2022-06",
        max_length=7,
        min_length=7,
        description="Until what year-month?",
    ),
):
    df = api.get_df()
    _, res = api.monthly(df, since, upto)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/monthly/{year}", tags=["monthly"])
async def monthly_y(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
):
    df = api.get_df()
    _, res = api.monthly_y(df, year)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/monthly/{year}/{month}", tags=["monthly"])
async def monthly_ym(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
    month: str = Path(
        ...,
        example="06",
        max_length=2,
        min_length=2,
        description="What month?",
    ),
):
    df = api.get_df()
    _, res = api.monthly_ym(df, year, month)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/daily", tags=["daily"])
async def daily(
    response: Response,
    since: str = Query(
        ...,
        example="2020-09-04",
        max_length=10,
        min_length=10,
        description="Since what year-month-date?",
    ),
    upto: str = Query(
        ...,
        example="2022-05-03",
        max_length=10,
        min_length=10,
        description="Until what year-month-date?",
    ),
):
    df = api.get_df()
    _, res = api.daily(df, since, upto)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/daily/{year}", tags=["daily"])
async def daily_y(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
):
    df = api.get_df()
    _, res = api.daily_y(df, year)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/daily/{year}/{month}", tags=["daily"])
async def daily_ym(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
    month: str = Path(
        ...,
        example="06",
        max_length=2,
        min_length=2,
        description="What month?",
    ),
):
    df = api.get_df()
    _, res = api.daily_ym(df, year, month)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res


@app.get("/api/v1/daily/{year}/{month}/{date}", tags=["daily"])
async def daily_ymd(
    response: Response,
    year: str = Path(
        ...,
        example="2020",
        max_length=4,
        min_length=4,
        description="What year?",
    ),
    month: str = Path(
        ...,
        example="06",
        max_length=2,
        min_length=2,
        description="What month?",
    ),
    date: str = Path(
        ...,
        example="03",
        max_length=2,
        min_length=2,
        description="What date?",
    ),
):
    df = api.get_df()
    _, res = api.daily_ymd(df, year, month, date)
    if res["ok"] is False:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return res
