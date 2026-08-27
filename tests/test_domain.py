import pytest

from anisotropy import (
    AnalysisRole,
    DOFState,
    EmitterState,
    Energization,
    MaterialStage,
    MaterialState,
    RunPlan,
    Symmetry,
    ValidationError,
)


def normal_dof():
    return DOFState(
        stage=MaterialStage.NORMAL,
        d_eff=1.0,
        d_eff_reference=1.0,
        reduction_threshold=0.25,
        metric_name="measured mode participation",
        measurement_method="qualified spectroscopy",
    )


def low_dof():
    return DOFState(
        stage=MaterialStage.LOW_DOF,
        d_eff=0.65,
        d_eff_reference=1.0,
        reduction_threshold=0.25,
        metric_name="measured mode participation",
        measurement_method="qualified spectroscopy",
        constrained_modes=("domain motion",),
        constraint_mechanism="qualified fixture",
        induced_conventional_changes={"permittivity_ratio": 0.02},
    )


def test_normal_state_is_qualified_reference():
    state = normal_dof()
    assert state.reduction_fraction == pytest.approx(0.0)
    assert state.qualified


def test_low_dof_requires_measured_reduction_and_named_constraint():
    state = low_dof()
    assert state.reduction_fraction == pytest.approx(0.35)
    assert state.qualified


def test_low_dof_without_constrained_mode_fails_closed():
    with pytest.raises(ValidationError, match="constrained mode"):
        DOFState(
            stage=MaterialStage.LOW_DOF,
            d_eff=0.8,
            d_eff_reference=1.0,
            reduction_threshold=0.1,
            metric_name="metric",
            measurement_method="method",
            constraint_mechanism="fixture",
        )


def test_direct_constructor_rejects_unvalidated_stage_string():
    with pytest.raises(ValidationError, match="MaterialStage"):
        DOFState(
            stage="normal",
            d_eff=1.0,
            d_eff_reference=1.0,
            reduction_threshold=0.1,
            metric_name="metric",
            measurement_method="method",
        )


def test_anisotropic_material_requires_director_and_distinct_responses():
    state = MaterialState(
        material_state_id="m1",
        specimen_id="s1",
        symmetry=Symmetry.ANISOTROPIC,
        dof_state=normal_dof(),
        director_angle_deg=45.0,
        anisotropy_parallel=2.0,
        anisotropy_perpendicular=1.0,
    )
    assert state.director_angle_deg == 45.0


def test_isotropic_emitter_fails_if_isotropy_tolerance_is_exceeded():
    with pytest.raises(ValidationError, match="isotropy acceptance"):
        EmitterState(
            emitter_state_id="e1",
            symmetry=Symmetry.ISOTROPIC_EFFECTIVE,
            deposited_energy_target_j=0.1,
            energy_tolerance_fraction=0.02,
            isotropy_metric=0.04,
            isotropy_acceptance_max=0.02,
        )


def test_low_dof_run_requires_locked_normal_analysis():
    with pytest.raises(ValidationError, match="locked normal"):
        RunPlan(
            run_id="r1",
            specimen_id="s1",
            material_state_id="m1",
            emitter_state_id="e1",
            energization=Energization.ON_ON,
            analysis_role=AnalysisRole.HELD_OUT,
            material_stage=MaterialStage.LOW_DOF,
            amplitude_level=1.0,
            mediator_id="i1",
            normal_analysis_locked=False,
        )


def test_destructive_run_requires_locked_precursor_analysis():
    with pytest.raises(ValidationError, match="locked precursor"):
        RunPlan(
            run_id="r1",
            specimen_id="s1",
            material_state_id="m1",
            emitter_state_id="e1",
            energization=Energization.ON_ON,
            analysis_role=AnalysisRole.HELD_OUT,
            material_stage=MaterialStage.NORMAL,
            amplitude_level=1.0,
            mediator_id="i1",
            destructive=True,
        )


def test_run_plan_rejects_non_boolean_lock_values():
    with pytest.raises(ValidationError, match="normal_analysis_locked must be boolean"):
        RunPlan(
            run_id="r1",
            specimen_id="s1",
            material_state_id="m1",
            emitter_state_id="e1",
            energization=Energization.ON_ON,
            analysis_role=AnalysisRole.HELD_OUT,
            material_stage=MaterialStage.NORMAL,
            amplitude_level=1.0,
            mediator_id="i1",
            normal_analysis_locked="false",
        )
