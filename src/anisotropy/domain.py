"""Validated, conventional domain records for M000-M002.

These records describe measured experimental state. They intentionally contain
no Phi/Psi observables or speculative conversion factors.
"""

from dataclasses import dataclass, field
from enum import Enum
from math import isfinite
from typing import Dict, Optional, Tuple


class ValidationError(ValueError):
    """Raised when a record violates the controlling experiment contract."""


class MaterialStage(str, Enum):
    NORMAL = "normal"
    LOW_DOF = "low_dof"


class Symmetry(str, Enum):
    ISOTROPIC_EFFECTIVE = "isotropic_effective"
    ANISOTROPIC = "anisotropic"


class Energization(str, Enum):
    OFF_OFF = "00"
    ON_OFF = "10"
    OFF_ON = "01"
    ON_ON = "11"


class AnalysisRole(str, Enum):
    CALIBRATION = "calibration"
    TRAINING = "training"
    HELD_OUT = "held_out"
    REPLICATION = "replication"


def _required_text(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError("{} must be non-empty".format(name))


def _finite_nonnegative(value: float, name: str) -> None:
    if not isfinite(value) or value < 0:
        raise ValidationError("{} must be finite and non-negative".format(name))


def _angle(value: Optional[float], name: str) -> None:
    if value is None or not isfinite(value) or not 0 <= value < 180:
        raise ValidationError("{} must be in [0, 180) degrees".format(name))


def _enum_instance(value: object, enum_type: object, name: str) -> None:
    if not isinstance(value, enum_type):
        raise ValidationError("{} must be a {} value".format(name, enum_type.__name__))


def _boolean(value: object, name: str) -> None:
    if not isinstance(value, bool):
        raise ValidationError("{} must be boolean".format(name))


@dataclass(frozen=True)
class Specimen:
    specimen_id: str
    batch_id: str
    parent_material_id: str
    composition: str
    mediator_id: str
    dimensions_mm: Tuple[float, float, float]

    def __post_init__(self) -> None:
        for name in ("specimen_id", "batch_id", "parent_material_id", "composition", "mediator_id"):
            _required_text(getattr(self, name), name)
        if len(self.dimensions_mm) != 3 or any(not isfinite(v) or v <= 0 for v in self.dimensions_mm):
            raise ValidationError("dimensions_mm must contain three finite positive values")


@dataclass(frozen=True)
class DOFState:
    stage: MaterialStage
    d_eff: float
    d_eff_reference: float
    reduction_threshold: float
    metric_name: str
    measurement_method: str
    constrained_modes: Tuple[str, ...] = ()
    constraint_mechanism: Optional[str] = None
    induced_conventional_changes: Dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _enum_instance(self.stage, MaterialStage, "stage")
        _required_text(self.metric_name, "metric_name")
        _required_text(self.measurement_method, "measurement_method")
        if not isfinite(self.d_eff) or self.d_eff <= 0:
            raise ValidationError("d_eff must be finite and positive")
        if not isfinite(self.d_eff_reference) or self.d_eff_reference <= 0:
            raise ValidationError("d_eff_reference must be finite and positive")
        if not isfinite(self.reduction_threshold) or not 0 <= self.reduction_threshold <= 1:
            raise ValidationError("reduction_threshold must be in [0, 1]")
        if any(not isfinite(value) for value in self.induced_conventional_changes.values()):
            raise ValidationError("induced conventional changes must be finite")

        if self.stage is MaterialStage.NORMAL:
            if self.constrained_modes or self.constraint_mechanism is not None:
                raise ValidationError("normal state cannot declare a low-DOF constraint")
            if abs(self.d_eff - self.d_eff_reference) > 1e-12:
                raise ValidationError("normal d_eff must equal its reference")
        else:
            if not self.constrained_modes:
                raise ValidationError("low-DOF state must name at least one constrained mode")
            _required_text(self.constraint_mechanism or "", "constraint_mechanism")
            if self.d_eff > self.d_eff_reference:
                raise ValidationError("low-DOF d_eff cannot exceed its normal reference")

    @property
    def reduction_fraction(self) -> float:
        return 1.0 - self.d_eff / self.d_eff_reference

    @property
    def qualified(self) -> bool:
        if self.stage is MaterialStage.NORMAL:
            return True
        return self.reduction_fraction >= self.reduction_threshold


@dataclass(frozen=True)
class MaterialState:
    material_state_id: str
    specimen_id: str
    symmetry: Symmetry
    dof_state: DOFState
    director_angle_deg: Optional[float] = None
    anisotropy_parallel: Optional[float] = None
    anisotropy_perpendicular: Optional[float] = None

    def __post_init__(self) -> None:
        _required_text(self.material_state_id, "material_state_id")
        _required_text(self.specimen_id, "specimen_id")
        _enum_instance(self.symmetry, Symmetry, "symmetry")
        if self.symmetry is Symmetry.ANISOTROPIC:
            _angle(self.director_angle_deg, "director_angle_deg")
            if self.anisotropy_parallel is None or self.anisotropy_perpendicular is None:
                raise ValidationError("anisotropic material requires parallel and perpendicular responses")
            _finite_nonnegative(self.anisotropy_parallel, "anisotropy_parallel")
            _finite_nonnegative(self.anisotropy_perpendicular, "anisotropy_perpendicular")
            if self.anisotropy_parallel == self.anisotropy_perpendicular:
                raise ValidationError("anisotropic responses must differ")
        elif any(value is not None for value in (
            self.director_angle_deg,
            self.anisotropy_parallel,
            self.anisotropy_perpendicular,
        )):
            raise ValidationError("isotropic-effective material cannot declare a director or principal responses")


@dataclass(frozen=True)
class EmitterState:
    emitter_state_id: str
    symmetry: Symmetry
    deposited_energy_target_j: float
    energy_tolerance_fraction: float
    isotropy_metric: float
    isotropy_acceptance_max: float
    director_angle_deg: Optional[float] = None

    def __post_init__(self) -> None:
        _required_text(self.emitter_state_id, "emitter_state_id")
        _enum_instance(self.symmetry, Symmetry, "symmetry")
        if not isfinite(self.deposited_energy_target_j) or self.deposited_energy_target_j <= 0:
            raise ValidationError("deposited_energy_target_j must be finite and positive")
        for name in ("energy_tolerance_fraction", "isotropy_metric", "isotropy_acceptance_max"):
            value = getattr(self, name)
            if not isfinite(value) or not 0 <= value <= 1:
                raise ValidationError("{} must be in [0, 1]".format(name))
        if self.symmetry is Symmetry.ANISOTROPIC:
            _angle(self.director_angle_deg, "director_angle_deg")
        elif self.director_angle_deg is not None:
            raise ValidationError("isotropic-effective emitter cannot declare a director")
        if self.symmetry is Symmetry.ISOTROPIC_EFFECTIVE and self.isotropy_metric > self.isotropy_acceptance_max:
            raise ValidationError("isotropic-effective emitter exceeds its isotropy acceptance limit")


@dataclass(frozen=True)
class Calibration:
    calibration_id: str
    instrument_id: str
    performed_at_utc: str
    valid_until_utc: str
    passed: bool

    def __post_init__(self) -> None:
        for name in ("calibration_id", "instrument_id", "performed_at_utc", "valid_until_utc"):
            _required_text(getattr(self, name), name)
        _boolean(self.passed, "passed")


@dataclass(frozen=True)
class RunPlan:
    run_id: str
    specimen_id: str
    material_state_id: str
    emitter_state_id: str
    energization: Energization
    analysis_role: AnalysisRole
    material_stage: MaterialStage
    amplitude_level: float
    mediator_id: str
    normal_analysis_locked: bool = False
    destructive: bool = False
    precursor_analysis_locked: bool = False

    def __post_init__(self) -> None:
        for name in ("run_id", "specimen_id", "material_state_id", "emitter_state_id", "mediator_id"):
            _required_text(getattr(self, name), name)
        _enum_instance(self.energization, Energization, "energization")
        _enum_instance(self.analysis_role, AnalysisRole, "analysis_role")
        _enum_instance(self.material_stage, MaterialStage, "material_stage")
        _boolean(self.normal_analysis_locked, "normal_analysis_locked")
        _boolean(self.destructive, "destructive")
        _boolean(self.precursor_analysis_locked, "precursor_analysis_locked")
        if not isfinite(self.amplitude_level) or self.amplitude_level < 0:
            raise ValidationError("amplitude_level must be finite and non-negative")
        if self.energization is Energization.OFF_OFF and self.amplitude_level != 0:
            raise ValidationError("00 runs must have zero amplitude")
        if self.energization is not Energization.OFF_OFF and self.amplitude_level <= 0:
            raise ValidationError("energized runs must have positive amplitude")
        if self.material_stage is MaterialStage.LOW_DOF and not self.normal_analysis_locked:
            raise ValidationError("low-DOF runs require a locked normal analysis")
        if self.destructive and not self.precursor_analysis_locked:
            raise ValidationError("destructive runs require locked precursor analysis")
