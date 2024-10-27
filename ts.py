import random
from collections import defaultdict

# Constants
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
time_slots = ["9:00-10:30", "10:30-12:00", "2:00-3:30", "3:30-5:00"]
rooms = ["R1", "R2", "R3", "R4", "R5"]

# Generate courses and teachers
courses = [f"C{i + 1}" for i in range(45)]
teachers = [f"T{i + 1}" for i in range(10)]
teacher_courses = defaultdict(list)

# Randomly assign teachers to courses (some teachers can teach multiple courses)
for course in courses:
    assigned_teacher = random.choice(teachers)
    teacher_courses[assigned_teacher].append(course)

# Initial state of the timetable (empty)
timetable = {room: {day: {slot: None for slot in time_slots} for day in days} for room in rooms}

# Function to check if a teacher is free at a given time slot
def is_teacher_free(timetable, teacher, day, time_slot):
    for room in rooms:
        if timetable[room][day][time_slot] and timetable[room][day][time_slot][1] == teacher:
            return False
    return True

# Function to check if the room is free at a given time slot
def is_room_free(timetable, room, day, time_slot):
    return timetable[room][day][time_slot] is None

# Function to check if we can assign a course to a time slot in a specific room
def can_assign(timetable, course, teacher, room, day, time_slot):
    return is_room_free(timetable, room, day, time_slot) and is_teacher_free(timetable, teacher, day, time_slot)

# Define a state as a tuple of (current timetable, course count)
class State:
    def __init__(self, timetable, course_count):
        self.timetable = timetable
        self.course_count = course_count

    def is_goal(self):
        return all(count == 2 for count in self.course_count.values())

# Generate initial state
initial_state = State(timetable, {course: 0 for course in courses})

# State space search using backtracking
def backtrack(state):
    if state.is_goal():
        return state

    # Select a course that has not yet been assigned twice
    random_course = random.choice([course for course in courses if state.course_count[course] < 2])
    teacher = [t for t, cs in teacher_courses.items() if random_course in cs][0]

    # Shuffle days for randomness
    random_days = days[:]
    random.shuffle(random_days)
    
    for day in random_days:
        # Shuffle time slots for randomness
        random_time_slots = time_slots[:]
        random.shuffle(random_time_slots)
        
        for time_slot in random_time_slots:
            # Shuffle rooms for randomness
            random_rooms = rooms[:]
            random.shuffle(random_rooms)
            
            for room in random_rooms:
                if can_assign(state.timetable, random_course, teacher, room, day, time_slot):
                    # Create a new timetable state
                    new_timetable = {r: {d: state.timetable[r][d].copy() for d in days} for r in rooms}
                    new_timetable[room][day][time_slot] = (random_course, teacher)

                    # Update course count
                    new_course_count = state.course_count.copy()
                    new_course_count[random_course] += 1

                    # Create new state
                    new_state = State(new_timetable, new_course_count)

                    # Recursively try to assign remaining courses
                    result = backtrack(new_state)
                    if result:
                        return result  # Found a valid timetable

    return None  # No valid timetable found

# Execute the search
final_state = backtrack(initial_state)

# Display the timetable if successful
if final_state:
    print("Timetable successfully created!")
    timetable = final_state.timetable

    # Display the timetable
    print("Timetable (Courses with Teachers):\n")
    print(f"{'Time Slots':<15}", end=" ")
    for room in rooms:
        print(f"{room:<15}", end=" ")
    print()

    for day in days:
        for slot in time_slots:
            print(f"{day}_{slot:<15}", end=" ")
            for room in rooms:
                if timetable[room][day][slot]:
                    course, teacher = timetable[room][day][slot]
                    print(f"{course} ({teacher})".ljust(15), end=" ")
                else:
                    print("-".ljust(15), end=" ")
            print()
        print()

    # Output the course-teacher mapping
    print("\nCourse-Teacher Assignments:\n")
    for teacher, courses in teacher_courses.items():
        print(f"{teacher}: {', '.join(courses)}")
else:
    print("Failed to create a valid timetable.")
