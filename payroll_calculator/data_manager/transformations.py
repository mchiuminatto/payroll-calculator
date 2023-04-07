import logging
import re
from re import Match
import time
from payroll_calculator.payroll.payroll_calculator import WeekDays

WEEK_DAY_MAP: dict = {"MO": WeekDays.MO,
                      "TU": WeekDays.TU,
                      "WE": WeekDays.WE,
                      "TH": WeekDays.TH,
                      "FR": WeekDays.FR,
                      "SA": WeekDays.SA,
                      "SU": WeekDays.SU
                      }

RECORD_PATTERN = r"([A-Z][A-Z])(\d{2}:\d{2})-(\d{2}:\d{2})"


class ParseWorkedDayData:
    """
    Parses the workday record per user
    """

    @staticmethod
    def parse_worked_day_record(record) -> dict:

        name: str = record.split("=")[0]
        if name == "":
            raise ValueError(f"Record has no name {record}")

        employee_record = {"name": name, "data": []}
        working_days_record: str = record.split("=")[1]
        working_days: list = working_days_record.split(",")

        for working_day in working_days:
            match: Match[str] = re.search(RECORD_PATTERN, working_day)
            if match is None:
                logging.error("Work range record not valid %s for user %s", working_day, name)
                continue

            week_day: str = match.group(1)
            time_from: str = match.group(2)
            time_to: str = match.group(3)

            worked_day: dict = {
                "weekday": WEEK_DAY_MAP[week_day],
                "time_from": time.strptime(time_from, "%H:%M"),
                "time_to": time.strptime(time_to, "%H:%M")
            }
            employee_record["data"].append(worked_day)

        logging.info("Parsed working day for %s", name)
        return employee_record

    @staticmethod
    def parse(employee_records: list) -> list:

        parsed_employee_records: list = []
        parser = ParseWorkedDayData()
        for employee_record in employee_records:
            parsed_record: dict = parser.parse_worked_day_record(employee_record)
            parsed_employee_records.append(parsed_record)

        return parsed_employee_records
