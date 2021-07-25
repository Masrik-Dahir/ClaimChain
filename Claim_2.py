class Claim_block(object):

    def __init__(self, Month, WeekOfMonth, DayOfWeek, Make, AccidentArea, DayOfWeekClaimed, MonthClaimed, WeekOfMonthClaimed, Sex,MaritalStatus,
                 Age,Fault,PolicyType,VehicleCategory,VehiclePrice,FraudFound_P,PolicyNumber,RepNumber,
                 Deductible,DriverRating,Days_Policy_Accident,Days_Policy_Claim,PastNumberOfClaims,AgeOfVehicle,AgeOfPolicyHolder,
                 PoliceReportFiled,WitnessPresent,
                 AgentType,NumberOfSuppliments,AddressChange_Claim,NumberOfCars,Year,BasePolicy):
        self.Month = Month
        self.WeekOfMonth = WeekOfMonth
        self.DayOfWeek = DayOfWeek
        self.Make = Make
        self.AccidentArea = AccidentArea
        self.DayOfWeekClaimed = DayOfWeekClaimed
        self.MonthClaimed = MonthClaimed
        self.WeekOfMonthClaimed = WeekOfMonthClaimed
        self.Sex = Sex
        self.MaritalStatus = MaritalStatus
        self.Age = Age
        self.Fault = Fault
        self.PolicyType = PolicyType
        self.VehicleCategory = VehicleCategory
        self.VehiclePrice = VehiclePrice
        self.FraudFound_P = FraudFound_P
        self.PolicyNumber = PolicyNumber
        self.RepNumber = RepNumber
        self.Deductible = Deductible
        self.DriverRating = DriverRating
        self.Days_Policy_Accident = Days_Policy_Accident
        self.Days_Policy_Claim = Days_Policy_Claim
        self.PastNumberOfClaims = PastNumberOfClaims
        self.AgeOfVehicle = AgeOfVehicle
        self.AgeOfPolicyHolder = AgeOfPolicyHolder
        self.PoliceReportFiled = PoliceReportFiled
        self.WitnessPresent = WitnessPresent
        self.AgentType = AgentType
        self.NumberOfSuppliments = NumberOfSuppliments
        self.AddressChange_Claim = AddressChange_Claim
        self.NumberOfCars = NumberOfCars
        self.Year = Year
        self.BasePolicy = BasePolicy

    def getMonth(self):
        return self.Month

    def getWeekOfMonth(self):
        return self.WeekOfMonth

    def getDayOfWeek(self):
        return self.DayOfWeek

    def getMake(self):
        return self.Make

    def getAccidentArea(self):
        return self.AccidentArea

    def getDayOfWeekClaimed(self):
        return self.DayOfWeekClaimed

    def getMonthClaimed(self):
        return self.MonthClaimed

    def getWeekOfMonthClaimed(self):
        return self.WeekOfMonthClaimed

    def getSex(self):
        return self.Sex

    def getMaritalStatus(self):
        return self.MaritalStatus

    def getAge(self):
        return self.Age

    def getFault(self):
        return self.Fault

    def getPolicyType(self):
        return self.PolicyType

    def getVehicleCategory(self):
        return self.VehicleCategory

    def getVehiclePrice(self):
        return self.VehiclePrice

    def getFraudFound_P(self):
        return self.FraudFound_P

    def getPolicyNumber(self):
        return self.PolicyNumber

    def getRepNumber(self):
        return self.RepNumber

    def getDeductible(self):
        return self.Deductible

    def getDriverRating(self):
        return self.DriverRating

    def getDays_Policy_Accident(self):
        return self.Days_Policy_Accident

    def getDays_Policy_Claim(self):
        return self.Days_Policy_Claim

    def getPastNumberOfClaims(self):
        return self.PastNumberOfClaims

    def getAgeOfVehicle(self):
        return self.AgeOfVehicle

    def getAgeOfPolicyHolder(self):
        return self.AgeOfPolicyHolder

    def getPoliceReportFiled(self):
        return self.PoliceReportFiled

    def getWitnessPresent(self):
        return self.WitnessPresent

    def getAgentType(self):
        return self.AgentType

    def getNumberOfSuppliments(self):
        return self.NumberOfSuppliments

    def getAddressChange_Claim(self):
        return self.AddressChange_Claim

    def getNumberOfCars(self):
        return self.NumberOfCars

    def getYear(self):
        return self.Year

    def getBasePolicy(self):
        return self.BasePolicy

    def toDictionary(self):
        dic = {}
        dic["Month"] = self.Month
        dic["WeekOfMonth"] = self.WeekOfMonth
        dic["DayOfWeek"] = self.DayOfWeek
        dic["Make"] = self.Make
        dic["AccidentArea"] = self.AccidentArea
        dic["DayOfWeekClaimed"] = self.DayOfWeekClaimed
        dic["MonthClaimed"] = self.MonthClaimed
        dic["WeekOfMonthClaimed"] = self.WeekOfMonthClaimed
        dic["Sex"] = self.Sex
        dic["MaritalStatus"] = self.MaritalStatus
        dic["Age"] = self.Age
        dic["Fault"] = self.Fault
        dic["PolicyType"] = self.PolicyType
        dic["VehicleCategory"] = self.VehicleCategory
        dic["VehiclePrice"] = self.VehiclePrice
        dic["FraudFound_P"] = self.FraudFound_P
        dic["PolicyNumber"] = self.PolicyNumber
        dic["RepNumber"] = self.RepNumber
        dic["Deductible"] = self.Deductible
        dic["DriverRating"] = self.DriverRating
        dic["Days_Policy_Accident"] = self.Days_Policy_Accident
        dic["Days_Policy_Claim"] = self.Days_Policy_Claim
        dic["PastNumberOfClaims"] = self.PastNumberOfClaims
        dic["AgeOfVehicle"] = self.AgeOfVehicle
        dic["AgeOfPolicyHolder"] = self.AgeOfPolicyHolder
        dic["PoliceReportFiled"] = self.PoliceReportFiled
        dic["WitnessPresent"] = self.WitnessPresent
        dic["AgentType"] = self.AgentType
        dic["NumberOfSuppliments"] = self.NumberOfSuppliments
        dic["AddressChange_Claim"] = self.AddressChange_Claim
        dic["NumberOfCars"] = self.NumberOfCars
        dic["Year"] = self.Year
        dic["BasePolicy"] = self.BasePolicy
        return dic

    def toList(self):
        lis = []
        lis.append(self.Month)
        lis.append(self.WeekOfMonth)
        lis.append(self.DayOfWeek)
        lis.append(self.Make)
        lis.append(self.AccidentArea)
        lis.append(self.DayOfWeekClaimed)
        lis.append(self.MonthClaimed)
        lis.append(self.WeekOfMonthClaimed)
        lis.append(self.Sex)
        lis.append(self.MaritalStatus)
        lis.append(self.Age)
        lis.append(self.Fault)
        lis.append(self.PolicyType)
        lis.append(self.VehicleCategory)
        lis.append(self.VehiclePrice)
        lis.append(self.FraudFound_P)
        lis.append(self.PolicyNumber)
        lis.append(self.RepNumber)
        lis.append(self.Deductible)
        lis.append(self.DriverRating)
        lis.append(self.Days_Policy_Accident)
        lis.append(self.Days_Policy_Claim)
        lis.append(self.PastNumberOfClaims)
        lis.append(self.AgeOfVehicle)
        lis.append(self.AgeOfPolicyHolder)
        lis.append(self.PoliceReportFiled)
        lis.append(self.WitnessPresent)
        lis.append(self.AgentType)
        lis.append(self.NumberOfSuppliments)
        lis.append(self.AddressChange_Claim)
        lis.append(self.NumberOfCars)
        lis.append(self.Year)
        lis.append(self.BasePolicy)
        return lis
