import json
from pathlib import Path

import pytest

from anisotropy import (
    MaterialStage,
    ValidationError,
    emitter_state_from_mapping,
    material_state_from_mapping,
    run_plan_from_mapping,
    specimen_from_mapping,
)


ROOT = Path(__file__).resolve().parents[1]


def test_all_json_files_parse():
    paths = sorted((ROOT / "schemas").glob("*.json"))
    paths += sorted((ROOT / "examples").glob("**/*.json"))
    assert paths
    for path in paths:
        with path.open(encoding="utf-8") as handle:
            assert isinstance(json.load(handle), dict), path


def test_schema_ids_are_unique():
    ids = []
    for path in sorted((ROOT / "schemas").glob("*.json")):
        with path.open(encoding="utf-8") as handle:
            ids.append(json.load(handle)["$id"])
    assert len(ids) == len(set(ids))


def test_unresolved_physical_choices_remain_explicit_in_examples():
    path = ROOT / "examples" / "valid" / "material-state-low-dof.json"
    content = path.read_text(encoding="utf-8")
    assert "UNRESOLVED_DOF_METRIC" in content
    assert "UNRESOLVED_CONSTRAINT" in content


def load_example(relative_path):
    with (ROOT / "examples" / relative_path).open(encoding="utf-8") as handle:
        return json.load(handle)


def test_valid_examples_pass_domain_validation():
    specimen = specimen_from_mapping(load_example("valid/specimen.json"))
    material = material_state_from_mapping(load_example("valid/material-state-low-dof.json"))
    emitter = emitter_state_from_mapping(load_example("valid/emitter-state-isotropic.json"))
    run = run_plan_from_mapping(load_example("valid/run-plan-normal.json"))

    assert specimen.specimen_id == "coupon-normal-001"
    assert material.dof_state.stage is MaterialStage.LOW_DOF
    assert material.dof_state.qualified
    assert emitter.isotropy_metric <= emitter.isotropy_acceptance_max
    assert run.material_stage is MaterialStage.NORMAL


def test_invalid_low_dof_run_is_rejected_by_domain_validation():
    with pytest.raises(ValidationError, match="locked normal"):
        run_plan_from_mapping(load_example("invalid/run-plan-low-dof-unlocked.json"))
