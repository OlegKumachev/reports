import pytest
from reports.report import PerformanceReport


@pytest.mark.parametrize(
    "data, expected_contains",
    [
        (
            [
                {"position": "DevOps Engineer", "performance": "4.9"},
                {"position": "DevOps Engineer", "performance": "5.0"},
                {"position": "Backend Developer", "performance": "4.8"},
            ],
            ["DevOps Engineer", "4.95", "Backend Developer", "4.80"],
        ),
        (
            [],
            ["No data"],
        ),
        (
            [{"position": "QA", "performance": "abc"}],
            ["No data"],
        ),
    ],
)
def test_performance_report_generates_correct_output(data, expected_contains):
    report = PerformanceReport()
    output = report.generate(data)

    assert "Performance Report" in output

    for substring in expected_contains:
        assert substring in output, f"Expected '{substring}' to be in report output"