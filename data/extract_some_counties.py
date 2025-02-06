import pandas as pd

df_counties = pd.read_csv('./data/county_migration_counts/CountyName_MSAName.csv')
# list_desired_counties_names = ['LA', 'MS', 'AL', 'FL', 'TX']
list_desired_counties_names = ['CA'];
county_filter = df_counties['state'].map(lambda x: x in list_desired_counties_names)
df_desired_counties = df_counties[county_filter]
fipscounty = set(list(df_desired_counties.fipscounty))

data_df = pd.DataFrame()
print('Data contains %s counties' % len(fipscounty))
for item in range(1, 19):
    file_name = 'county_time_%s.csv' % item
    file_path = './data/county_migration_counts/%s' % file_name
    df = pd.read_csv(file_path)
    # df.index = df['Unnamed: 0']
    del df['Unnamed: 0']
    df.columns = [int(item) for item in df.columns]
    assert df.shape[1] == len(set(df.index))

    desired_columns = [col in fipscounty for col in df.columns]
    # county_filter = df.index.map(lambda x: x in fipscounty)
    df = df.loc[desired_columns, desired_columns]
    df.to_csv('./data/county_migration_counts/CA/%s' % file_name)
    print('Save %s' % file_name)

