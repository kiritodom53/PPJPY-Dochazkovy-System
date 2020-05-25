from datetime import datetime

class Validation:

    def month_to_number(x):
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

    def date_convert(input):
        tempDate = input.split("-")
        newDate = tempDate[2] + "." + tempDate[1] + "." + tempDate[0]
        return newDate

    def time_covert(input):
        tempTime = input.split(":")
        newTime = ""
        if (len(tempTime[0]) != 1):
            newTime += tempTime[0]
        else:
            newTime += "0" + tempTime[0]

        newTime += ":"

        if (len(tempTime[1]) != 1):
            newTime += tempTime[1]
        else:
            newTime += "0" + tempTime[1]

        return newTime

    def pocet_hodin(time_1, time_2):
        format = '%H:%M'
        date_x = datetime.strptime(Validation.time_covert(time_1), format) - datetime.strptime(Validation.time_covert(time_2), format)
        string_x = str(date_x)
        string_x = string_x[:-3]
        return Validation.time_covert(string_x)

    def number_to_time(hours, minutes):
        m = str('{:02d}:{:02d}'.format(*divmod(minutes, 60))) # Minuty na na hh:mm
        final_h = int(hours) + int(m.split(":")[0]) # Final hodiny
        final = str(final_h) + ":" + str(int(m.split(":")[1]))
        return final