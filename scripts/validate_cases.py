#!/usr/bin/env python3
"""Validate Spark-X2.5 community case metadata without external dependencies."""

from __future__ import annotations

import argparse
import re
import tempfile
from datetime import date
from pathlib import Path


DISCUSSION_RE = re.compile(
    r"^https://huggingface\.co/XHToken/Spark-X2\.5-(?:4B|1\.7B)/discussions/\d+(?:#\S+)?$"
)
REVISION_RE = re.compile(r"^[0-9a-fA-F]{40}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED_FIELDS = (
    "title", "author", "date", "category", "testedRevision",
    "runtime", "hardware", "downloadSource", "channels",
)
ALLOWED_SOURCES = {
    "huggingface", "modelscope", "modelers", "scnet", "sourcefind", "ollama",
}
WEIGHT_SUFFIXES = {".safetensors", ".gguf", ".pt", ".pth", ".ckpt"}


def parse_frontmatter(text: str) -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, ["README.md must start with YAML frontmatter"]
    try:
        frontmatter, _body = normalized[4:].split("\n---\n", 1)
    except ValueError:
        return {}, ["README.md frontmatter must end with a second --- line"]

    fields: dict[str, object] = {}
    active_list: str | None = None
    for raw_line in frontmatter.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        item = re.match(r"^\s+-\s+(.+?)\s*$", raw_line)
        if item and active_list:
            values = fields.setdefault(active_list, [])
            if isinstance(values, list):
                values.append(item.group(1).strip("'\""))
            continue
        field = re.match(r"^([A-Za-z][A-Za-z0-9]*):\s*(.*?)\s*$", raw_line)
        if not field:
            errors.append(f"unsupported frontmatter line: {raw_line}")
            active_list = None
            continue
        key, value = field.groups()
        value = value.split(" #", 1)[0].strip().strip("'\"")
        if value:
            fields[key] = value
            active_list = None
        else:
            fields[key] = []
            active_list = key
    return fields, errors


def validate_case(case_dir: Path) -> list[str]:
    errors: list[str] = []
    readme = case_dir / "README.md"
    if not readme.is_file():
        return [f"{case_dir.name}: missing README.md"]

    text = readme.read_text(encoding="utf-8")
    fields, parse_errors = parse_frontmatter(text)
    errors.extend(f"{case_dir.name}: {message}" for message in parse_errors)
    for key in REQUIRED_FIELDS:
        if not fields.get(key):
            errors.append(f"{case_dir.name}: missing frontmatter field {key}")

    author = str(fields.get("author", ""))
    if author.lower().startswith("your-") or "replace_me" in author.lower():
        errors.append(f"{case_dir.name}: replace the author placeholder")

    raw_date = str(fields.get("date", ""))
    if not DATE_RE.fullmatch(raw_date):
        errors.append(f"{case_dir.name}: date must use YYYY-MM-DD")
    else:
        try:
            date.fromisoformat(raw_date)
        except ValueError:
            errors.append(f"{case_dir.name}: date is not a real calendar date")

    revision = str(fields.get("testedRevision", ""))
    if not REVISION_RE.fullmatch(revision):
        errors.append(f"{case_dir.name}: testedRevision must be a full 40-character commit SHA")
    if str(fields.get("downloadSource", "")).lower() not in ALLOWED_SOURCES:
        errors.append(
            f"{case_dir.name}: downloadSource must be one of {sorted(ALLOWED_SOURCES)}"
        )

    channels = fields.get("channels", [])
    if not isinstance(channels, list) or not channels:
        errors.append(f"{case_dir.name}: channels must contain a Spark-X2.5 Discussion URL")
    else:
        body = text.split("\n---\n", 1)[-1]
        for channel in channels:
            if not DISCUSSION_RE.fullmatch(str(channel)):
                errors.append(
                    f"{case_dir.name}: invalid channel {channel}; only public Spark-X2.5 Discussions are accepted"
                )
            if str(channel) not in body:
                errors.append(f"{case_dir.name}: Discussion URL must also appear in the case body")

    lowered = text.lower()
    if "replace_me" in lowered or "<case title>" in lowered:
        errors.append(f"{case_dir.name}: unresolved template placeholder")
    for path in case_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in WEIGHT_SUFFIXES:
            errors.append(f"{case_dir.name}: do not commit model weight file {path.name}")
    return errors


def validate_repository(root: Path) -> list[str]:
    cases = root / "cases"
    errors: list[str] = []
    for required in (cases / "README.md", cases / "TEMPLATE" / "README.md"):
        if not required.is_file():
            errors.append(f"missing scaffold file: {required.relative_to(root)}")
    if not cases.is_dir():
        return errors
    for case_dir in sorted(cases.iterdir()):
        if case_dir.is_dir() and case_dir.name != "TEMPLATE":
            errors.extend(validate_case(case_dir))
    return errors


def self_test() -> None:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        (root / "cases" / "TEMPLATE").mkdir(parents=True)
        (root / "cases" / "README.md").write_text("scaffold\n", encoding="utf-8")
        (root / "cases" / "TEMPLATE" / "README.md").write_text("template\n", encoding="utf-8")
        case_dir = root / "cases" / "valid-case"
        case_dir.mkdir()
        discussion = "https://huggingface.co/XHToken/Spark-X2.5-4B/discussions/42"
        case_dir.joinpath("README.md").write_text(
            f"""---
title: Real Spark-X2.5 agent run
author: contributor
date: 2026-09-08
category: agentic-workflow
testedRevision: 6c71a32f4d624cadfd9fce9d10240d8068e53456
runtime: sglang-nightly-cu13
hardware: A100-80GB
downloadSource: huggingface
channels:
  - {discussion}
---

# Real Spark-X2.5 agent run

## Published Hugging Face Discussion

{discussion}
""",
            encoding="utf-8",
        )
        assert validate_repository(root) == []
        bad = case_dir.joinpath("README.md").read_text(encoding="utf-8").replace(
            discussion, "https://example.com/post"
        )
        case_dir.joinpath("README.md").write_text(bad, encoding="utf-8")
        assert any("invalid channel" in error for error in validate_repository(root))
    print("[cases] self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    errors = validate_repository(args.root.resolve())
    if errors:
        for error in errors:
            print(f"[cases] ERROR: {error}")
        return 1
    print("[cases] scaffold and submitted cases are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
