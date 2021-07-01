import csv
import Claim

class Result():
    def __init__(self, a, frequency, score):
        # super().__init__(username, d_id, p_id, d_policy, b_id, location, issue, d_incident, d_report, amount, asset)
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
        for i_i, j_j in dic.items():
            if (i > i_i):
                n += 1
                score = 0
                if (j.get_d_id() == j_j.get_d_id() and j.get_username() != j_j.get_username()) or \
                        (j.get_d_id() == j_j.get_d_id() and j.get_p_id() != j_j.get_p_id() or \
                        (j.get_d_id() != j_j.get_d_id() and j.get_p_id() == j_j.get_p_id()) or \
                        (j.get_p_id() == j_j.get_p_id() and j.get_username() != j_j.get_username())):
                    score = 1000



                result = Result(j,duplicate_dictionary[j.get_p_id()], score)
                result_dic[j.get_c_id()] = result.toList()

    return result_dic



# print(read_csv("Excel_data/1625127082.4865746.csv"))
print(inspect("Excel_data/1625127082.4865746.csv"))