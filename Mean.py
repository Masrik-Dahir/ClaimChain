from collections import Counter
import Read

def Average(lst):
    return sum(lst) / len(lst)

def range(lst):
    lst.sort()
    lowest = lst[0]
    highest = lst[len(lst)-1]
    return "%d to %d" %(lowest,highest)

def duplicate(lst):
    dic = Counter(lst)
    return dic

def mean(dir):
    claims, fraud_claims, legit_claims = Read.read_csv(dir)
    WeekOfMonth = []
    VehiclePrice = []
    Deductible = []
    DriverRating = []
    Days_Policy_Accident = []
    Days_Policy_Claim = []
    PastNumberOfClaims = []
    AgeOfVehicle = []
    AgeOfPolicyHolder = []
    NumberOfSuppliments = []
    AddressChange_Claim = []
    NumberOfCars = []

    for i in fraud_claims:
        for key, value in i.toDictionary().items():
            if key == "WeekOfMonth":
                WeekOfMonth.append(int(value))
            if key == "VehiclePrice":
                VehiclePrice.append(int(value))
            if key == "Deductible":
                Deductible.append(int(value))
            if key == "DriverRating":
                DriverRating.append(int(value))
            if key == "Days_Policy_Accident":
                Days_Policy_Accident.append(int(value))
            if key == "Days_Policy_Claim":
                Days_Policy_Claim.append(int(value))
            if key == "PastNumberOfClaims":
                PastNumberOfClaims.append(int(value))
            if key == "AgeOfVehicle":
                AgeOfVehicle.append(int(value))
            if key == "AgeOfPolicyHolder":
                AgeOfPolicyHolder.append(int(value))
            if key == "NumberOfSuppliments":
                NumberOfSuppliments.append(int(value))
            if key == "AddressChange_Claim":
                AddressChange_Claim.append(float(value))
            if key == "NumberOfCars":
                NumberOfCars.append(int(value))
    dic = {}
    dic["WeekOfMonth"] = duplicate(WeekOfMonth)
    dic["VehiclePrice"] = duplicate(VehiclePrice)
    dic["Deductible"] = duplicate(Deductible)
    dic["DriverRating"] = duplicate(DriverRating)
    dic["Days_Policy_Accident"] = duplicate(Days_Policy_Accident)
    dic["Days_Policy_Claim"] = duplicate(Days_Policy_Claim)
    dic["PastNumberOfClaims"] = duplicate(PastNumberOfClaims)
    dic["AgeOfVehicle"] = duplicate(AgeOfVehicle)
    dic["AgeOfPolicyHolder"] = duplicate(AgeOfPolicyHolder)
    dic["NumberOfSuppliments"] = duplicate(NumberOfSuppliments)
    dic["AddressChange_Claim"] = duplicate(AddressChange_Claim)
    dic["NumberOfCars"] = duplicate(NumberOfCars)




    return dic

print(mean("claims_modified.csv"))