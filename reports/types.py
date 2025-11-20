from dataclasses import dataclass
from typing import TypedDict, List

class EmployeeDict(TypedDict):
    name: str
    position: str
    completed_task: str
    performance: str
    skills: str
    team: str
    experience_years: str

@dataclass(frozen=True, slots=True)
class Employee:
    name: str
    position: str
    performance: float
