from datetime import datetime
import pandas

report_name = "report_validation_%s.csv" % datetime.now().strftime("%d%b%Y%H%M%S")

def main():

    file = "example_pepfar_indicators.csv" #input file name of indicators that needs to be validated
    indicator = "TX_CURR" #type of indicator that needs to be validated. Could be removed if idicator is included in csv

    #reading the input file
    data = pandas.read_csv(file)

    facilities = data.drop_duplicates(subset=['facility_name'])['facility_name']

    match indicator:
        case 'TX_CURR':
            for facility in facilities:
                tx_curr(data.loc[data['facility_name'] == facility], facility)
        case 'TX_NEW':
            for facility in facilities:
                tx_new(data.loc[data['facility_name'] == facility], facility)
        case 'TX_PVLS':
            for facility in facilities:
                tx_pvls(data.loc[data['facility_name'] == facility], facility)
        case 'TX_ML':
            for facility in facilities:
                tx_ml(data.loc[data['facility_name'] == facility], facility)
        case 'TX_RTT':
            for facility in facilities:
                tx_rtt(data.loc[data['facility_name'] == facility], facility)



def report_failure(facility, msg):
    #function to write validation issues
    with open(report_name, "a") as f:
        f.write("%s,%s \n" % (facility, msg))
        f.close()


def tx_curr(data, facility):
    pass
    all_male = data.loc[(data['gender'] == 'Male') & (data['age_category'] == 'All')]['tx_curr'].astype(int).tolist()
    fnp = data.loc[(data['gender'] == 'FNP')]['tx_curr'].astype(int).tolist() 
    fbf = data.loc[(data['gender'] == 'FBF')]['tx_curr'].astype(int).tolist() 
    fp = data.loc[(data['gender'] == 'FP')]['tx_curr'].astype(int).tolist()
    all_clients =data.loc[(data['gender'] == 'FNP')]['tx_curr'].astype(int).tolist() #REPLACE WITH: all_clients =data.loc[(data['gender'] == 'All')]['tx_curr'].astype(int).tolist()

    if not all_clients == (all_male + fnp + fbf + fp):
        report_failure(facility, "All != Male + FNP + FBF + FP")



def tx_new(data, facility):
    pass


def tx_pvls(data, facility):
    pass


def tx_ml(data, facility):
    pass


def tx_rtt(data, facility):
    pass


if __name__ == '__main__':
    main()