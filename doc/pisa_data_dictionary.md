# PISA 2022 Germany Dataset - Data Dictionary

## Overview
This dataset contains student-level data from the PISA 2022 assessment for Germany, focusing on socioeconomic background, migration status, language, and academic achievement.

**Sample Size:** ~6,000-7,000 German students  
**Source:** OECD PISA 2022 Student Questionnaire  
**Country:** Germany (DEU)

---

## Variable Descriptions

### 1. CNT - Country Code
**Type:** Categorical (String)  
**Description:** Three-letter country code identifying the country where the student was assessed.

**Values:**
- `DEU` = Germany (all rows should have this value in your filtered dataset)

**Usage:** Identifier variable. Used for filtering/verification but not for analysis.

---

### 2. ST004D01T - Gender
**Type:** Categorical (Integer)  
**Description:** Student's self-reported gender.

**Values:**
- `1` = Female
- `2` = Male
- `NaN` = Missing/Not reported

**Usage:** Control variable for demographic analysis. Gender gaps in achievement are well-documented in education research.

**Analysis Note:** Check for gender differences in achievement scores and whether SES/migration effects differ by gender.

---

### 3. IMMIG - Immigration Status
**Type:** Categorical (Integer)  
**Description:** Student's immigration/migration background based on country of birth (student and parents).

**Values:**
- `1` = **Native students** (student and both parents born in the country of assessment)
- `2` = **Second-generation immigrants** (student born in country, but at least one parent born abroad)
- `3` = **First-generation immigrants** (student born abroad)
- `NaN` = Missing

**Usage:** **KEY VARIABLE for your research question.** This distinguishes between students with and without migration background.

**Analysis Note:** 
- Compare achievement across these three groups
- Interaction with ESCS and LANGN is critical for your research question
- First-generation typically face more challenges than second-generation

**Expected Pattern in Germany:** Native > Second-gen > First-gen (but this gap often disappears when controlling for SES)

---

### 4. LANGN - Language Spoken at Home
**Type:** Categorical (Float)  
**Description:** Whether the language spoken most often at home is the same as the language of the PISA test (German).

**Values:**
- `148` = **Test language spoken at home** (German) => remaped to 1
- `range 100 - 998` = **Other language spoken at home** (not German) => remaped to 2
- `999` = Missing => remaped to 0


**Usage:** **KEY VARIABLE for your research question.** This is your direct measure of language barrier.

**Analysis Note:**
- Students who don't speak German at home typically score lower
- This is partially independent of IMMIG (some natives speak minority languages)
- Critical for isolating "language barrier effect" vs. "migration effect"

**Interpretation:** If achievement gaps persist after controlling for LANGN, it suggests factors beyond language (e.g., discrimination, school resources, cultural capital).

---

### 5. PAREDINT - Parental Education
**Type:** Continuous (Float)  
**Description:** Highest level of parental education in years of schooling. Calculated as the maximum of mother's and father's education converted to years.

**Values:**
- Range: Typically 0-18+ years
- Higher values = more education
- `NaN` = Missing

**Typical Conversions:**
- ~9 years = Lower secondary
- ~12-13 years = Upper secondary/High school
- ~15-16 years = Bachelor's degree
- ~18+ years = Master's/Doctoral degree

**Usage:** Component of SES; measure of family educational background (cultural capital).

**Analysis Note:** Strong predictor of student achievement. Often mediates the relationship between migration status and achievement.

---

### 6. ESCS - Economic, Social and Cultural Status Index
**Type:** Continuous (Float)  
**Description:** **THE PRIMARY SES MEASURE.** A composite index derived from parental education (PAREDINT), parental occupation (HISEI), and home possessions (HOMEPOS). Standardized to have mean=0 and SD=1 across OECD countries.

**Values:**
- Range: Typically -4 to +3 (most students between -2 and +2)
- **Mean ≈ 0** (by design, across all OECD countries)
- **SD ≈ 1** (by design)
- Negative values = Below average SES
- Positive values = Above average SES
- `NaN` = Missing

**Interpretation:**
- ESCS = -2: Very low SES (bottom ~2%)
- ESCS = -1: Below average SES (bottom ~16%)
- ESCS = 0: Average SES
- ESCS = +1: Above average SES (top ~16%)
- ESCS = +2: Very high SES (top ~2%)

**Usage:** **KEY VARIABLE for your research question.** This is your primary measure of socioeconomic disadvantage.

**Analysis Note:** 
- Most powerful predictor of educational achievement in PISA data
- Your research question: Does ESCS or LANGN/IMMIG matter more?
- Check correlation with IMMIG (migrants often have lower ESCS)

---

### 7. PV1MATH - Mathematics Achievement (Plausible Value 1)
**Type:** Continuous (Float)  
**Description:** First plausible value for mathematics proficiency. Represents student's estimated mathematics ability based on their responses to test items.

**Values:**
- Range: Typically 200-800 (mean ≈ 500, SD ≈ 100 for OECD average)
- Higher values = Better performance
- `NaN` = Missing (student didn't take math test)

**PISA Proficiency Levels (approximate):**
- **Below 358:** Below Level 1 (very low)
- **358-420:** Level 1 (basic skills)
- **420-482:** Level 2 (minimum proficiency - baseline)
- **482-545:** Level 3 (moderate proficiency)
- **545-607:** Level 4 (high proficiency)
- **607-669:** Level 5 (very high proficiency)
- **Above 669:** Level 6 (exceptional)

**Usage:** Primary outcome variable for mathematics.

**Note:** This is one of 10 plausible values (PV1-PV10). Using only PV1 is acceptable for student projects but technically ignores measurement uncertainty.

---

### 8. PV1READ - Reading Achievement (Plausible Value 1)
**Type:** Continuous (Float)  
**Description:** First plausible value for reading proficiency. Represents student's estimated reading literacy based on comprehension tasks.

**Values:**
- Range: Typically 200-800 (mean ≈ 500, SD ≈ 100 for OECD average)
- Higher values = Better performance
- `NaN` = Missing

**PISA Proficiency Levels (approximate):**
- **Below 335:** Below Level 1c (very low)
- **335-407:** Level 1c-1a (basic skills)
- **407-480:** Level 2 (baseline proficiency)
- **480-553:** Level 3 (moderate proficiency)
- **553-626:** Level 4 (high proficiency)
- **626-698:** Level 5 (very high proficiency)
- **Above 698:** Level 6 (exceptional)

**Usage:** Primary outcome variable for reading. **Especially relevant for language barrier research** since reading is most affected by language proficiency.

**Analysis Note:** Expected to show the largest gaps between LANGN groups.

---

### 9. PV1SCIE - Science Achievement (Plausible Value 1)
**Type:** Continuous (Float)  
**Description:** First plausible value for science proficiency. Represents student's knowledge and ability to apply scientific concepts.

**Values:**
- Range: Typically 200-800 (mean ≈ 500, SD ≈ 100 for OECD average)
- Higher values = Better performance
- `NaN` = Missing

**PISA Proficiency Levels (approximate):**
- **Below 335:** Below Level 1b (very low)
- **335-410:** Level 1b-1a (basic skills)
- **410-484:** Level 2 (baseline proficiency)
- **484-559:** Level 3 (moderate proficiency)
- **559-633:** Level 4 (high proficiency)
- **633-708:** Level 5 (very high proficiency)
- **Above 708:** Level 6 (exceptional)

**Usage:** Primary outcome variable for science.

---

## Research Question Alignment

### Your Core Question:
**"Do migrant children do worse in school due to language barriers OR is low income (SES) a bigger factor?"**

### Key Variables for Analysis:

**Outcome Variables (Y):**
- `PV1MATH`, `PV1READ`, `PV1SCIE` - What you're trying to predict

**Primary Predictors (X):**
- `ESCS` - Socioeconomic status (income/resource effect)
- `IMMIG` - Migration background (migration effect)
- `LANGN` - Language at home (language barrier effect)

**Control Variables:**
- `ST004D01T` - Gender (known to affect achievement)
- `PAREDINT` - Parental education (alternative SES measure)

### Analysis Strategy:

1. **Descriptive Analysis:**
   - Compare mean achievement by IMMIG groups
   - Compare mean achievement by LANGN groups
   - Compare mean ESCS by IMMIG/LANGN groups

2. **Correlation Analysis:**
   - How correlated are ESCS, IMMIG, and LANGN?
   - Which has the strongest correlation with achievement?

3. **Regression Models:**
   - **Model 1:** Achievement ~ ESCS (SES effect only)
   - **Model 2:** Achievement ~ IMMIG (migration effect only)
   - **Model 3:** Achievement ~ LANGN (language barrier only)
   - **Model 4:** Achievement ~ ESCS + IMMIG + LANGN (all together)
   
   Compare R² and coefficients to see which matters most.

4. **Key Question to Answer:**
   - Does the IMMIG/LANGN achievement gap disappear when controlling for ESCS?
   - If YES → SES is the bigger factor
   - If NO → Language/migration has independent effects beyond SES

---

## Missing Data Considerations

**Expected Missing Data:**
- IMMIG: ~5-10% missing
- LANGN: ~5-10% missing
- ESCS/PAREDINT: ~10-15% missing (some parents don't report education/occupation)
- Achievement scores: <5% missing

**Handling Strategies:**
- Complete case analysis (drop rows with any missing values) - simplest
- Imputation (fill missing values) - more advanced
- Multiple imputation - research-grade (overkill for bootcamp)

**Recommendation for your project:** Start with complete case analysis. Document how many cases you drop.

---

## Data Quality Checks

Before analysis, verify:
```python
# Check value ranges
print(df['IMMIG'].value_counts())  # Should be 1, 2, 3
print(df['LANGN'].value_counts())  # Should be 1, 2
print(df['ST004D01T'].value_counts())  # Should be 1, 2

# Check achievement scores are reasonable
print(df[['PV1MATH', 'PV1READ', 'PV1SCIE']].describe())
# Should be roughly 200-800 range, mean around 500

# Check ESCS distribution
print(df['ESCS'].describe())
# Should be roughly -3 to +3, mean near 0

# Check for impossible values
print((df['PAREDINT'] < 0).sum())  # Should be 0
print((df['PAREDINT'] > 25).sum())  # Should be very few
```

---

## References

- OECD PISA 2022 Technical Report: https://www.oecd.org/pisa/
- PISA 2022 Assessment and Analytical Framework: https://www.oecd.org/pisa/
- Variable codebook: Included in your PISA data download

---

**Last Updated:** October 2025  
**Dataset Version:** PISA 2022 Public Use File  
**Country Focus:** Germany (DEU)