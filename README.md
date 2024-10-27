# CS-367-Project

# Timetable Scheduling System

This project implements a timetable scheduling system using a state-space search algorithm with backtracking to assign courses to teachers in available time slots and rooms. The goal is to generate a timetable where each course is scheduled exactly twice, without overlapping teacher assignments or room conflicts.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [Explanation](#explanation)
- [Algorithm Details](#algorithm-details)
- [Output Example](#output-example)


## Overview
The timetable scheduling system generates a timetable by assigning courses to available rooms and time slots while ensuring that no teacher is double-booked in a single time slot. The code randomly assigns each course a teacher, then uses backtracking to search for a valid scheduling solution.

## Features
- **Random Assignment of Teachers**: Randomly assigns each course a teacher.
- **Flexible Scheduling**: Ensures that each course is scheduled twice in the timetable.
- **Conflict Avoidance**: Prevents scheduling conflicts by checking teacher availability and room occupancy.
- **Backtracking Algorithm**: Uses a backtracking search to explore possible timetable configurations.

## Dependencies
- Python 3.x
- Libraries: `random`, `collections`

## Explanation

### Modules and Constants
- **Modules**:
  - `random`: Used to shuffle days, time slots, and rooms for randomness in scheduling.
  - `defaultdict`: Used to store lists of courses per teacher.
- **Constants**:
  - `days`, `time_slots`, `rooms`: Define the available scheduling slots.
  
### Data Structures
- `courses`: A list of courses from `C1` to `C45`.
- `teachers`: A list of teachers from `T1` to `T10`.
- `teacher_courses`: A dictionary mapping teachers to the courses they teach.
- `timetable`: A nested dictionary representing the schedule, initially empty.

## Algorithm Details

### Helper Functions
- `is_teacher_free`: Checks if a teacher is available in a specific time slot.
- `is_room_free`: Checks if a room is available in a specific time slot.
- `can_assign`: Combines the above two checks to ensure both teacher and room availability.

### State Class
The `State` class stores a scheduling state with:
  - `timetable`: The current timetable.
  - `course_count`: A count of each course's occurrences in the timetable.

### Backtracking Search
The `backtrack` function uses backtracking to:
  - Select courses with fewer than two scheduled occurrences.
  - Attempt to assign them to an available slot.
  - Recursively build a complete and conflict-free timetable.


## Output Example
Below are example images of the generated timetable and course-teacher mappings:

### Timetable Example
![Screenshot 2024-10-27 110634](https://github.com/user-attachments/assets/edebc2e8-0a89-48a9-8751-0264cca1b591)

### Course-Teacher Assignments
![Screenshot 2024-10-27 110648](https://github.com/user-attachments/assets/13640269-5574-4c3b-91ce-90fe0023b93a)
