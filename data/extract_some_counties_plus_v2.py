import pandas as pd



# ==============================
# BEGIN: Define inputs for the script

# list_desired_counties_names = ['LA', 'MS', 'AL', 'FL', 'TX']
list_desired_counties_names = ['LA'];
output_dir_name = 'LA_plus';

# END: Define inputs for the script
# ==============================


df_counties = pd.read_csv('./data/migration_v2/origin/CountyName_MSAName.csv')


county_filter = df_counties['state'].map(lambda x: x in list_desired_counties_names)
df_desired_counties = df_counties[county_filter]
fipscounty = set(list(df_desired_counties.fipscounty))

data_df = pd.DataFrame()
print('Data contains %s counties' % len(fipscounty))
for item in range(1990, 2011):
    file_name = 'IRS_Migration_Matrix_%d.csv' % item
    file_path = './data/migration_v2/%s' % file_name
    df = pd.read_csv(file_path)
    del df['Unnamed: 0']
    df.columns = [int(item) for item in df.columns]
    assert df.shape[1] == len(set(df.index))

    mask_pos = [col in fipscounty for col in df.columns]
    mask_neg = [not col for col in mask_pos]
    if (sum(mask_pos) != len(fipscounty)):
        print('Only extract %d counties out of %d ' % (sum(mask_pos), len(fipscounty)))

    df_derived = df.loc[mask_pos, mask_pos]
    df_derived[-1] = df.loc[mask_pos, mask_neg].sum(axis=1)
    df_derived.loc[-1, :] = df.loc[mask_neg, mask_pos].sum(axis=0)

    path_to_output = './data/migration_v2/%s/%s' % (output_dir_name, file_name)
    df_derived.to_csv(path_to_output)
    print('Save %s' % path_to_output)

