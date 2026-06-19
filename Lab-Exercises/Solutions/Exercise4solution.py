raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# 1. Writing a loop to clean each string element
for item in raw_survey_inputs:
    # 2. Remove whitespace and force lowercase
    cleaned_item = item.strip().lower()
    
    # 3. Saved it to sanitized_records
    sanitized_records.append(cleaned_item)

# 4. Output both lists to visually verify
print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")