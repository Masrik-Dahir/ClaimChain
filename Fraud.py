import csv
import Claim
class Claim_block(object):
    def __init__(self, username, d_id, p_id, d_policy, b_id,location,issue, d_incident,d_report,amount,asset):
        self.p_id = p_id
        self.username = username
        self.d_id = d_id
        self.b_id = b_id
        self.d_incident = d_incident
        self.d_policy = d_policy
        self.d_report = d_report
        self.issue = issue
        self.amount = amount
        self.location = location
        self.asset = asset
    def get_username(self):
        return self.username
    def get_p_id(self):
        return self.p_id
    def get_d_id(self):
        return self.d_id
    def get_b_id(self):
        return self.b_id
    def get_d_incident(self):
        return self.d_incident
    def get_d_policy(self):
        return self.d_policy
    def get_d_report(self):
        return self.d_report
    def get_issue(self):
        return self.issue
    def get_amount(self):
        return self.amount
    def get_location(self):
        return self.location
    def get_asset(self):
        return self.asset
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

        return dic

    def toList(self):
        lis = []
        lis.append(self.username)
        lis.append(self.d_id)
        lis.append(self.p_id)
        lis.append(self.d_policy)
        lis.append( self.b_id)
        lis.append(self.location)
        lis.append(self.issue)
        lis.append(self.d_incident)
        lis.append(self.d_report)
        lis.append( self.amount)
        lis.append(self.asset)

        return lis

class Result(Claim_block):
    def __init__(self, Claim_block, frequency, score):
        # super().__init__(username, d_id, p_id, d_policy, b_id, location, issue, d_incident, d_report, amount, asset)
        self.p_id = Claim_block.p_id
        self.username = Claim_block.username
        self.d_id = Claim_block.d_id
        self.b_id = Claim_block.b_id
        self.d_incident = Claim_block.d_incident
        self.d_policy = Claim_block.d_policy
        self.d_report = Claim_block.d_report
        self.issue = Claim_block.issue
        self.amount = Claim_block.amount
        self.location = Claim_block.location
        self.asset = Claim_block.asset
        self.frequency = frequency
        self.score = score

    def set_frequency(self,value):
        self.frequency  = value

    def toList(self):
        lis = []
        lis.append(self.get_username)
        lis.append(self.get_d_id)
        lis.append(self.get_p_id)
        lis.append(self.get_d_policy)
        lis.append(self.get_b_id)
        lis.append(self.get_location)
        lis.append(self.get_issue)
        lis.append(self.get_d_incident)
        lis.append(self.get_d_report)
        lis.append(self.get_amount)
        lis.append(self.get_asset)

        return lis


def lis_double_dictionary(p_id_lis):
    pass


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
        claim_block = Claim.Claim_block(lis[0],lis[1],lis[2],lis[3],lis[4],lis[5],lis[6],lis[7],lis[8],lis[9],lis[10])
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
        for i_i, j_j in dic.items():
            if (i > i_i):
                n += 1
                score = 0
                if (j.get_d_id() == j_j.get_d_id() and j.username != j_j.username) or \
                        (j.get_d_id() == j_j.get_d_id() and j.get_d_policy != j_j.get_d_policy) or \
                        (j.get_d_id() != j_j.get_d_id() and j.get_d_policy == j_j.get_d_policy) or \
                        (j.get_d_policy() == j_j.get_d_policy() and j.username != j_j.username):
                    score = 1000


                # elif ()
                # result = Result(j.get_username(),j.get_d_id(), j.get_p_id(),j.get_d_policy(),j.get_b_id(),j.get_location(),j.get_issue(),
                #                 j.get_d_incident(),j.get_d_report(),j.get_amount(),j.get_asset(),duplicate_dictionary[j.get_p_id()], score)
                result = Result(j,duplicate_dictionary[j.get_p_id()], score)
                print(result.toList())
                result_dic[j.get_p_id(),n] = result.toList()

    return result_dic



print(read_csv("Excel_data/1625118342.40798.csv"))
inspect("Excel_data/1625118342.40798.csv")