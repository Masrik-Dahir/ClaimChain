import csv
import Claim
from datetime import datetime
import holidays
import pprint


class Result():
    def __init__(self, a, frequency, score):
        self.p_id = a.get_p_id()
        self.username = a.get_username()
        self.d_id = a.get_d_id()
        self.b_id = a.get_b_id()
        self.d_incident = a.get_d_incident()
        self.d_policy = a.get_d_policy()
        self.d_report = a.get_d_report()
        self.issue = a.get_issue()
        self.amount = a.get_amount()
        self.location = a.get_location()
        self.asset = a.get_asset()
        self.c_id = a.get_c_id()
        self.frequency = frequency
        self.score = score

    def set_frequency(self,value):
        self.frequency  = value

    def toList(self):
        lis = []
        lis.append(self.username)
        lis.append(self.d_id)
        lis.append(self.p_id)
        lis.append(self.d_policy)
        lis.append(self.b_id)
        lis.append(self.location)
        lis.append(self.issue)
        lis.append(self.d_incident)
        lis.append(self.d_report)
        lis.append(self.amount)
        lis.append(self.asset)
        lis.append(self.c_id)
        lis.append(self.frequency)
        lis.append(self.score)

        return lis
    def toDictionary(self):
        dic = {}
        dic["Username"] = self.username
        dic["Driver ID"] = self.d_id
        dic["Policy ID"] = self.p_id
        dic["Date of Policy"] = self.d_policy
        dic["Block ID"] = self.b_id
        dic["Location"] = self.location
        dic["Reason for Claim"] = self.issue
        dic["Date of Incident"] = self.d_incident
        dic["Date of Report"] = self.d_report
        dic["Claimed mount"] = self.amount
        dic["Insured Asset Value"] = self.asset
        dic["Claim ID"] = self.c_id
        dic["Frequency"] = self.frequency
        dic["Score"] = self.score

        return dic

    def days_between(self):
        d1 = datetime.strptime(str(self.d_policy).replace("/","-"), "%m-%d-%Y")
        d2 = datetime.strptime(str(self.d_incident).replace("/","-"), "%m-%d-%Y")
        return abs((d2 - d1).days)


def read_csv(dir):
    # csv file name
    filename = dir

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    #  printing first 5 rows
    print('\nFirst %d rows are:\n'%(csvreader.line_num))

    dic = {}
    n = 1
    p_id_lis = []
    for row in rows[:]:
        # parsing each column of a row
        lis = []
        for col in row:
            # print("%10s" % col)
            lis.append(col)
        p_id_lis.append(lis[2])
        claim_block = Claim.Claim_block(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],lis[10],lis[12])
        # result = Result(claim_block,frequency=0,score=0)
        dic[n] = claim_block
        n += 1
        # print('\n')
    duplicate_dictionary = lis_duplicate_dictionary(p_id_lis)

    return dic, duplicate_dictionary

def lis_duplicate_dictionary(lis):
    return {i:lis.count(i) for i in lis}


def inspect(dir):
    dic, duplicate_dictionary = read_csv(dir)
    result_dic = {}
    n = 0

    for i,j in dic.items():
        score = 0
        # for i_i, j_j in dic.items():
        #     if (i > i_i):
        #         n += 1
        #         score = 0
        #         if (j.get_d_id() == j_j.get_d_id() and j.get_username() != j_j.get_username()) or \
        #                 (j.get_d_id() == j_j.get_d_id() and j.get_p_id() != j_j.get_p_id() or \
        #                 (j.get_d_id() != j_j.get_d_id() and j.get_p_id() == j_j.get_p_id()) or \
        #                 (j.get_p_id() == j_j.get_p_id() and j.get_username() != j_j.get_username())):
        #             score = 1000
        frequnecy = int(days_between(j)/duplicate_dictionary[j.get_p_id()])
        diff_in_report = days_between(a=j.get_d_incident(), b=j.get_d_report())
        diff_in_holidays = int(days_berween_holidays(date_of_incident=str(j.d_incident)))
        diff_in_claim_from_policy_holding_date = days_between(a=j.get_d_policy(),b=j.get_d_incident())
        claim_times_more_than_liability = int(j.get_amount())/int(j.get_asset())

        # Score based on how much they claim
        if (frequnecy <= 100 and frequnecy >= 50):
            score += 50
        elif (frequnecy < 50 and frequnecy >= 30):
            score += 200
        elif (frequnecy < 30 and frequnecy > 10):
            score += 400


        # difference in incident and report
        if (diff_in_report <= 7):
            score += 50
        elif (diff_in_report <= 30 and diff_in_report > 7):
            score += 150
        elif (diff_in_report <= 120 and diff_in_report > 30):
            score += 350
        elif (diff_in_report <= 365 and diff_in_report > 120):
            score += 500

        # Reporting close to holidays
        if(diff_in_holidays <= 7):
            score += 300
        elif (diff_in_holidays <= 14 and diff_in_holidays > 7):
            score += 150

        # Reporting in first 10 days of holding policy
        if (diff_in_claim_from_policy_holding_date <= 10):
            score += 700

        # If the claim is more than liability
        if (claim_times_more_than_liability > 1 and claim_times_more_than_liability < 1.5):
            score += 200

        if (claim_times_more_than_liability > 1.5 and claim_times_more_than_liability <= 2):
            score += 250

        if (claim_times_more_than_liability > 2 and claim_times_more_than_liability <= 2.5):
            score += 300

        if (claim_times_more_than_liability > 2.5 and claim_times_more_than_liability <= 3):
            score += 350

        if (claim_times_more_than_liability > 3):
            score += 500



        result = Result(j,frequnecy, score)
        result_dic[j.get_c_id()] = result.toDictionary()

    return result_dic


def days_between(cliam_object=None,a=None,b=None):

    if (a == None and b == None and isinstance(cliam_object,Claim.Claim_block)):
        d1 = datetime.strptime(str(cliam_object.get_d_policy()).replace("/", "-"), "%m-%d-%Y")
        d2 = datetime.strptime(str(cliam_object.get_d_incident()).replace("/", "-"), "%m-%d-%Y")
        return abs((d2 - d1).days)
    elif (isinstance(a, str) and isinstance(b, str) and cliam_object == None):
        if "/" in str(a):
            d1 = datetime.strptime(str(a).replace("/", "-"), "%m-%d-%Y")
        else:
            d1 = datetime.strptime(a, "%Y-%m-%d")
        if "/" in str(b):
            d2 = datetime.strptime(str(b).replace("/", "-"), "%m-%d-%Y")
        else:
            d2 = datetime.strptime(b, "%Y-%m-%d")
        return abs((d2 - d1).days)
    else:
        return None

def days_berween_holidays(date_of_incident, country = "UnitedStates"):
    year = str(datetime.today().year)
    if ("-" in date_of_incident):
        ls = date_of_incident.split("-")
        year = int(ls[0])
    elif ("/" in date_of_incident):
        ls = date_of_incident.split("/")
        year = int(ls[2])

    # Select country
    us_holidays = holidays.UnitedStates()
    holi = []
    # Print all the holidays in UnitedKingdom in year 2018
    for i,j in holidays.UnitedStates(years=year).items():
        holi.append(str(i))

    shotest_defference = 365
    for i in holi:
        diff = int(days_between(a = str(date_of_incident),b = i))
        if shotest_defference > diff:
            shotest_defference = diff

    return shotest_defference

# pprint.pprint(inspect("Excel_data/1625127082.4865746.csv"))
# print(days_berween_holidays(date_of_incident = "2021-12-17"))