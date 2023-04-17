class Info:
    def __init__(self,city,wastage,impact):
        self.city = city
        self.wastage = wastage
        self.impact =impact
    def __str__(self):

        return str(self.city) + ", " + str(self.wastage)+ "Kgs" + ", " +"has impact on " + str(self.impact)+ " people"