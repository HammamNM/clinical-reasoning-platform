from backend.session import ClinicalSession
from backend.case_loader import CaseLoader


class SessionManager:


    def __init__(
        self
    ):

        self.case_loader = CaseLoader()


        self.sessions = {}



    def create_session(
        self,
        student_id,
        scenario_id,
        case_path
    ):

        session = ClinicalSession()

        session.student_id = student_id

        session.scenario_id = scenario_id


        session.active_case = (
            self.case_loader.load_case(
                case_path
            )
        )


        self.sessions[
            session.session_id
        ] = session


        return session



    def get_session(
        self,
        session_id
    ):

        return self.sessions.get(
            session_id
        )
