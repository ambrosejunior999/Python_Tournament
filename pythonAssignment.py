# defined the partcipants in the tournamnets and stored the participants name and points 
class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0

# defined the events storing the name of the participants and event type
class Event:
    def __init__(self, name, event_type):
        self.name = name
        self.event_type = event_type
        self.participants = []


# method that adds participants   
    def add_participant(self, participant):
        self.participants.append(participant)

# method that adds eachpoints to the participants attribute 
    def assign_points(self, points):
        for participant in self.participants:
            participant.points += points

# defined the tournament
class Tournament:
    def __init__(self):
        self.events = []

# method that appends events to the tournamnets
    def add_event(self, event):
        self.events.append(event)

# method that runs the tournamnets based on the events in progress
    def run_tournament(self):
        for event in self.events:
            print(f" events in progress: {event.name}")
            event.assign_points(event_points[event.name])

# dictionary that stores the points per event type
event_points = {
    "SportingEvent": 10,
    "AcademicEvent": 8,
    "TeamBuildingEvent": 6,
    "CreativeEvent": 7,
    "OtherEvent": 5,
}

# instance of the event class 
sporting_event = Event("SportingEvent", "Team")
academic_event = Event("AcademicEvent", "Individual")
team_building_event = Event("TeamBuildingEvent", "Team")
creative_event = Event("CreativeEvent", "Individual")
other_event = Event("OtherEvent", "Individual")

# creating an object of particapnts. Grtting the participants based on the index
participants = [Participant(f"Participant_{i}") for i in range(1, 21)]

# nested for loop that will add participants to the event
for i in range(0, 20, 5):
    for j in range(5):
        sporting_event.add_participant(participants[i + j])

academic_event.participants = participants[:20]
team_building_event.participants = participants[:5]
creative_event.participants = participants[5:10]
other_event.participants = participants[10:15]

# instances of the tournaments 
tournament = Tournament()
tournament.add_event(sporting_event)
tournament.add_event(academic_event)
tournament.add_event(team_building_event)
tournament.add_event(creative_event)
tournament.add_event(other_event)

# Run the tournament
tournament.run_tournament()

# Display final scores
print("\nFinal Scores:")
for participant in participants:
    print(f"{participant.name}: {participant.points} points")

