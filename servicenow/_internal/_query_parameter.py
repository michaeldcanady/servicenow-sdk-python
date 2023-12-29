from copy import deepcopy
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class QueryParameter:

    __list_sep__ = ","

    def to_query(self) -> Dict[str, str]:

        as_dict = asdict(self)

        for key, value in deepcopy(as_dict).items():
            match value:
                case list():
                    value = self.__list_sep__.join(value)
                case bool():
                    value = str(value).lower()
                case None:
                    del as_dict[key]
                case _:
                    value = str(value)
            if value is not None:
                as_dict[key] = value
        return as_dict
