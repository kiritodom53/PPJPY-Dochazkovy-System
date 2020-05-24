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

    # def month_to_number(self, argument):
    #     switcher = {
    #         "Leden": "01",
    #         "Únor" : "02",
    #         "Březen" : "03",
    #         "Duben" : "04",
    #         "Květen" : "05",
    #         "Červen" : "06",
    #         "Červenec" : "07",
    #         "Srpen" : "08",
    #         "Září" : "09",
    #         "Říjen" : "10",
    #         "Listopad" : "11",
    #         "Prosinec" : "12",
    #
    #     }
    #
    #     return switcher.get(argument, "Invalid month")