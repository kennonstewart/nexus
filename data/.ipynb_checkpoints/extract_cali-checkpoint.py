import pandas as pd

counties = pd.read_csv('./data/county_migration_counts/CountyName_MSAName.csv')

counties_CA = counties[counties['state'] == 'CA']
fipscounty_CA = set(counties_CA.fipscounty)

data_df = pd.DataFrame()
print('CA contains %s counties' % len(fipscounty_CA))
for item in range(1, 19):
    file_name = 'county_time_%s.csv' % item
    file_path = './data/county_migration_counts/%s' % file_name
    df = pd.read_csv(file_path)
    df.index = df['Unnamed: 0']
    del df['Unnamed: 0']
    df.columns = [int(item) for item in df.columns]
    assert len(set(df.index).difference(set(df.columns))) == 0
    assert df.shape[1] == len(set(df.index))


    all_counties = set(df.index)
    missing_counties = set(fipscounty_CA).difference(all_counties)
    if len(missing_counties) > 0:
        print('Missing counties: ', missing_counties)
        fipscounty_CA = fipscounty_CA.intersection(all_counties)
        print('CA now contain %s counties' % len (fipscounty_CA))

    df = df.loc[list(fipscounty_CA), :]
    df.to_csv('./data/county_migration_counts/CA_out/%s' % file_name)
    print('Save %s' % file_name)

