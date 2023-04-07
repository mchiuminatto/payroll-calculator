import logging
from enum import Enum
import time

from payroll_calculator import constants
from payroll_calculator.utils import time_interval_algebra as tia


class WeekDays(Enum):
    SU = "SU"
    MO = "MO"
    TU = "TU"
    WE = "WE"
    TH = "TH"
    FR = "FR"
    SA = "SA"


class EmployeeSalary:

    def __init__(self):
        # region data_table
        self.rate_table = {WeekDays.MO: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 15.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         ],
                           WeekDays.TU: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 15.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         ],
                           WeekDays.WE: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 15.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         ],
                           WeekDays.TH: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 15.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         ],
                           WeekDays.FR: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 15.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         ],
                           WeekDays.SA: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 30.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 25.00
                                          }],
                           WeekDays.SU: [{"start_time": time.strptime("00:00", "%H:%M"),
                                          "end_time": time.strptime("09:00", "%H:%M"),
                                          "rate": 30.00
                                          },
                                         {"start_time": time.strptime("09:01", "%H:%M"),
                                          "end_time": time.strptime("18:00", "%H:%M"),
                                          "rate": 20.00
                                          },
                                         {"start_time": time.strptime("18:01", "%H:%M"),
                                          "end_time": time.strptime("23:59", "%H:%M"),
                                          "rate": 25.00
                                          },
                                         ]
                           }

        # endregion

    def _collect_salary_data(self, day_hours: dict) -> list:

        day_rates = self.rate_table[day_hours["weekday"]]
        day_time_from = day_hours["time_from"]
        day_time_to = day_hours["time_to"]
        found_start: bool = False

        salary_rates: list = []
        for interval in day_rates:
            if not found_start:
                if tia.is_inside(day_time_from,
                                 interval["start_time"],
                                 interval["end_time"]):
                    found_start = True
                    logging.info("Found interval for range start")
                    if tia.is_inside(day_time_to,
                                     interval["start_time"],
                                     interval["end_time"]
                                     ):
                        interval_time_min: float = (time.mktime(day_time_to) -
                                                    time.mktime(day_time_from)) / 60

                        interval_rate: float = interval["rate"]
                        salary_rates.append({"day": day_hours["weekday"],
                                             "interval_time_min": interval_time_min,
                                             "interval_rate": interval_rate})

                        logging.info(f"Found and inside interval for range end [%s, %s]",
                                     interval["start_time"], interval["end_time"])
                        break

                    else:
                        interval_time_min: float = (time.mktime(interval["end_time"]) -
                                                    time.mktime(day_time_from)) / 60

                        interval_rate: float = interval["rate"]
                        salary_rates.append({"day": day_hours["weekday"],
                                             "interval_time_min": interval_time_min,
                                             "interval_rate": interval_rate})

                        logging.info("Not found range for interval and yet")

            else:
                if tia.is_inside(day_time_to,
                                 interval["start_time"],
                                 interval["end_time"]
                                 ):
                    interval_time_min: float = (time.mktime(day_time_to) -
                                                time.mktime(interval["start_time"])) / 60

                    interval_rate: float = interval["rate"]
                    salary_rates.append({"day": day_hours["weekday"],
                                         "interval_time_min": interval_time_min,
                                         "interval_rate": interval_rate})

                    logging.info("Found the end interval")
                    break
                else:
                    interval_time_min: float = (time.mktime(interval["end_time"]) -
                                                time.mktime(interval["start_time"])) / 60
                    interval_rate: float = interval["rate"]
                    salary_rates.append({"day": day_hours["weekday"],
                                         "interval_time_min": interval_time_min,
                                         "interval_rate": interval_rate})
                    logging.info("Found a full interval")

        return salary_rates

    def _compute_employee(self, employee_record: dict) -> dict:
        """
        Compute one employee salary for a set of working days

        :param employee_record:
        :return:
        """

        worked_days_salary: list = []
        for work_day in employee_record["data"]:
            worked_days_salary += self._collect_salary_data(work_day)
        total_rate: float = 0
        logging.info("Calculating salary for %s", {employee_record['name']})
        for salary_entry in worked_days_salary:
            logging.info("Salary entry %s", salary_entry)
            total_rate += round(salary_entry["interval_time_min"] * salary_entry["interval_rate"] / 60,
                                constants.DECIMAL_PLACES)

        return {"name": employee_record["name"], "salary": total_rate}

    def compute_payroll(self, worked_days_data: list) -> list:

        payroll: list = list()
        for employee_record in worked_days_data:
            payroll.append(self._compute_employee(employee_record))

        return payroll
