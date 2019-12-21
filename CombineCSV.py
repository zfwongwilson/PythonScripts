import glob
import pandas as pd

# Identify all csv files in the directory
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all csv files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# Export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
