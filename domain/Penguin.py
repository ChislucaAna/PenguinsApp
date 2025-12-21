class Penguin:
    def __init__(
        self,
        study_name,
        sample_number,
        species,
        region,
        island,
        stage,
        individual_id,
        clutch_completion,
        date_egg,
        culmen_length_mm,
        culmen_depth_mm,
        flipper_length_mm,
        body_mass_g,
        sex,
        delta_15_n,
        delta_13_c,
        comments,
    ):
        self.__study_name = study_name
        self.__sample_number = sample_number
        self.__species = species
        self.__region = region
        self.__island = island
        self.__stage = stage
        self.__individual_id = individual_id
        self.__clutch_completion = clutch_completion
        self.__date_egg = date_egg
        self.__culmen_length_mm = culmen_length_mm
        self.__culmen_depth_mm = culmen_depth_mm
        self.__flipper_length_mm = flipper_length_mm
        self.__body_mass_g = body_mass_g
        self.__sex = sex
        self.__delta_15_n = delta_15_n
        self.__delta_13_c = delta_13_c
        self.__comments = comments

    @property
    def study_name(self):
        return self.__study_name

    @property
    def sample_number(self):
        return self.__sample_number

    @property
    def species(self):
        return self.__species

    @property
    def region(self):
        return self.__region

    @property
    def island(self):
        return self.__island

    @property
    def stage(self):
        return self.__stage

    @property
    def individual_id(self):
        return self.__individual_id

    @property
    def clutch_completion(self):
        return self.__clutch_completion

    @property
    def date_egg(self):
        return self.__date_egg

    @property
    def culmen_length_mm(self):
        return self.__culmen_length_mm

    @property
    def culmen_depth_mm(self):
        return self.__culmen_depth_mm

    @property
    def flipper_length_mm(self):
        return self.__flipper_length_mm

    @property
    def body_mass_g(self):
        return self.__body_mass_g

    @property
    def sex(self):
        return self.__sex

    @property
    def delta_15_n(self):
        return self.__delta_15_n

    @property
    def delta_13_c(self):
        return self.__delta_13_c

    @property
    def comments(self):
        return self.__comments
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("study_name"),
            data.get("sample_number"),
            data.get("species"),
            data.get("region"),
            data.get("island"),
            data.get("stage"),
            data.get("individual_id"),
            data.get("clutch_completion"),
            data.get("date_egg"),
            data.get("culmen_length_mm"),
            data.get("culmen_depth_mm"),
            data.get("flipper_length_mm"),
            data.get("body_mass_g"),
            data.get("sex"),
            data.get("delta_15_n"),
            data.get("delta_13_c"),
            data.get("comments"),
        )
    
    def __repr__(self):
        return (
            "Penguin("
            f"study_name={self.study_name!r}, "
            f"sample_number={self.sample_number!r}, "
            f"species={self.species!r}, "
            f"region={self.region!r}, "
            f"island={self.island!r}, "
            f"stage={self.stage!r}, "
            f"individual_id={self.individual_id!r}, "
            f"clutch_completion={self.clutch_completion!r}, "
            f"date_egg={self.date_egg!r}, "
            f"culmen_length_mm={self.culmen_length_mm!r}, "
            f"culmen_depth_mm={self.culmen_depth_mm!r}, "
            f"flipper_length_mm={self.flipper_length_mm!r}, "
            f"body_mass_g={self.body_mass_g!r}, "
            f"sex={self.sex!r}, "
            f"delta_15_n={self.delta_15_n!r}, "
            f"delta_13_c={self.delta_13_c!r}, "
            f"comments={self.comments!r}"
            ")"
        )