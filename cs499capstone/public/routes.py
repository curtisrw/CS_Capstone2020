# stl
import datetime
from json import dumps
from typing import TYPE_CHECKING

# PIP
from flask import Blueprint, render_template, request

if TYPE_CHECKING:
    from types import ModuleType
    from typing import NewType

    JSON = NewType("JSON", str)


bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
<<<<<<< Updated upstream
    return render_template("index.html")


@bp.route("/door-state")
def get_door_state():
    result = db_door_state()
    return result or ("", 204)


@bp.route("/light-state")
def get_light_state():
    result = db_light_state()
    return result or ("", 204)


@bp.route("/window-state")
def get_window_state():
    result = db_window_state()
    return result or ("", 204)


@bp.route("/home-stats")
def get_home_stats():
    start = request.args.get("date_start")
    start = request.args.get("date_start")
    end = request.args.get("date_end")
    result = db_home_stats(start, end)
    return result or ("", 204)  # 204 is No Content


################
# HELPER FUNCS #
################


def db_home_stats(date_start: "datetime.date", date_end: "datetime.date") -> "JSON":
    # TODO: create basic daterange query over db connection
    # TODO: make that query variable over the data types collected
    return "Home Stats"


def db_door_state():
    # TODO: db query to get state of doors
    return "Door State"


def db_light_state():
    # TODO: db query to get state of lights
    return "Light State"


def db_window_state():
    # TODO: query
    return "Window State"
=======
    """ Home page of website.
    Renders the chart of the last 30 days of data."""
    _log.info("Started PSQL connection on index endpoint")
    init_psql()
    data = chart_data(g.psql)
    cur_day = data.cur_day
    data.import_chart_data(end=cur_day)

    next_day_form = NextDayForm()
    if next_day_form.validate_on_submit():
        _log.info("Simulating day")
        simulate_day(g.psql)
        _log.info("Finished simulating day")

    temperature_form = TemperatureForm()
    if temperature_form.validate_on_submit():
        temp = temperature_form.settemp.data
        _log.info("Setting temperature to %s", temperature_form.settemp.data)
        set_temp(g.psql, temp)

    toggle_object_form = ToggleObjectForm()
    if toggle_object_form.validate_on_submit():
        toggle_obj_state(
            g.psql,
            toggle_object_form.object_table.data,
            toggle_object_form.object_type.data,
        )

    chart_select_form = DataSelectForm()
    if chart_select_form.validate_on_submit():
        stat = chart_select_form.data_to_show.data
        return render_template(
            "index.html",
            values=data.__getattribute__(stat),
            labels=data.labels,
            legend=map_label_to_legend(stat),
            chart_select_form=chart_select_form,
            toggle_object_form=toggle_object_form,
            temperature_form=temperature_form,
            next_day_form=next_day_form,
        )
    else:
        return render_template(
            "index.html",
            values=data.intemp,
            labels=data.labels,
            legend="Inside Temperature",
            chart_select_form=chart_select_form,
            toggle_object_form=toggle_object_form,
            temperature_form=temperature_form,
            next_day_form=next_day_form,
        )


##########################
# SECONDARY PAGE CONTENT #
##########################


@bp.route("/admin")
def admin():
    
    # toggle_object_form = ToggleObjectForm()
    # if toggle_object_form.object_type.lights.toggle_obj_state == True:
    #     return render_template("admin.html")
    # else:
    #  

        return render_template("admin.html")
>>>>>>> Stashed changes
