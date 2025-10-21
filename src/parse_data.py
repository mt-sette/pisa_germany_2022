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
    'CNT', 'CNTSCHID', 'CNTSTUID',
    
    # Migration variables
    'IMMIG',         # Immigration status (KEY!)
    'LANGN',         # Language at home
    'ST021Q01TA',    # Country of birth - student
    'ST022Q01TA',    # Country of birth - mother
    'ST022Q02TA',    # Country of birth - father
    
    # SES variables
    'ESCS',          # Economic, Social, Cultural Status (KEY!)
    'HISEI',         # Highest parental occupational status
    'PAREDINT',      # Parental education in years
    'HOMEPOS',       # Home possessions
    'WEALTH',        # Family wealth
    'CULTPOSS',      # Cultural possessions
    'HEDRES',        # Home educational resources
    'ICTRES',        # ICT resources
    
    # Demographic
    'ST004D01T',     # Gender
    'AGE',           # Age
    
    # Education background
    'DURECEC',       # Duration in early childhood education
    'REPEAT',        # Ever repeated a grade
    
    # PISA Performance Scores
    'PV1READ',       # Reading score
    'PV1MATH',       # Mathematics score
    'PV1SCIE',       # Science score
    
    # Weights (for proper statistical analysis)
    'W_FSTUWT',      # Final student weight
    
    # Optional: Language learning
    'ST022Q03TA',    # Age when learned test language
]

print("Reading SPSS file with limited columns...")
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