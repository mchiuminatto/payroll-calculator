import time

from payroll_calculator.payroll.payroll_calculator import EmployeeSalary
from payroll_calculator.payroll.payroll_calculator import WeekDays

employee_record_inside: dict = {"name": "RENE",
                                "data": [
                                    {"weekday": WeekDays.MO,
                                     "time_from": time.strptime("10:00", "%H:%M"),
                                     "time_to": time.strptime("12:00", "%H:%M")
                                     },
                                    {"weekday": WeekDays.TU,
                                     "time_from": time.strptime("10:00", "%H:%M"),
                                     "time_to": time.strptime("12:00", "%H:%M")
                                     },
                                    {"weekday": WeekDays.TH,
                                     "time_from": time.strptime("01:00", "%H:%M"),
                                     "time_to": time.strptime("03:00", "%H:%M")
                                     },
                                    {"weekday": WeekDays.SA,
                                     "time_from": time.strptime("14:00", "%H:%M"),
                                     "time_to": time.strptime("18:00", "%H:%M")
                                     },
                                    {"weekday": WeekDays.SU,
                                     "time_from": time.strptime("20:00", "%H:%M"),
                                     "time_to": time.strptime("21:00", "%H:%M")
                                     },
                                ]
                                }

employee_record_two_ranges: dict = {"name": "MARCELLO",
                                    "data": [
                                        {"weekday": WeekDays.MO,
                                         "time_from": time.strptime("08:00", "%H:%M"),
                                         "time_to": time.strptime("12:00", "%H:%M")
                                         }
                                    ]
                                    }

employee_record_extended: dict = {"name": "WILLIAM",
                                  "data": [
                                      {"weekday": WeekDays.MO,
                                       "time_from": time.strptime("08:00", "%H:%M"),
                                       "time_to": time.strptime("15:00", "%H:%M")
                                       }
                                  ]
                                  }


def test_calculate_one_day_salary():
    employee_salary_calculator = EmployeeSalary()
    employee_day_salary: list = employee_salary_calculator._collect_salary_data(
        employee_record_inside["data"][0])
    assert employee_day_salary[0]["interval_time_min"] == 120.0 and employee_day_salary[0]["interval_rate"] == 15.0


def test_calculate_multiple_days():
    employee_salary_calculator = EmployeeSalary()

    for worked_day in employee_record_inside["data"]:
        employee_day_salary: list = employee_salary_calculator._collect_salary_data(worked_day)

    assert employee_day_salary[0]["interval_time_min"] == 60 and employee_day_salary[0]["interval_rate"] == 25


def test_calculate_employee_salary():
    employee_salary_calculator = EmployeeSalary()
    employee_salary: dict = employee_salary_calculator._compute_employee(employee_record_inside)
    assert employee_salary["salary"] == 215


def test_calculate_employee_salary_two_ranges():
    employee_salary_calculator = EmployeeSalary()
    employee_salary: dict = employee_salary_calculator._compute_employee(employee_record_two_ranges)
    assert employee_salary["salary"] == 69.75


def test_calculate_employee_salary_extended():
    employee_salary_calculator = EmployeeSalary()
    employee_salary: dict = employee_salary_calculator._compute_employee(employee_record_extended)
    assert employee_salary["salary"] == 114.75
