from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorDestroyRequest(_message.Message):
    __slots__ = ("author_id",)
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    def __init__(self, author_id: _Optional[str] = ...) -> None: ...

class AuthorListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AuthorListResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[AuthorResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[AuthorResponse, _Mapping]]] = ...) -> None: ...

class AuthorPartialUpdateRequest(_message.Message):
    __slots__ = ("author_id", "name_first", "name_last", "birth_date", "_partial_update_fields")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIRST_FIELD_NUMBER: _ClassVar[int]
    NAME_LAST_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    name_first: str
    name_last: str
    birth_date: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, author_id: _Optional[str] = ..., name_first: _Optional[str] = ..., name_last: _Optional[str] = ..., birth_date: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthorRequest(_message.Message):
    __slots__ = ("author_id", "name_first", "name_last", "birth_date")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIRST_FIELD_NUMBER: _ClassVar[int]
    NAME_LAST_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    name_first: str
    name_last: str
    birth_date: str
    def __init__(self, author_id: _Optional[str] = ..., name_first: _Optional[str] = ..., name_last: _Optional[str] = ..., birth_date: _Optional[str] = ...) -> None: ...

class AuthorResponse(_message.Message):
    __slots__ = ("author_id", "name_first", "name_last", "birth_date")
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIRST_FIELD_NUMBER: _ClassVar[int]
    NAME_LAST_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    name_first: str
    name_last: str
    birth_date: str
    def __init__(self, author_id: _Optional[str] = ..., name_first: _Optional[str] = ..., name_last: _Optional[str] = ..., birth_date: _Optional[str] = ...) -> None: ...

class AuthorRetrieveRequest(_message.Message):
    __slots__ = ("author_id",)
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    def __init__(self, author_id: _Optional[str] = ...) -> None: ...

class BookDestroyRequest(_message.Message):
    __slots__ = ("book_id",)
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    def __init__(self, book_id: _Optional[str] = ...) -> None: ...

class BookListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BookListResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[BookResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[BookResponse, _Mapping]]] = ...) -> None: ...

class BookPartialUpdateRequest(_message.Message):
    __slots__ = ("book_id", "title", "authors", "categories", "isbn", "publisher", "publication_date", "_partial_update_fields")
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    isbn: str
    publisher: str
    publication_date: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, book_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., isbn: _Optional[str] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class BookRequest(_message.Message):
    __slots__ = ("book_id", "title", "authors", "categories", "isbn", "publisher", "publication_date")
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    isbn: str
    publisher: str
    publication_date: str
    def __init__(self, book_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., isbn: _Optional[str] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ...) -> None: ...

class BookResponse(_message.Message):
    __slots__ = ("book_id", "title", "authors", "categories", "isbn", "publisher", "publication_date")
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    isbn: str
    publisher: str
    publication_date: str
    def __init__(self, book_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., isbn: _Optional[str] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ...) -> None: ...

class BookRetrieveRequest(_message.Message):
    __slots__ = ("book_id",)
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    def __init__(self, book_id: _Optional[str] = ...) -> None: ...

class BookStreamBooksByIDListRequest(_message.Message):
    __slots__ = ("book_ids",)
    BOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    book_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, book_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BookStreamBooksByIDListResponse(_message.Message):
    __slots__ = ("book",)
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: BookResponse
    def __init__(self, book: _Optional[_Union[BookResponse, _Mapping]] = ...) -> None: ...

class BookStreamRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JournalDestroyRequest(_message.Message):
    __slots__ = ("journal_id",)
    JOURNAL_ID_FIELD_NUMBER: _ClassVar[int]
    journal_id: str
    def __init__(self, journal_id: _Optional[str] = ...) -> None: ...

class JournalListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JournalListResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[JournalResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[JournalResponse, _Mapping]]] = ...) -> None: ...

class JournalPartialUpdateRequest(_message.Message):
    __slots__ = ("journal_id", "title", "authors", "categories", "publisher", "publication_date", "volume", "issue", "issn", "_partial_update_fields")
    JOURNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    ISSN_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    journal_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    publisher: str
    publication_date: str
    volume: int
    issue: int
    issn: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, journal_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ..., volume: _Optional[int] = ..., issue: _Optional[int] = ..., issn: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class JournalRequest(_message.Message):
    __slots__ = ("journal_id", "title", "authors", "categories", "publisher", "publication_date", "volume", "issue", "issn")
    JOURNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    ISSN_FIELD_NUMBER: _ClassVar[int]
    journal_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    publisher: str
    publication_date: str
    volume: int
    issue: int
    issn: str
    def __init__(self, journal_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ..., volume: _Optional[int] = ..., issue: _Optional[int] = ..., issn: _Optional[str] = ...) -> None: ...

class JournalResponse(_message.Message):
    __slots__ = ("journal_id", "title", "authors", "categories", "publisher", "publication_date", "volume", "issue", "issn")
    JOURNAL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHORS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    ISSN_FIELD_NUMBER: _ClassVar[int]
    journal_id: str
    title: str
    authors: _containers.RepeatedScalarFieldContainer[str]
    categories: _containers.RepeatedScalarFieldContainer[str]
    publisher: str
    publication_date: str
    volume: int
    issue: int
    issn: str
    def __init__(self, journal_id: _Optional[str] = ..., title: _Optional[str] = ..., authors: _Optional[_Iterable[str]] = ..., categories: _Optional[_Iterable[str]] = ..., publisher: _Optional[str] = ..., publication_date: _Optional[str] = ..., volume: _Optional[int] = ..., issue: _Optional[int] = ..., issn: _Optional[str] = ...) -> None: ...

class JournalRetrieveRequest(_message.Message):
    __slots__ = ("journal_id",)
    JOURNAL_ID_FIELD_NUMBER: _ClassVar[int]
    journal_id: str
    def __init__(self, journal_id: _Optional[str] = ...) -> None: ...

class PublicationCategoryDestroyRequest(_message.Message):
    __slots__ = ("category_id",)
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class PublicationCategoryListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublicationCategoryListResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PublicationCategoryResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[PublicationCategoryResponse, _Mapping]]] = ...) -> None: ...

class PublicationCategoryPartialUpdateRequest(_message.Message):
    __slots__ = ("category_id", "name", "_partial_update_fields")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    name: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, category_id: _Optional[str] = ..., name: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class PublicationCategoryRequest(_message.Message):
    __slots__ = ("category_id", "name")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    name: str
    def __init__(self, category_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PublicationCategoryResponse(_message.Message):
    __slots__ = ("category_id", "name")
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    name: str
    def __init__(self, category_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PublicationCategoryRetrieveRequest(_message.Message):
    __slots__ = ("category_id",)
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class PublisherDestroyRequest(_message.Message):
    __slots__ = ("publisher_id",)
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    publisher_id: str
    def __init__(self, publisher_id: _Optional[str] = ...) -> None: ...

class PublisherListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublisherListResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[PublisherResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[PublisherResponse, _Mapping]]] = ...) -> None: ...

class PublisherPartialUpdateRequest(_message.Message):
    __slots__ = ("publisher_id", "name", "address", "city", "state_province", "country", "website", "_partial_update_fields")
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_PROVINCE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    publisher_id: str
    name: str
    address: str
    city: str
    state_province: str
    country: str
    website: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, publisher_id: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state_province: _Optional[str] = ..., country: _Optional[str] = ..., website: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class PublisherRequest(_message.Message):
    __slots__ = ("publisher_id", "name", "address", "city", "state_province", "country", "website")
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_PROVINCE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    publisher_id: str
    name: str
    address: str
    city: str
    state_province: str
    country: str
    website: str
    def __init__(self, publisher_id: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state_province: _Optional[str] = ..., country: _Optional[str] = ..., website: _Optional[str] = ...) -> None: ...

class PublisherResponse(_message.Message):
    __slots__ = ("publisher_id", "name", "address", "city", "state_province", "country", "website")
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_PROVINCE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    publisher_id: str
    name: str
    address: str
    city: str
    state_province: str
    country: str
    website: str
    def __init__(self, publisher_id: _Optional[str] = ..., name: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ..., state_province: _Optional[str] = ..., country: _Optional[str] = ..., website: _Optional[str] = ...) -> None: ...

class PublisherRetrieveRequest(_message.Message):
    __slots__ = ("publisher_id",)
    PUBLISHER_ID_FIELD_NUMBER: _ClassVar[int]
    publisher_id: str
    def __init__(self, publisher_id: _Optional[str] = ...) -> None: ...
