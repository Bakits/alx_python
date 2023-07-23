def validate_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digits
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        if has_uppercase and has_lowercase and has_digit:
            break

    # Check for spaces
    if " " in password:
        return False

    # Return True if all checks pass
    return has_uppercase and has_lowercase and has_digit
