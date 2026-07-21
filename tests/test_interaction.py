from backend.interaction_engine import InteractionEngine


engine = InteractionEngine("cases/case_001.json")

stage = engine.show_stage(1)

choice = input("\nType your choice exactly:\n")

engine.record_choice(choice)

engine.show_events()
