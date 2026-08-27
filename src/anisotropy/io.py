"""Explicit mapping adapters for JSON-compatible experiment records."""

from typing import Any, Mapping

from .domain import (
    AnalysisRole,
    DOFState,
    EmitterState,
    Energization,
    MaterialStage,
    MaterialState,
    RunPlan,
    Specimen,
    Symmetry,
    ValidationError,
)


def _enum(enum_type: Any, value: Any, field_name: str) -> Any:
    try:
        return enum_type(value)
    except (TypeError, ValueError):
        allowed = ", ".join(item.value for item in enum_type)
        raise ValidationError("{} must be one of: {}".format(field_name, allowed))


def specimen_from_mapping(data: Mapping[str, Any]) -> Specimen:
    try:
        dimensions = tuple(data["dimensions_mm"])
        return Specimen(
            specimen_id=data["specimen_id"],
            batch_id=data["batch_id"],
            parent_material_id=data["parent_material_id"],
            composition=data["composition"],
            mediator_id=data["mediator_id"],
            dimensions_mm=dimensions,
        )
    except KeyError as error:
        raise ValidationError("missing specimen field: {}".format(error.args[0]))


def material_state_from_mapping(data: Mapping[str, Any]) -> MaterialState:
    try:
        raw_dof = data["dof_state"]
        dof = DOFState(
            stage=_enum(MaterialStage, raw_dof["stage"], "dof_state.stage"),
            d_eff=raw_dof["d_eff"],
            d_eff_reference=raw_dof["d_eff_reference"],
            reduction_threshold=raw_dof["reduction_threshold"],
            metric_name=raw_dof["metric_name"],
            measurement_method=raw_dof["measurement_method"],
            constrained_modes=tuple(raw_dof.get("constrained_modes", ())),
            constraint_mechanism=raw_dof.get("constraint_mechanism"),
            induced_conventional_changes=dict(raw_dof.get("induced_conventional_changes", {})),
        )
        return MaterialState(
            material_state_id=data["material_state_id"],
            specimen_id=data["specimen_id"],
            symmetry=_enum(Symmetry, data["symmetry"], "symmetry"),
            dof_state=dof,
            director_angle_deg=data.get("director_angle_deg"),
            anisotropy_parallel=data.get("anisotropy_parallel"),
            anisotropy_perpendicular=data.get("anisotropy_perpendicular"),
        )
    except KeyError as error:
        raise ValidationError("missing material-state field: {}".format(error.args[0]))


def emitter_state_from_mapping(data: Mapping[str, Any]) -> EmitterState:
    try:
        return EmitterState(
            emitter_state_id=data["emitter_state_id"],
            symmetry=_enum(Symmetry, data["symmetry"], "symmetry"),
            deposited_energy_target_j=data["deposited_energy_target_j"],
            energy_tolerance_fraction=data["energy_tolerance_fraction"],
            isotropy_metric=data["isotropy_metric"],
            isotropy_acceptance_max=data["isotropy_acceptance_max"],
            director_angle_deg=data.get("director_angle_deg"),
        )
    except KeyError as error:
        raise ValidationError("missing emitter-state field: {}".format(error.args[0]))


def run_plan_from_mapping(data: Mapping[str, Any]) -> RunPlan:
    try:
        return RunPlan(
            run_id=data["run_id"],
            specimen_id=data["specimen_id"],
            material_state_id=data["material_state_id"],
            emitter_state_id=data["emitter_state_id"],
            energization=_enum(Energization, data["energization"], "energization"),
            analysis_role=_enum(AnalysisRole, data["analysis_role"], "analysis_role"),
            material_stage=_enum(MaterialStage, data["material_stage"], "material_stage"),
            amplitude_level=data["amplitude_level"],
            mediator_id=data["mediator_id"],
            normal_analysis_locked=data.get("normal_analysis_locked", False),
            destructive=data.get("destructive", False),
            precursor_analysis_locked=data.get("precursor_analysis_locked", False),
        )
    except KeyError as error:
        raise ValidationError("missing run-plan field: {}".format(error.args[0]))
