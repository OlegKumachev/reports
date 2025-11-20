from pathlib import Path


def test_cli_invalid_file_exits_with_error(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["reports", "--files", "nonexistent.csv", "--report", "performance"]
    )
    import main as main

    with __import__("pytest").raises(SystemExit) as exc:
        main.main()

    assert exc.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Files not found" in captured.err


def test_cli_valid_files_prints_report(tmp_path: Path, capsys, monkeypatch):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(
        "name,position,performance\n"
        "Alex,Backend Developer,4.8\n"
        "Anna,DevOps Engineer,5.0\n",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        "sys.argv",
        ["reports", "--files", str(csv_file), "--report", "performance"]
    )
    import main as main
    main.main()

    captured = capsys.readouterr()
    output = captured.out
    assert "Performance Report" in output
    assert "DevOps Engineer" in output
    assert "Backend Developer" in output
    assert "4.90" in output or "5.00" in output