VALID_STATUS = ["Planned", "In Progress", "Completed"]

def validate_name(name):
    return name.strip() != ""

def validate_technology(technology):
    return technology.strip() != ""

def validate_status(status):
    return status in VALID_STATUS

