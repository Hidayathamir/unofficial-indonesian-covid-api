import json
import urllib.request
from datetime import datetime
from typing import Any, Dict, Tuple

from pandas import DataFrame


def get_json_data() -> Dict[str, Any]:
    api_url = "https://data.covid19.go.id/public/api/update.json"
    with urllib.request.urlopen(api_url) as url:
        json_data = json.loads(url.read().decode())
    return json_data


def get_df() -> DataFrame:
    json_data = get_json_data()
    mydata = {
        "date": [],
        "meninggal": [],
        "sembuh": [],
        "positif": [],
        "dirawat": [],
    }
    for i in json_data["update"]["harian"]:
        dt = i["key_as_string"]
        dt = datetime.strptime(dt, "%Y-%m-%dT00:00:00.000Z")
        mydata["date"].append(dt)
        mydata["meninggal"].append(i["jumlah_meninggal"]["value"])
        mydata["sembuh"].append(i["jumlah_sembuh"]["value"])
        mydata["positif"].append(i["jumlah_positif"]["value"])
        mydata["dirawat"].append(i["jumlah_dirawat"]["value"])
    df = DataFrame.from_dict(mydata)
    df = df.set_index("date")
    return df


def index(myjson: Dict[str, Any]) -> Dict[str, Any]:
    res = {
        "ok": True,
        "data": {
            "total_positive": myjson["update"]["total"]["jumlah_positif"],
            "total_recovered": myjson["update"]["total"]["jumlah_sembuh"],
            "total_deaths": myjson["update"]["total"]["jumlah_meninggal"],
            "total_active": myjson["update"]["total"]["jumlah_dirawat"],
            "new_positive": myjson["update"]["penambahan"]["jumlah_positif"],
            "new_recovered": myjson["update"]["penambahan"]["jumlah_sembuh"],
            "new_deaths": myjson["update"]["penambahan"]["jumlah_meninggal"],
            "new_active": myjson["update"]["penambahan"]["jumlah_dirawat"],
        },
        "message": "success",
    }
    return res


def get_res_success() -> Dict[str, Any]:
    res = {
        "ok": True,
        "data": [],
        "message": "success",
    }
    return res


def get_res_failled() -> Dict[str, Any]:
    res = {
        "ok": False,
        "data": [],
        "message": "error",
    }
    return res


def yearly(
    df: DataFrame, since: str, upto: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    try:
        a = df.loc[since:upto]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res
    a = a.groupby(a.index.to_period("Y")).sum()

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "year": str(i),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def yearly_y(df: DataFrame, year: str):
    try:
        a = df.loc[year:year].sum()
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = {
        "ok": True,
        "data": {
            "year": year,
            "positive": a.positif.item(),
            "recovered": a.sembuh.item(),
            "deaths": a.meninggal.item(),
            "active": a.dirawat.item(),
        },
        "message": "success",
    }
    return a, res


def monthly(
    df: DataFrame, since: str, upto: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    try:
        a = df.loc[since:upto]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    a = a.groupby(a.index.to_period("M")).sum()

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "month": i.strftime("%Y-%m"),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def monthly_y(df: DataFrame, year: str) -> Tuple[DataFrame, Dict[str, Any]]:
    try:
        a = df.loc[year:year]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    a = a.groupby(a.index.to_period("M")).sum()

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "month": str(i),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def monthly_ym(
    df: DataFrame, year: str, month: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    month = f"{year}-{month}"
    try:
        a = df.loc[month:month].sum()
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = {
        "ok": True,
        "data": {
            "month": month,
            "positive": a.positif.item(),
            "recovered": a.sembuh.item(),
            "deaths": a.meninggal.item(),
            "active": a.dirawat.item(),
        },
        "message": "success",
    }
    return a, res


def daily(
    df: DataFrame, since: str, upto: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    try:
        a = df.loc[since:upto]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "date": i.strftime("%Y-%m-%d"),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def daily_y(df: DataFrame, year: str) -> Tuple[DataFrame, Dict[str, Any]]:
    try:
        a = df.loc[year:year]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "date": i.strftime("%Y-%m-%d"),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def daily_ym(
    df: DataFrame, year: str, month: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    month = f"{year}-{month}"
    try:
        a = df.loc[month:month]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = get_res_success()

    for i in a.index:
        res["data"].append(
            {
                "date": i.strftime("%Y-%m-%d"),
                "positive": a.loc[i].positif.item(),
                "recovered": a.loc[i].sembuh.item(),
                "deaths": a.loc[i].meninggal.item(),
                "active": a.loc[i].dirawat.item(),
            }
        )
    return a, res


def daily_ymd(
    df: DataFrame, year: str, month: str, date: str
) -> Tuple[DataFrame, Dict[str, Any]]:
    date = f"{year}-{month}-{date}"
    try:
        a = df.loc[date:date]
    except (TypeError, ValueError) as e:
        res = get_res_failled()
        res["message"] = str(e)
        return df, res

    res = {
        "ok": True,
        "data": {
            "date": date,
            "positive": a.positif.item(),
            "recovered": a.sembuh.item(),
            "deaths": a.meninggal.item(),
            "active": a.dirawat.item(),
        },
        "message": "success",
    }
    return a, res
