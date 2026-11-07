import math
import re


def validate_blood_type(blood_code):
    """
    Standardizes a valid ABO/Rh blood type (e.g. 'O+', 'AB-').

    Invalid inputs return a readable validation message instead of raising
    an exception. Valid ABO groups are A, B, AB and O; Rh must be + or -.
    """
    if not isinstance(blood_code, str):
        return "Invalid blood type: input must be a string"

    cleaned = blood_code.strip().upper()
    match = re.fullmatch(r"(A|B|AB|O)([+-])", cleaned)
    if not match:
        return "Invalid blood type: use A+, A-, B+, B-, AB+, AB-, O+ or O-"

    antigen, rh_char = match.groups()
    rh_map = {"+": "Positive", "-": "Negative"}
    return f"{antigen} {rh_map[rh_char]}"


def calculate_pulse_pressure(bp_string):
    """
    Calculates pulse pressure (systolic - diastolic) and systolic/diastolic
    ratio from a string in 'systolic/diastolic' format.

    Invalid inputs return a readable validation message instead of raising
    an exception.
    """
    if not isinstance(bp_string, str):
        return "Invalid blood pressure: input must be a string"

    cleaned = bp_string.strip()
    if not re.fullmatch(r"\d+\s*/\s*\d+", cleaned):
        return "Invalid blood pressure: use the format systolic/diastolic"

    sys_str, dia_str = cleaned.split("/")
    try:
        systolic = int(sys_str.strip())
        diastolic = int(dia_str.strip())
    except ValueError:
        return "Invalid blood pressure: numeric values are too large or invalid"

    if systolic <= 0 or diastolic <= 0:
        return "Invalid blood pressure: values must be greater than zero"
    if systolic <= diastolic:
        return "Invalid blood pressure: systolic must be greater than diastolic"

    pulse_diff = systolic - diastolic
    ratio = round(systolic / diastolic, 2)
    return f"Diff: {pulse_diff}, Ratio: {ratio}"


def parse_donor_registry(donor_entry):
    """
    Parses a pipe-delimited record: 'DonorID|WeightKg|Hemoglobin'.

    Invalid inputs return a readable validation message instead of raising
    an exception. Eligibility thresholds remain weight >= 50 kg and
    hemoglobin >= 12.5.
    """
    if not isinstance(donor_entry, str):
        return "Invalid donor record: input must be a string"

    fields = donor_entry.split("|")
    if len(fields) != 3:
        return "Invalid donor record: expected DonorID|WeightKg|Hemoglobin"

    donor_id = fields[0].strip()
    if not donor_id:
        return "Invalid donor record: donor ID cannot be empty"

    try:
        weight = float(fields[1].strip())
        hemoglobin = float(fields[2].strip())
    except (TypeError, ValueError):
        return "Invalid donor record: weight and hemoglobin must be numbers"

    if not math.isfinite(weight) or not math.isfinite(hemoglobin):
        return "Invalid donor record: numeric values must be finite"
    if weight < 0 or hemoglobin < 0:
        return "Invalid donor record: numeric values cannot be negative"

    eligible = weight >= 50.0 and hemoglobin >= 12.5
    return f"Donor {donor_id}: {'Eligible' if eligible else 'Deferred'}"


def main():
    print("==== Running validate_blood_type ====")
    b_input = input("Enter blood type (e.g. A+, O-, AB+): ")
    print("Validated:", validate_blood_type(b_input))

    print("\n==== Running calculate_pulse_pressure ====")
    bp_input = input("Enter BP (e.g. 120/80): ")
    print("BP Metrics:", calculate_pulse_pressure(bp_input))

    print("\n==== Running parse_donor_registry ====")
    d_input = input("Enter record (ID|Weight|Hemoglobin): ")
    print("Status:", parse_donor_registry(d_input))


if __name__ == "__main__":
    main()
