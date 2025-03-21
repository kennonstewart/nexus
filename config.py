# constants.py

# FILE PATHS
DATA_FILE_PATH = "/workspaces/nexus/data/world/csv/world_migration_time_{YEAR}.csv"
DICTIONARY_PATH = "/workspaces/nexus/data/world/csv/world_dictionary.csv"

# TIME PERIODS
YEARS = ["1990", "1995", "2000", "2005", "2010"]

# column name mappings
COLUMN_MAPPINGS = {
    "Country_name": "country",
    "Official state name": "state_name",
    "Sovereignty": "sovereign",
    "Alpha-2 code": "country_code_2",
    "Alpha-3 code": "country_code_3",
    "Numeric code":"numeric_code",
    "Subdivision code links":"subdivision",
    "Internet ccTLD":"internet",
    "Unnamed: 0": "source"
}


