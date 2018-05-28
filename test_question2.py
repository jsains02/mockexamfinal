class phonebill:
    def __init__(self,accountnumber,surname, service, minutes):
        self.accountnumber = accountnumber
        self.surname = surname
        self.service = service
        self.minutes = minutes
        if service == R:
            if int(minutes)<=50:
                charge == 10
            else:
                charge = 10 + ((minutes-50)*.20)
        else:
            for i in minutes:
                if i == 1:
                    if minutes[i] < 75:
                        chargeA=0
                    else:
                        chargeA=(minutes[i]-75)*10
                if i ==2:
                    if minutes[i] < 100:
                        chargeA=0
                    else:
                        chargeA=(minutes[i]-100)*5

