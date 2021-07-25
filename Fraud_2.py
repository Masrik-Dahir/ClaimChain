import os
import pprint
import xlsxwriter as xlsxwriter
import Read


class Result():
    def __init__(self, a, score, reason):
        self.Month = a.Month
        self.WeekOfMonth = a.WeekOfMonth
        self.DayOfWeek = a.DayOfWeek
        self.Make = a.Make
        self.AccidentArea = a.AccidentArea
        self.DayOfWeekClaimed = a.DayOfWeekClaimed
        self.MonthClaimed = a.MonthClaimed
        self.WeekOfMonthClaimed = a.WeekOfMonthClaimed
        self.Sex = a.Sex
        self.MaritalStatus = a.MaritalStatus
        self.Age = a.Age
        self.Fault = a.Fault
        self.PolicyType = a.PolicyType
        self.VehicleCategory = a.VehicleCategory
        self.VehiclePrice = a.VehiclePrice
        self.FraudFound_P = a.FraudFound_P
        self.PolicyNumber = a.PolicyNumber
        self.RepNumber = a.RepNumber
        self.Deductible = a.Deductible
        self.DriverRating = a.DriverRating
        self.Days_Policy_Accident = a.Days_Policy_Accident
        self.Days_Policy_Claim = a.Days_Policy_Claim
        self.PastNumberOfClaims = a.PastNumberOfClaims
        self.AgeOfVehicle = a.AgeOfVehicle
        self.AgeOfPolicyHolder = a.AgeOfPolicyHolder
        self.PoliceReportFiled = a.PoliceReportFiled
        self.WitnessPresent = a.WitnessPresent
        self.AgentType = a.AgentType
        self.NumberOfSuppliments = a.NumberOfSuppliments
        self.AddressChange_Claim = a.AddressChange_Claim
        self.NumberOfCars = a.NumberOfCars
        self.Year = a.Year
        self.BasePolicy = a.BasePolicy
        self.score = score
        self.reason = reason

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

    def set_score(self, value):
        self.score = value

    def add_reason(self, value):
        self.reason += str(value) + "\n"

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
        dic["Risk Score"] = self.score
        dic["Risk Score Factors"] = self.reason
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
        lis.append(self.score)
        lis.append(self.reason)

        return lis

    def __eq__(self, other):
        if (isinstance(other, Result)):
            return self.Month == other.Month and \
                   self.WeekOfMonth == other.WeekOfMonth and \
                   self.DayOfWeek == other.DayOfWeek and \
                   self.Make == other.Make and \
                   self.AccidentArea == other.AccidentArea and \
                   self.DayOfWeekClaimed == other.DayOfWeekClaimed and \
                   self.MonthClaimed == other.MonthClaimed and \
                   self.WeekOfMonthClaimed == other.WeekOfMonthClaimed and \
                   self.Sex == other.Sex and \
                   self.MaritalStatus == other.MaritalStatus and \
                   self.Age == other.Age and \
                   self.Fault == other.Fault and \
                   self.PolicyType == other.PolicyType and \
                   self.VehicleCategory == other.VehicleCategory and \
                   self.VehiclePrice == other.VehiclePrice and \
                   self.FraudFound_P == other.FraudFound_P and \
                   self.PolicyNumber == other.PolicyNumber and \
                   self.RepNumber == other.RepNumber and \
                   self.Deductible == other.Deductible and \
                   self.DriverRating == other.DriverRating and \
                   self.Days_Policy_Accident == other.Days_Policy_Accident and \
                   self.Days_Policy_Claim == other.Days_Policy_Claim and \
                   self.PastNumberOfClaims == other.PastNumberOfClaims and \
                   self.AgeOfVehicle == other.AgeOfVehicle and \
                   self.AgeOfPolicyHolder == other.AgeOfPolicyHolder and \
                   self.PoliceReportFiled == other.PoliceReportFiled and \
                   self.WitnessPresent == other.WitnessPresent and \
                   self.AgentType == other.AgentType and \
                   self.NumberOfSuppliments == other.NumberOfSuppliments and \
                   self.AddressChange_Claim == other.AddressChange_Claim and \
                   self.NumberOfCars == other.NumberOfCars and \
                   self.Year == other.Year and \
                   self.BasePolicy == other.BasePolicy and self.score == other.score and \
                   self.reason == other.reason
        return False


def inspect(dir, dictionary=True):
    claims, fraud_claims, legit_claims = Read.read_csv(dir)
    result_dic = {}
    n = 0

    for i in claims:
        score = 0

        WeekOfMonth = int(i.getWeekOfMonth())
        VehiclePrice = int(i.getVehiclePrice())
        Deductible = int(i.getDeductible())
        DriverRating = int(i.getDriverRating())
        Days_Policy_Accident = int(i.getDays_Policy_Accident())
        Days_Policy_Claim = int(i.getDays_Policy_Claim())
        PastNumberOfClaims = int(i.getPastNumberOfClaims())
        AgeOfVehicle = int(i.getAgeOfVehicle())
        AgeOfPolicyHolder = int(i.getAgeOfPolicyHolder())
        NumberOfSuppliments = int(i.getNumberOfSuppliments())
        AddressChange_Claim = float(i.getAddressChange_Claim())
        NumberOfCars = int(i.getNumberOfCars())
        PoliceReportFiled = str(i.getPoliceReportFiled()).replace(" ","")
        WitnessPresent = str(i.getWitnessPresent()).replace(" ","")

        reason = ""

        # Score based on WeekOfMonth
        if WeekOfMonth == 2:
            score += 50
        elif WeekOfMonth == 3:
            score += 40
        elif WeekOfMonth == 1:
            score += 30
        elif WeekOfMonth == 4:
            score += 20
        elif WeekOfMonth == 5:
            score += 10

        # Score based on Vehicle Price
        if 20000 < VehiclePrice < 30000:
            score += 50
        if VehiclePrice > 69000:
            score += 40
        if 30000 < VehiclePrice < 40000:
            score += 30
        if VehiclePrice <= 19000:
            score += 20
        if 40000 < VehiclePrice < 50000:
            score += 10

        # score based on Deductible
        if Deductible == 400:
            score += 50
        if VehiclePrice == 500:
            score += 20
        if VehiclePrice == 700:
            score += 10

        # score based on DriverRating
        if DriverRating == 3:
            score += 50
        if DriverRating == 4:
            score += 40
        if DriverRating == 1:
            score += 20
        if DriverRating == 2:
            score += 10

        # Score based on Days_Policy_Accident
        if Days_Policy_Accident > 30:
            score += 50
        if Days_Policy_Accident == 0:
            score += 70
        if Days_Policy_Accident < 30:
            score += 60

        # Score based on Days_Policy_Claim
        if Days_Policy_Claim > 31:
            score += 50
        if 15 < Days_Policy_Claim < 30:
            score += 60
        if Days_Policy_Claim < 10:
            score += 70

        # Score based on PastNumberOfClaims
        if PastNumberOfClaims == 0:
            score += 50
        if PastNumberOfClaims == 3:
            score += 30
        if PastNumberOfClaims == 1:
            score += 20
        if PastNumberOfClaims == 5:
            score += 10

        # Score based on AgeOfVehicle
        if AgeOfVehicle == 7:
            score += 50
        if AgeOfVehicle == 6:
            score += 40
        if AgeOfVehicle == 8:
            score += 30
        if AgeOfVehicle == 5:
            score += 20
        if AgeOfVehicle == 0 or AgeOfVehicle == 4 or AgeOfVehicle == 3 or AgeOfVehicle == 2:
            score += 10

        # AgeOfPolicyHolder
        if 30 <= AgeOfPolicyHolder < 35:
            score += 50
            reason += "[Claimant age is between 30 to 35]- %d\n" % (50)

        if 35 <= AgeOfPolicyHolder < 40:
            score += 40
            reason += "[Claimant age is between 35 to 40]- %d\n" % (40)

        if 40 <= AgeOfPolicyHolder <= 45:
            score += 30
            reason += "[Claimant age is between 40 to 45]- %d\n" % (30)

        if 50 <= AgeOfPolicyHolder <= 55:
            score += 20
            reason += "[Claimant age is between 50 to 55]- %d\n" % (20)

        if 25 < AgeOfPolicyHolder <= 30:
            score += 10
            reason += "[Claimant age is between 25 to 30]- %d\n" % (10)

        if 18 < AgeOfPolicyHolder <= 17:
            score += 10
            reason += "[Claimant age is between 17 to 18]- %d\n" % (10)
        if AgeOfPolicyHolder > 65:
            score += 10
            reason += "[Claimant age is greater than 65]- %d\n" % (10)
        if 25 < AgeOfPolicyHolder <= 20:
            score += 10
            reason += "[Claimant age is between 20 to 25]- %d\n" % (10)
        if 18 < AgeOfPolicyHolder <= 20:
            score += 10
            reason += "[Claimant age is between 18 to 20]- %d\n" % (10)

        # NumberOfSuppliments
        if NumberOfSuppliments == 0:
            score += 50
        if NumberOfSuppliments == 6:
            score += 40
        if NumberOfSuppliments == 2:
            score += 30
        if NumberOfSuppliments == 4:
            score += 20

        # AddressChange_Claim
        if AddressChange_Claim == 0.0:
            score += 50
        if NumberOfSuppliments == 3.0:
            score += 40
        if NumberOfSuppliments == 5.0:
            score += 30
        if NumberOfSuppliments == 1.0 or NumberOfSuppliments == 0.49:
            score += 10

        # NumberOfCars
        if NumberOfCars == 1:
            score += 50
        if NumberOfCars == 2:
            score += 40
        if NumberOfCars == 4:
            score += 30
        if NumberOfCars == 6:
            score += 10

        # PoliceReport
        if PoliceReportFiled == "No":
            score += 50

        # WitnessPresent
        if WitnessPresent == "No":
            score += 50



        result = Result(i, score, reason)

        result_dic[n] = result
        n += 1

    if dictionary == True:
        res = {}
        for i, j in result_dic.items():
            res[i] = result_dic[i].toDictionary().copy()

        return res
    else:
        res = {}
        for i, j in result_dic.items():
            res[i] = result_dic[i].toList().copy()
        return res


def create_cvs(dir: str):
    dic = inspect(dir,dictionary=False)
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Result')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    name = str(dir.replace("Excel_data/", "").replace(".csv", "").replace(".", ""))
    workbook = xlsxwriter.Workbook('Result/' + name + '.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Month')
    worksheet.write('B1', 'WeekOfMonth')
    worksheet.write('C1', 'DayOfWeek')
    worksheet.write('D1', 'Make')
    worksheet.write('E1', 'AccidentArea')
    worksheet.write('F1', 'DayOfWeekClaimed')
    worksheet.write('G1', 'MonthClaimed')
    worksheet.write('H1', 'WeekOfMonthClaimed')
    worksheet.write('I1', 'Sex')
    worksheet.write('J1', 'MaritalStatus')
    worksheet.write('K1', 'Age')
    worksheet.write('L1', 'Fault')
    worksheet.write('M1', 'PolicyType')
    worksheet.write('N1', 'VehicleCategory')
    worksheet.write('O1', 'VehiclePrice')
    worksheet.write('P1', 'FraudFound_P')
    worksheet.write('Q1', 'PolicyNumber')
    worksheet.write('R1', 'RepNumber')
    worksheet.write('S1', 'Deductible')
    worksheet.write('T1', 'DriverRating')
    worksheet.write('U1', 'Days_Policy_Accident')
    worksheet.write('V1', 'Days_Policy_Claim')
    worksheet.write('W1', 'PastNumberOfClaims')
    worksheet.write('X1', 'AgeOfVehicle')
    worksheet.write('Y1', 'AgeOfPolicyHolder')
    worksheet.write('Z1', 'PoliceReportFiled')
    worksheet.write('AA1', 'WitnessPresent')
    worksheet.write('AB1', 'AgentType')
    worksheet.write('AC1', 'NumberOfSuppliments')
    worksheet.write('AD1', 'AddressChange_Claim')
    worksheet.write('AE1', 'NumberOfCars')
    worksheet.write('AF1', 'Year')
    worksheet.write('AG1', 'BasePolicy')
    worksheet.write('AH1', 'Score')
    worksheet.write('AI1', 'Reason for Score')


    n = 0
    for i, j in dic.items():
        n += 1
        worksheet.write('A' + str(n + 1), j[0])
        worksheet.write('B' + str(n + 1), j[1])
        worksheet.write('C' + str(n + 1), j[2])
        worksheet.write('D' + str(n + 1), j[3])
        worksheet.write('E' + str(n + 1), j[4])
        worksheet.write('F' + str(n + 1), j[5])
        worksheet.write('G' + str(n + 1), j[6])
        worksheet.write('H' + str(n + 1), j[7])
        worksheet.write('I' + str(n + 1), j[8])
        worksheet.write('J' + str(n + 1), j[9])
        worksheet.write('K' + str(n + 1), j[10])
        worksheet.write('L' + str(n + 1), j[11])
        worksheet.write('M' + str(n + 1), j[12])
        worksheet.write('N' + str(n + 1), j[13])
        worksheet.write('O' + str(n + 1), j[14])
        worksheet.write('P' + str(n + 1), j[15])
        worksheet.write('Q' + str(n + 1), j[16])
        worksheet.write('R' + str(n + 1), j[17])
        worksheet.write('S' + str(n + 1), j[18])
        worksheet.write('T' + str(n + 1), j[19])
        worksheet.write('U' + str(n + 1), j[20])
        worksheet.write('V' + str(n + 1), j[21])
        worksheet.write('W' + str(n + 1), j[22])
        worksheet.write('X' + str(n + 1), j[23])
        worksheet.write('Y' + str(n + 1), j[24])
        worksheet.write('Z' + str(n + 1), j[25])
        worksheet.write('AA' + str(n + 1), j[26])
        worksheet.write('AB' + str(n + 1), j[27])
        worksheet.write('AC' + str(n + 1), j[28])
        worksheet.write('AD' + str(n + 1), j[29])
        worksheet.write('AE' + str(n + 1), j[30])
        worksheet.write('AF' + str(n + 1), j[31])
        worksheet.write('AG' + str(n + 1), j[32])
        worksheet.write('AH' + str(n + 1), j[33])
        worksheet.write('AI' + str(n + 1), j[34])
    workbook.close()


# pprint.pprint(inspect("Excel_data/1625246842.4975214.csv"))
# 1625571009.4605668.csv

# pprint.pprint(inspect("claims_modified.csv"))
create_cvs("claims_modified.csv")