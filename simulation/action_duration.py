class ActionDurationModel:


    DEFAULT_DURATION = 1


    ACTION_DURATIONS = {


        "ORDER_ECG": 2,


        "ORDER_TROPONIN": 5,


        "ORDER_CBC": 10,


        "ORDER_CXR": 15,


        "GIVE_ASPIRIN": 0,


        "GIVE_HEPARIN": 0,


        "WAIT": 10


    }



    def get_duration(
        self,
        action
    ):

        return self.ACTION_DURATIONS.get(

            action,

            self.DEFAULT_DURATION

        )
