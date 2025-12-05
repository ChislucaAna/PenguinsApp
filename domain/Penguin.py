from datetime import date
class Penguin:
    """
    Holds information from one row of the penguin dataset.
    """

    def __init__(self, study_name=None, sample_number:int=None, species=None, region=None, island=None, stage=None,
                 individual=None, clutch_completion=None, date_egg:date=None, culmen_length:float=None, culmen_depth:float=None,
                 flipper_length:int=None, body_mass:int=None, sex=None, delta_15_n:float=None, delta_13_c:float=None, comments=None):

        self.__study_name = study_name
        self.__sample_number = sample_number
        self.__species = species
        self.__region = region
        self.__island = island
        self.__stage = stage
        self.__individual = individual
        self.__clutch_completion = clutch_completion
        self.__date_egg = date_egg
        self.__culmen_length = culmen_length
        self.__culmen_depth = culmen_depth
        self.__flipper_length = flipper_length
        self.__body_mass = body_mass
        self.__sex = sex
        self.__delta_15_n = delta_15_n
        self.__delta_13_c = delta_13_c
        self.__comments = comments

    # ---------- PROPERTIES ----------

    @property
    def study_name(self):
        return self.__study_name

    @study_name.setter
    def study_name(self, value):
        self.__study_name = value

    @property
    def sample_number(self):
        return self.__sample_number

    @sample_number.setter
    def sample_number(self, value):
        self.__sample_number = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    @property
    def island(self):
        return self.__island

    @island.setter
    def island(self, value):
        self.__island = value

    @property
    def stage(self):
        return self.__stage

    @stage.setter
    def stage(self, value):
        self.__stage = value

    @property
    def individual(self):
        return self.__individual

    @individual.setter
    def individual(self, value):
        self.__individual = value

    @property
    def clutch_completion(self):
        return self.__clutch_completion

    @clutch_completion.setter
    def clutch_completion(self, value):
        self.__clutch_completion = value

    @property
    def date_egg(self):
        return self.__date_egg

    @date_egg.setter
    def date_egg(self, value):
        self.__date_egg = value

    @property
    def culmen_length(self):
        return self.__culmen_length

    @culmen_length.setter
    def culmen_length(self, value):
        self.__culmen_length = value

    @property
    def culmen_depth(self):
        return self.__culmen_depth

    @culmen_depth.setter
    def culmen_depth(self, value):
        self.__culmen_depth = value

    @property
    def flipper_length(self):
        return self.__flipper_length

    @flipper_length.setter
    def flipper_length(self, value):
        self.__flipper_length = value

    @property
    def body_mass(self):
        return self.__body_mass

    @body_mass.setter
    def body_mass(self, value):
        self.__body_mass = value

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @property
    def delta_15_n(self):
        return self.__delta_15_n

    @delta_15_n.setter
    def delta_15_n(self, value):
        self.__delta_15_n = value

    @property
    def delta_13_c(self):
        return self.__delta_13_c

    @delta_13_c.setter
    def delta_13_c(self, value):
        self.__delta_13_c = value

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, value):
        self.__comments = value

    def to_csv_row(self):
        """
        Creates a CSV-ready row (list of fields).
        Returns: list
        """

        return [
            self.study_name,
            self.sample_number,
            self.species,
            self.region,
            self.island,
            self.stage,
            self.individual,
            self.clutch_completion,
            self.date_egg.isoformat() if self.date_egg else "",
            self.culmen_length,
            self.culmen_depth,
            self.flipper_length,
            self.body_mass,
            self.sex,
            self.delta_15_n,
            self.delta_13_c,
            self.comments
        ]

