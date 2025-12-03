class Console:
    """Console-based UI for interacting with pennguin services."""

    def __init__(self, course_service: CourseService, student_service: StudentService, grade_service: GradeService,
                 reports_service: ReportsService):
        self.__course_service = course_service
        self.__student_service = student_service
        self.__grade_service = grade_service
        self.__reports_service = reports_service
