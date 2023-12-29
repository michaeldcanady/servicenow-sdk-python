from typing import Dict, Any

from pydantic import RootModel

from servicenow.table_api._table_value import TableValue


class TableEntry(RootModel[Dict[str, TableValue]]):

    def __iter__(self) -> str:
        return self.root.__iter__()

    def __getitem__(self, __key: str) -> TableValue:
        return self.root[__key]

    def items(self) -> Dict[str, TableValue]:
        return self.root.items()
