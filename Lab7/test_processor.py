from hypothesis import given, strategies as st

from processor import (
    validate_blood_type,
    calculate_pulse_pressure,
    parse_donor_registry,
)


# The handout asks Hypothesis to generate arbitrary strings and None values.
# Any uncaught exception is treated as a fuzz-test failure.


@given(st.text() | st.none())
def test_validate_blood_type_no_crash(value):
    try:
        result = validate_blood_type(value)
        assert isinstance(result, str)
    except Exception as exc:
        assert False, f"validate_blood_type crashed with {value!r}: {exc}"


@given(st.text() | st.none())
def test_calculate_pulse_pressure_safe(value):
    try:
        result = calculate_pulse_pressure(value)
        assert isinstance(result, str)
    except Exception as exc:
        assert False, f"calculate_pulse_pressure crashed with {value!r}: {exc}"


@given(st.text() | st.none())
def test_parse_donor_registry_safe(value):
    try:
        result = parse_donor_registry(value)
        assert isinstance(result, str)
    except Exception as exc:
        assert False, f"parse_donor_registry crashed with {value!r}: {exc}"


@given(st.sampled_from(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]))
def test_valid_blood_types_are_standardized(value):
    result = validate_blood_type(value)
    assert result in {
        "A Positive", "A Negative", "B Positive", "B Negative",
        "AB Positive", "AB Negative", "O Positive", "O Negative",
    }


@given(
    st.integers(min_value=1, max_value=300),
    st.integers(min_value=1, max_value=200),
)
def test_valid_blood_pressure_returns_metrics(systolic, diastolic):
    if systolic > diastolic:
        result = calculate_pulse_pressure(f"{systolic}/{diastolic}")
        assert result.startswith(f"Diff: {systolic - diastolic}, Ratio: ")


@given(
    st.text(alphabet=st.characters(whitelist_categories=("L", "N")), min_size=1, max_size=12),
    st.floats(min_value=0, max_value=250, allow_nan=False, allow_infinity=False),
    st.floats(min_value=0, max_value=30, allow_nan=False, allow_infinity=False),
)
def test_valid_donor_registry_is_classified(donor_id, weight, hemoglobin):
    result = parse_donor_registry(f"{donor_id}|{weight}|{hemoglobin}")
    expected = "Eligible" if weight >= 50.0 and hemoglobin >= 12.5 else "Deferred"
    assert result == f"Donor {donor_id}: {expected}"
