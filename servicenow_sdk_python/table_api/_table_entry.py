from typing import Dict, TypeVar, Union

from pydantic import RootModel

from servicenow_sdk_python.table_api._table_value import TableValue


_T = TypeVar("_T")


class TableEntry(RootModel[Dict[str, TableValue]]):
    """A class used to represent a table entry."""

    # TODO: find way to indicate when single values are display values vs
    # values

    def __iter__(self) -> str:
        return self.root.__iter__()

    def __getitem__(self, __key: str) -> TableValue:
        return self.root[__key]

    def items(self) -> Dict[str, TableValue]:
        """
        Gets the items of the root of the table entry.

        Returns:
            Dict[str, TableValue]: The items of the root of the table entry.
        """

        return self.root.items()

    def get(self, __key: str, default: _T = None) -> Union[TableValue, _T]:
        """
        Gets the value of the root of the table value by key.

        Args:
            __key (str): The key of the value.
            default (_T, optional): The default value if the key is not found.
            Defaults to None.

        Returns:
            _T: The value of the root of the table value.
        """

        return self.root.get(__key, default)
