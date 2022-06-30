from locust import events

from PerformanceTestingWithLocust.taskset.category_navigate import CategoryNavigate
from PerformanceTestingWithLocust.taskset.view_cart import ViewCart
from PerformanceTestingWithLocust.user.guest_http_user import GuestHttpUser
from PerformanceTestingWithLocust.user.registered_http_user import RegisteredHttpUser
from PerformanceTestingWithLocust.taskset.my_account_navigate import MyAccountNavigate
from PerformanceTestingWithLocust.common.user_loader import UserLoader
from PerformanceTestingWithLocust.common.logger import Logger
from PerformanceTestingWithLocust.common.event_influxdb_handler import EventInfluxHandlers


@events.test_start.add_listener
def on_test_start(**kwargs):
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    UserLoader.load_users()
    EventInfluxHandlers.init_influx_client()
    Logger.log_message("......... Initiating Load Test .......")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message("........ Load Test Completed ........")


class UserGroupA(RegisteredHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [MyAccountNavigate, CategoryNavigate, ViewCart]


class UserGroupB(GuestHttpUser):
    weight = 4
    GuestHttpUser.tasks = [CategoryNavigate, ViewCart]





