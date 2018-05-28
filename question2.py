class phonebill:
    def __init__(self,accountnumber,surname,outstanding, service, minutes):
        self.accountnumber = accountnumber
        self.surname = surname
        self.outstanding = outstanding
        self.service = service
        self.minutes = minutes
        if service == 'R':
            if int(minutes)<=50:
                self.charge == 10
            else:
                self.charge = 10 + ((minutes-50)*.20)
        else:
            if minutes[0] < 75:
                chargeA=0
            else:
                chargeA=(minutes[0]-75)*10
            if minutes[1] < 100:
                chargeB=0
            else:
                chargeB=float((minutes[1]-100))*float(0.05)
            self.charge = float(chargeA + chargeB)

cust_1 = phonebill('A9845','Hurley',37.5,'R',55)
cust_2 = phonebill('A9846','Hicks',00.00,'P', [70, 139])

print(cust_2.__dict__)

