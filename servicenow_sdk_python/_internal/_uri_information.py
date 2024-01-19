from copy import deepcopy
from typing import Dict, Optional, Union
from uritemplate import URITemplate

from servicenow_sdk_python._internal._collection import Collection

_RAW_URL_KEY = "request-raw-url"
_BASE_URL_PLACEHOLDER = "baseurl"
_BASE_URL_TEMPLATE_PLACEHOLDER = "{+baseurl}"


class URIInformation:
    _query: Collection[str]
    _path: Collection[str]
    _template: str

    def __init__(
        self,
        query: Optional[Collection[str]] = None,
        path: Optional[Collection[str]] = None,
        template: Optional[str] = None,
    ) -> None:

        self._query = query or Collection()
        self._path = path or Collection()
        self._template = template or ""

    @property
    def path(self) -> Collection[str]:
        return self._path

    @path.setter
    def path(self, collection: Union[Dict[str, str], Collection[str]]) -> None:

        if not isinstance(collection, Union[dict, Collection]):
            raise TypeError(
                "collection must be of type Dict[str, str] or Collection[str]"
            )

        if isinstance(collection, dict):
            collection = Collection(**collection)

        if (
            _BASE_URL_PLACEHOLDER not in collection.keys()
            and
            _RAW_URL_KEY not in collection.keys()
        ):
            raise ValueError(
                (
                    f"collection must contain {_BASE_URL_PLACEHOLDER!r} "
                    f"or {_RAW_URL_KEY!r}"
                )
            )

        self._path = collection

    @property
    def query(self) -> Collection[str]:

        return self._query

    @query.setter
    def query(
        self, collection: Union[Dict[str, str], Collection[str], None]
    ) -> None:

        if collection is None:
            collection = Collection()

        if not isinstance(collection, Union[dict, Collection]):
            raise TypeError(
                "collection must be of type Dict[str, str] or Collection[str]"
            )

        if isinstance(collection, dict):
            collection = Collection(**collection)

        self._query = collection

    @property
    def template(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        return self._template

    @template.setter
    def template(self, template: str) -> str:
        """_summary_

        Args:
            template (str): _description_

        Returns:
            str: _description_
        """

        if not isinstance(template, str):
            raise TypeError("template must be of type 'str'")

        if _BASE_URL_TEMPLATE_PLACEHOLDER not in template:
            raise ValueError(
                f"template must contain {_BASE_URL_TEMPLATE_PLACEHOLDER}"
            )

        self._template = template

    def _get_uri_from_raw(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        raw_uri = self._path.get(_RAW_URL_KEY, None)
        if raw_uri is None:
            return ""
        return raw_uri

    def _build_uri(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        _vars = deepcopy(self._path)
        _vars.update(self._query)

        template = URITemplate(self._template)
        return template.expand(_vars)

    def to_url(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """

        uri = self._get_uri_from_raw()
        if uri != "":
            return uri
        return self._build_uri()
