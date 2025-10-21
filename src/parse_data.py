import pyreadstat


# Minimal essential columns
columns = [
    'CNT', 'IMMIG', 'ESCS', 'LANGN',
    'PV1READ', 'PV1MATH', 'PV1SCIE',
    'ST004D01T', 'PAREDINT'
]

# Expanded column list
columns_expanded = [
    # IDs and basic info
    'CNT',
    
    # Migration variables
    'IMMIG',         # Immigration status (KEY!)
    'LANGN',         # Language at home
    
    # SES variables
    'ESCS',          # Economic, Social, Cultural Status (KEY!)
    'HISEI',         # Highest parental occupational status
    'PAREDINT',      # Parental education in years
    'HOMEPOS',       # Home possessions
    'ICTRES',        # ICT resources
    
    # Demographic
    'ST004D01T',     # Gender
    
    # Education background
    'DURECEC',       # Duration in early childhood education
    'REPEAT',        # Ever repeated a grade

    # School quality variables
    'RELATST',       # Quality of student-teacher relationships
    'BELONG',        # Sense of belonging (WLE)
    'COOPAGR',       # Cooperation (agreement) (WLE)
    'DISCLIM',       # Disciplinary climate in mathematics (WLE)
    #'CURSUPP',       # Current parental/guardian Support (WLE)
    'PARINVOL',      # Parental Involvement (WLE)
    
    # PISA Performance Scores
    'PV1READ',       # Reading score
    'PV1MATH',       # Mathematics score
    'PV1SCIE',       # Science score
]

print("Reading SPSS file with expanded columns...")
sav_df, meta = pyreadstat.read_sav(
    '../data/raw/CY08MSP_STU_QQQ.SAV',
    usecols=columns_expanded
)


 # Filter Germany
df_germany = sav_df[sav_df['CNT'] == 'DEU'].copy()
print(f"Germany students: {len(df_germany)}")

# Save
df_germany.to_csv('../data/raw/pisa_expanded_germany_STU_QQQ.csv')
print("Saved expanded Germany PISA data.")