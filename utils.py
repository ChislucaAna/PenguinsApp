DEFAULT_FIELDS = [
    "study_name",
    "sample_number",
    "species",
    "region",
    "island",
    "stage",
    "individual_id",
    "clutch_completion",
    "date_egg",
    "culmen_length_mm",
    "culmen_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "sex",
    "delta_15_n",
    "delta_13_c",
    "comments",
]

CSV_TO_PENGUIN_FIELD_MAP = {
    "studyName": "study_name",
    "Sample Number": "sample_number",
    "Species": "species",
    "Region": "region",
    "Island": "island",
    "Stage": "stage",
    "Individual ID": "individual_id",
    "Clutch Completion": "clutch_completion",
    "Date Egg": "date_egg",
    "Culmen Length (mm)": "culmen_length_mm",
    "Culmen Depth (mm)": "culmen_depth_mm",
    "Flipper Length (mm)": "flipper_length_mm",
    "Body Mass (g)": "body_mass_g",
    "Sex": "sex",
    "Delta 15 N (o/oo)": "delta_15_n",
    "Delta 13 C (o/oo)": "delta_13_c",
    "Comments": "comments",
}

def str_to_bool(value):
    return value.lower() == "true"
