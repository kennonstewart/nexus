# Extract specifiec area and put the remainder into 1 extra node
import pandas as pd

df_counties = pd.read_csv('./county_migration_counts/CountyName_MSAName.csv')
# list_desired_counties_names = ['LA', 'MS', 'AL', 'FL', 'TX']
list_desired_counties_names = ['LA']
county_filter = df_counties['state'].map(lambda x: x in list_desired_counties_names)
df_desired_counties = df_counties[county_filter]
fipscounty = set(list(df_desired_counties.fipscounty))

data_df = pd.DataFrame()
print('Data contains %s counties' % len(fipscounty))
for item in range(1, 19):
    file_name = 'county_time_%s.csv' % item
    file_path = './county_migration_counts/%s' % file_name
    df = pd.read_csv(file_path)
    del df['Unnamed: 0']
    df.columns = [int(item) for item in df.columns]
    assert df.shape[1] == len(set(df.index))

    desired_indices = [col in fipscounty for col in df.columns]
    remaining_indices = [not col for col in desired_indices]
    if (sum(desired_indices) != len(fipscounty)):
        print('Only extract %s counties' % sum(desired_indices))

    df_derived = df.loc[desired_indices, desired_indices]
    df_derived[-1] = df.loc[desired_indices, remaining_indices].sum(axis=1)
    df_derived.loc[-1, :] = df.loc[remaining_indices, desired_indices].sum(axis=0)
    df_derived.to_csv('./county_migration_counts/LA_extra/%s' % file_name)
    print('Save %s' % file_name)
    print()

