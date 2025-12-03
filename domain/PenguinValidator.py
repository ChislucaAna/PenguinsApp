from domain.Penguin import Penguin
from datetime import date

class PenguinValidator:
    """
    Ensures each row from our dataset is appropriate for our scope:
    validates based on general criteria = the values given are of correct type
    (making sure that adding additional rows to the dataset
    doesn't result in value errors) and specific criteria(as required in task1)
    """

    @staticmethod
    def validate_fields(study_name,sample_number,species,region,island,stage,individual,clutch_completion,
            date_egg,culmen_length,culmen_depth,flipper_length,body_mass,sex,delta_15_n,delta_13_c,comments):
        """
        Validates and converts all inputs (strings) to their proper types.
        USED WHEN WE READ DATA FROM FILE
        Raises ValueError if any field has an incorrect type.
        Returns converted values in correct order.
        """

        # int fields
        try:
            sample_number = int(sample_number)
        except ValueError:
            raise ValueError("sample_number must be an integer")

        try:
            flipper_length = int(flipper_length)
        except ValueError:
            raise ValueError("flipper_length must be an integer")

        try:
            body_mass = int(body_mass)
        except ValueError:
            raise ValueError("body_mass must be an integer")

        # float fields
        try:
            culmen_length = float(culmen_length)
        except ValueError:
            raise ValueError("culmen_length must be a float")

        try:
            culmen_depth = float(culmen_depth)
        except ValueError:
            raise ValueError("culmen_depth must be a float")

        try:
            delta_15_n = float(delta_15_n)
        except ValueError:
            raise ValueError("delta_15_n must be a float")

        try:
            delta_13_c = float(delta_13_c)
        except ValueError:
            raise ValueError("delta_13_c must be a float")

        # date field (YYYY-MM-DD)
        try:
            y, m, d = map(int, date_egg.split("-"))
            date_egg = date(y, m, d)
        except Exception:
            raise ValueError("date_egg must be a valid date in 'YYYY-MM-DD' format")

        # all other fields remain strings (no validation needed)
        return Penguin(study_name,sample_number,species,region,island,stage,individual,clutch_completion,
            date_egg,culmen_length,culmen_depth,flipper_length,body_mass,sex,delta_15_n,delta_13_c,comments
        )

    @staticmethod
    def validate_special_fields(penguin: Penguin):
        """
        Validates the 7 mandatory fields used for saving.
        Raises ValueError if any of the fields is None or empty.
        """

        required_fields = {
            "species": penguin.species,
            "flipper_length": penguin.flipper_length,
            "culmen_length": penguin.culmen_length,
            "culmen_depth": penguin.culmen_depth,
            "body_mass": penguin.body_mass,
            "island": penguin.island,
            "sex": penguin.sex
        }

        for field_name, value in required_fields.items():
            if value is None or value == "":
                raise ValueError(f"Missing required field: {field_name}")
