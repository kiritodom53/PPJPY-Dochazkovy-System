import binascii
import hashlib
import os
from datetime import datetime


class Validation:
    @staticmethod
    def month_to_number(x: str) -> str:
        """Convert month from Czech text to 2d num format

        Args:
            x (str): Month parameter in full name format (Leden...)
        Returns:
            str: Month in number format (mm)

        """
        return {
            "Leden": "01",
            "Únor": "02",
            "Březen": "03",
            "Duben": "04",
            "Květen": "05",
            "Červen": "06",
            "Červenec": "07",
            "Srpen": "08",
            "Září": "09",
            "Říjen": "10",
            "Listopad": "11",
            "Prosinec": "12",
        }[x]

    @staticmethod
    def get_current_month() -> str:
        """Convert current month from num format to Czech language
        Returns:
            str: Current Month in Czech language
        """
        current_month = datetime.now().month
        print(type(current_month))
        print(current_month)
        return {
            1: "Leden",
            2: "Únor",
            3: "Březen",
            4: "Duben",
            5: "Květen",
            6: "Červen",
            7: "Červenec",
            8: "Srpen",
            9: "Září",
            10: "Říjen",
            11: "Listopad",
            12: "Prosinec",
        }[current_month]

    @staticmethod
    def date_convert(date: str) -> str:
        """Convert month from yyyy-mm-dd to dd.mm.yyyy format
        Args:
            date (str): date in (yyyy-mm-dd) format
        Returns:
            str: Date in (dd.mm.yyy) format
        """
        temp_date = date.split("-")
        new_date = temp_date[2] + "." + temp_date[1] + "." + temp_date[0]
        return new_date

    @staticmethod
    def time_covert(time: str) -> str:
        """Convert time to hh:mm format
        Args:
            time (str): time
        Returns:
            str: time in hh:mm format
        """
        temp_time = time.split(":")
        new_time = ""
        if len(temp_time[0]) != 1:
            new_time += temp_time[0]
        else:
            new_time += "0" + temp_time[0]

        new_time += ":"

        if len(temp_time[1]) != 1:
            new_time += temp_time[1]
        else:
            new_time += "0" + temp_time[1]

        return new_time

    @staticmethod
    def number_of_hours(time_1: str, time_2: str) -> str:
        """Calculates the time between two times

        Args:
            time_1 (str): first time
            time_2 (str): second time

        Returns:
            str: Worked hours
        """
        time_format: str = '%H:%M'
        date_x = datetime.strptime(Validation.time_covert(time_1), time_format) - \
                 datetime.strptime(Validation.time_covert(time_2), time_format)
        string_x: str = str(date_x)
        string_x = string_x[:-3]
        return Validation.time_covert(string_x)


    @staticmethod
    def number_to_time(hours: int, minutes: int) -> str:
        """Convert hours and minutes to hh:mm format

        Args:
            hours (int): hours
            minutes (int): minutes

        Returns:
            str: Time in hh:mm format
        """
        m: str = str('{:02d}:{:02d}'.format(*divmod(minutes, 60)))  # Minutes to hh:mm
        final_time: str = str(int(hours) + int(m.split(":")[0])) + ":" + m.split(":")[1]
        return final_time

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password for storing
        Args:
            password (str): user password for hashing

        Returns:
            str: hash
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        password_hash = hashlib.pbkdf2_hmac('sha512',
                                            password.encode('utf-8'),
                                            salt,
                                            100000)
        password_hash = binascii.hexlify(password_hash)
        return (salt + password_hash).decode('ascii')

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """Verify a stored password against one provided by user
        Args:
            stored_password: password stored in the database
            provided_password: password provided by user

        Returns:
            True if the password match otherwise False
        """
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        password_hash = hashlib.pbkdf2_hmac('sha512',
                                            provided_password.encode('utf-8'),
                                            salt.encode('ascii'),
                                            100000)
        password_hash = binascii.hexlify(password_hash).decode('ascii')
        return password_hash == stored_password
