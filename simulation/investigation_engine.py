from kernel.events import ReasoningEvent

class InvestigationEngine:

def process_event(  
    self,  
    event,  
    session  
):  

    if event.event_type != "ACTION":  

        return None  


    investigations = (  
        session.active_case.get(  
            "investigations",  
            {}  
        )  
    )  


    action = event.payload.get(  
        "action"  
    )  


    if action not in investigations:  

        return None  


    result = investigations[action]  


    return ReasoningEvent(  

        event_type="INVESTIGATION_RESULT",  

        payload={  

            "action": action,  

            "result": result  

        },  

        source="INVESTIGATION_ENGINE"  

    )
