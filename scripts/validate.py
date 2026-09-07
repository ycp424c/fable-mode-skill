#!/usr/bin/env python3
"""Check repository metadata and policy without loading or invoking a model."""

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_mapping(content, label):
    value = yaml.safe_load(content)
    require(isinstance(value, dict), f"{label}: expected a YAML mapping")
    return value


def frontmatter(path):
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", content, re.DOTALL)
    require(match is not None, f"{path.name}: missing YAML frontmatter")
    return load_mapping(match.group(1), path.name), content[match.end():]


def validate():
    metadata, body = frontmatter(ROOT / "fable-mode/SKILL.md")
    require(metadata.get("name") == "fable-mode", "Skill name must be fable-mode")
    description = metadata.get("description")
    require(
        isinstance(description, str) and 0 < len(description.strip()) <= 1024,
        "Skill description must be a nonempty string of at most 1024 characters",
    )
    require(
        "<" not in description and ">" not in description,
        "Skill description must not contain angle brackets",
    )
    require(bool(body.strip()), "Skill instructions must not be empty")

    config = load_mapping(
        (ROOT / "fable-mode/agents/openai.yaml").read_text(encoding="utf-8"),
        "agents/openai.yaml",
    )
    policy = config.get("policy")
    require(
        isinstance(policy, dict) and policy.get("allow_implicit_invocation") is False,
        "policy.allow_implicit_invocation must be the boolean false",
    )

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    require(license_text.startswith("MIT License\n"), "Expected the MIT license")
    require(
        (ROOT / "fable-mode/LICENSE").read_text(encoding="utf-8") == license_text,
        "Root and installable skill licenses must match",
    )

    for path in sorted((ROOT / ".github").rglob("*")):
        if path.suffix in {".yml", ".yaml"}:
            load_mapping(path.read_text(encoding="utf-8"), str(path.relative_to(ROOT)))
        elif path.suffix == ".md" and path.parent.name == "ISSUE_TEMPLATE":
            template, _ = frontmatter(path)
            for key in ("name", "about"):
                require(
                    isinstance(template.get(key), str) and bool(template[key].strip()),
                    f"{path.name}: missing nonempty {key}",
                )


if __name__ == "__main__":
    try:
        validate()
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print("Skill metadata, explicit invocation policy, license copies, and GitHub YAML are valid.")
    print("Static checks only; behavioral evaluation is documented in evals/scenarios.md.")
