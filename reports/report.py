import statistics
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List
from tabulate import tabulate
from report.types import EmployeeDict


class Report(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def generate(self, data:List[EmployeeDict]) -> str:
        ...

class PerformanceReport(Report):
    name = "Performance Report"

    def generate(self, data:List[EmployeeDict]) -> str:
        position_perf: dict[str, List[float]] = defaultdict(list)

        for row in data:
            try:
                perf = float(row["performance"])
                position_perf[row["position"]].append(perf)
            except (KeyError, ValueError):
                continue
        if not position_perf:
            return  return f"{self.name}\n{'-' * len(self.name)}\nNo data"
        table_data = []
        for position, value in position_perf.items():
            avg = round(statistics.mean(value), 2)
            table_data.append((position, avg))

        table_data.sort(key=lambda x: x[1], reverse=True)

        headers = ["position", "average_performance"]
        table = tabulate(table_data, headers=headers, tablefmt='pipe', floatfmt=".2f")

        return f"{self.name}\n{'-' * len(self.name)}\n{table}"

