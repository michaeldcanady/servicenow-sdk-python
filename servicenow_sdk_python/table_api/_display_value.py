from enum import IntEnum, auto


class DisplayValue(IntEnum):
    """Determines the type of data returned, either the actual values from the
database or the display values of the fields. Display values are
manipulated based on the actual value in the database and user or system
settings and preferences.

If returning display values, the value that is returned is dependent on the
field type.

- Choice fields: The database value may be a number, but the display value
will be more descriptive.
- Date fields: The database value is in UTC format, while the display value is
based on the user's time zone.
- Encrypted text: The database value is encrypted, while the displayed value
is unencrypted based on the user's encryption context.
- Reference fields: The database value is sys_id, but the display value is a
display field of the referenced record.
    """

    NONE = 0
    """Value unset"""
    TRUE = auto()
    """Returns the display values for all fields."""
    FALSE = auto()
    """Returns the actual values from the database."""
    ALL = auto()
    """Returns both actual and display values."""

    def __str__(self) -> str:

        return [
            "",
            "true",
            "false",
            "all",
        ][self]
