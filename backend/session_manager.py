from backend.session import ClinicalSession


class SessionManager:

    def __init__(self):

        self.sessions = {}


    def create_session(
        self,
        student_id,
        scenario_id
    ):

        session = ClinicalSession(
            student_id=student_id,
            scenario_id=scenario_id
        )

        self.sessions[
            session.session_id
        ] = session

        return session


    def get_session(
        self,
        session_id
    ):

        return self.sessions.get(session_id)
