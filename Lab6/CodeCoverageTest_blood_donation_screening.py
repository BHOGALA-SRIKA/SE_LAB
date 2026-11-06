
import pytest
from blood_donation_screening import (
    process_donor_cohort,
    verify_storage_centrifuge
)


def test_invalid_non_list():
    with pytest.raises(ValueError):
        process_donor_cohort(None, 450)


def test_invalid_volume():
    with pytest.raises(ValueError):
        process_donor_cohort([], -10)


def test_valid_empty_cohort_list():
    assert process_donor_cohort([], 450) == {
        "collected_ml": 0, "status": "ZERO_YIELD"
    }


def test_unregistered_cohort():
    cohorts = [{"clinic_registered": False}]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_registered_cohort_without_donors():
    cohorts = [{"clinic_registered": True}]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_age_below_17():
    cohorts = [{
        "clinic_registered": True,
        "donors": [{"age": 16, "weight_kg": 65, "hb": 14.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_weight_below_50():
    cohorts = [{
        "clinic_registered": True,
        "donors": [{"age": 20, "weight_kg": 49, "hb": 14.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_low_hemoglobin_standard():
    cohorts = [{
        "clinic_registered": True,
        "type": "standard",
        "donors": [{"age": 25, "weight_kg": 65, "hb": 12.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_low_hemoglobin_high_altitude():
    cohorts = [{
        "clinic_registered": True,
        "type": "high_altitude",
        "donors": [
            {"age": 25, "weight_kg": 65, "hb": 14.0},
            {"age": 25, "weight_kg": 65, "hb": 12.0},
            {"age": 25, "weight_kg": 65, "hb": 14.0}
        ]
    }]
    result = process_donor_cohort(cohorts, 450)
    assert result["collected_ml"] == 0


def test_high_hemoglobin():
    cohorts = [{
        "clinic_registered": True,
        "donors": [{"age": 25, "weight_kg": 65, "hb": 19.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["status"] == "ZERO_YIELD"


def test_hemoglobin_boundaries():
    cohorts = [{
        "clinic_registered": True,
        "donors": [
            {"age": 25, "weight_kg": 65, "hb": 12.5},
            {"age": 25, "weight_kg": 65, "hb": 18.0}
        ]
    }]
    result = process_donor_cohort(cohorts, 450)
    assert result["collected_ml"] == 900
    assert result["status"] == "ACCEPTED"


def test_fast_track_true():
    cohorts = [{
        "clinic_registered": True,
        "fast_track": True,
        "donors": [{"age": 25, "weight_kg": 65, "hb": 14.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["collected_ml"] == 500


def test_fast_track_false():
    cohorts = [{
        "clinic_registered": True,
        "fast_track": False,
        "donors": [{"age": 25, "weight_kg": 65, "hb": 14.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["collected_ml"] == 450


def test_more_than_four_deferrals():
    donors = [
        {"age": 16, "weight_kg": 65, "hb": 14.0}
        for _ in range(5)
    ]
    result = process_donor_cohort(
        [{"clinic_registered": True, "donors": donors}], 450
    )
    assert result["status"] == "HIGH_DEFERRAL"


def test_four_or_fewer_deferrals():
    donors = [
        {"age": 16, "weight_kg": 65, "hb": 14.0}
        for _ in range(4)
    ]
    result = process_donor_cohort(
        [{"clinic_registered": True, "donors": donors}], 450
    )
    assert result["status"] == "ZERO_YIELD"


def test_accepted_status():
    cohorts = [{
        "clinic_registered": True,
        "donors": [{"age": 25, "weight_kg": 65, "hb": 14.0}]
    }]
    assert process_donor_cohort(cohorts, 450)["status"] == "ACCEPTED"


def test_no_centrifuge_data():
    assert verify_storage_centrifuge([]) == "NO_DATA"


def test_empty_centrifuge_run():
    assert verify_storage_centrifuge([[]]) == "STABLE"


def test_single_low_rpm():
    assert verify_storage_centrifuge([[2500]]) == "STABLE"


def test_rpm_recovery_resets_streak():
    assert verify_storage_centrifuge([[2500, 3500, 2500]]) == "STABLE"


def test_two_consecutive_low_rpm():
    assert verify_storage_centrifuge([[2500, 2800]]) == "ABORT_SPIN"


def test_multiple_runs():
    assert verify_storage_centrifuge([[2500], [3500]]) == "STABLE"
