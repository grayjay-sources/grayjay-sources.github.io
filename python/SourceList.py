import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, List, Optional, Type, TypeVar, Union, cast
from uuid import UUID

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_stringified_bool(x: str) -> bool:
    if x == "true":
        return True
    if x == "false":
        return False
    assert False


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class DomainHeadersToFind:
    twitch_tv: Optional[List[str]] = None
    youtube_com: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> "DomainHeadersToFind":
        assert isinstance(obj, dict)
        twitch_tv = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get(".twitch.tv")
        )
        youtube_com = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get(".youtube.com")
        )
        return DomainHeadersToFind(twitch_tv, youtube_com)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.twitch_tv is not None:
            result[".twitch.tv"] = from_union(
                [lambda x: from_list(from_str, x), from_none], self.twitch_tv
            )
        if self.youtube_com is not None:
            result[".youtube.com"] = from_union(
                [lambda x: from_list(from_str, x), from_none], self.youtube_com
            )
        return result


@dataclass
class Authentication:
    login_url: str
    user_agent: Optional[str] = None
    cookies_to_find: Optional[List[str]] = None
    headers_to_find: Optional[List[str]] = None
    cookies_excl_others: Optional[bool] = None
    completion_url: Optional[str] = None
    login_button: Optional[str] = None
    domain_headers_to_find: Optional[DomainHeadersToFind] = None
    login_warning: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Authentication":
        assert isinstance(obj, dict)
        login_url = from_str(obj.get("loginUrl"))
        user_agent = from_union([from_str, from_none], obj.get("userAgent"))
        cookies_to_find = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("cookiesToFind")
        )
        headers_to_find = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("headersToFind")
        )
        cookies_excl_others = from_union(
            [from_bool, from_none], obj.get("cookiesExclOthers")
        )
        completion_url = from_union([from_str, from_none], obj.get("completionUrl"))
        login_button = from_union([from_str, from_none], obj.get("loginButton"))
        domain_headers_to_find = from_union(
            [DomainHeadersToFind.from_dict, from_none], obj.get("domainHeadersToFind")
        )
        login_warning = from_union([from_str, from_none], obj.get("loginWarning"))
        return Authentication(
            login_url,
            user_agent,
            cookies_to_find,
            headers_to_find,
            cookies_excl_others,
            completion_url,
            login_button,
            domain_headers_to_find,
            login_warning,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["loginUrl"] = from_str(self.login_url)
        if self.user_agent is not None:
            result["userAgent"] = from_union([from_str, from_none], self.user_agent)
        if self.cookies_to_find is not None:
            result["cookiesToFind"] = from_union(
                [lambda x: from_list(from_str, x), from_none], self.cookies_to_find
            )
        if self.headers_to_find is not None:
            result["headersToFind"] = from_union(
                [lambda x: from_list(from_str, x), from_none], self.headers_to_find
            )
        if self.cookies_excl_others is not None:
            result["cookiesExclOthers"] = from_union(
                [from_bool, from_none], self.cookies_excl_others
            )
        if self.completion_url is not None:
            result["completionUrl"] = from_union(
                [from_str, from_none], self.completion_url
            )
        if self.login_button is not None:
            result["loginButton"] = from_union([from_str, from_none], self.login_button)
        if self.domain_headers_to_find is not None:
            result["domainHeadersToFind"] = from_union(
                [lambda x: to_class(DomainHeadersToFind, x), from_none],
                self.domain_headers_to_find,
            )
        if self.login_warning is not None:
            result["loginWarning"] = from_union(
                [from_str, from_none], self.login_warning
            )
        return result


@dataclass
class CAPTCHA:
    user_agent: str
    captcha_url: None
    cookies_to_find: List[str]

    @staticmethod
    def from_dict(obj: Any) -> "CAPTCHA":
        assert isinstance(obj, dict)
        user_agent = from_str(obj.get("userAgent"))
        captcha_url = from_none(obj.get("captchaUrl"))
        cookies_to_find = from_list(from_str, obj.get("cookiesToFind"))
        return CAPTCHA(user_agent, captcha_url, cookies_to_find)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userAgent"] = from_str(self.user_agent)
        result["captchaUrl"] = from_none(self.captcha_url)
        result["cookiesToFind"] = from_list(from_str, self.cookies_to_find)
        return result


@dataclass
class Constants:
    base_url: str

    @staticmethod
    def from_dict(obj: Any) -> "Constants":
        assert isinstance(obj, dict)
        base_url = from_str(obj.get("baseUrl"))
        return Constants(base_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["baseUrl"] = from_str(self.base_url)
        return result


@dataclass
class CustomButton:
    text: str
    url: str
    classes: str

    @staticmethod
    def from_dict(obj: Any) -> "CustomButton":
        assert isinstance(obj, dict)
        text = from_str(obj.get("text"))
        url = from_str(obj.get("url"))
        classes = from_str(obj.get("classes"))
        return CustomButton(text, url, classes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_str(self.text)
        result["url"] = from_str(self.url)
        result["classes"] = from_str(self.classes)
        return result


class Package(Enum):
    DOM_PARSER = "DOMParser"
    HTTP = "Http"
    UTILITIES = "Utilities"


class TypeEnum(Enum):
    BOOLEAN = "Boolean"
    DROPDOWN = "Dropdown"
    HEADER = "Header"


@dataclass
class Setting:
    variable: str
    name: str
    description: str
    type: TypeEnum
    default: Optional[Union[int, bool]] = None
    options: Optional[List[str]] = None
    warning_dialog: Optional[str] = None
    dependency: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Setting":
        assert isinstance(obj, dict)
        variable = from_str(obj.get("variable"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        type = TypeEnum(obj.get("type"))
        default = from_union(
            [
                from_none,
                lambda x: from_union(
                    [from_stringified_bool, lambda x: int(x)], from_str(x)
                ),
            ],
            obj.get("default"),
        )
        options = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("options")
        )
        warning_dialog = from_union([from_str, from_none], obj.get("warningDialog"))
        dependency = from_union([from_str, from_none], obj.get("dependency"))
        return Setting(
            variable,
            name,
            description,
            type,
            default,
            options,
            warning_dialog,
            dependency,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["variable"] = from_str(self.variable)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["type"] = to_enum(TypeEnum, self.type)
        if self.default is not None:
            result["default"] = from_union(
                [
                    lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(bool, x))(x)).lower())(x)
                    ),
                    lambda x: from_str(
                        (lambda x: str((lambda x: is_type(int, x))(x)))(x)
                    ),
                ],
                self.default,
            )
        if self.options is not None:
            result["options"] = from_union(
                [lambda x: from_list(from_str, x), from_none], self.options
            )
        if self.warning_dialog is not None:
            result["warningDialog"] = from_union(
                [from_str, from_none], self.warning_dialog
            )
        if self.dependency is not None:
            result["dependency"] = from_union([from_str, from_none], self.dependency)
        return result


@dataclass
class Feeds:
    commits: Optional[str]
    releases: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "Feeds":
        assert isinstance(obj, dict)
        commits = from_union([from_str, from_none], obj.get("commits"))
        releases = from_union([from_str, from_none], obj.get("releases"))
        return Feeds(commits, releases)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.commits is not None:
            result["commits"] = from_union([from_str, from_none], self.commits)
        if self.releases is not None:
            result["releases"] = from_union([from_str, from_none], self.releases)
        return result


@dataclass
class SourceListElement:
    name: str
    description: str
    author: str
    author_url: str
    source_url: str
    repository_url: str
    script_url: str
    version: int
    icon_url: str
    id: UUID
    packages: List[Package]
    allow_eval: bool
    allow_urls: List[str]
    tags: List[str]
    script_signature: Optional[str] = None
    script_public_key: Optional[str] = None
    platform_url: Optional[str] = None
    authentication: Optional[Authentication] = None
    settings: Optional[List[Setting]] = None
    supported_claim_types: Optional[List[int]] = None
    constants: Optional[Constants] = None
    custom_buttons: Optional[List[CustomButton]] = None
    source_list_icon_url: Optional[str] = None
    nsfw: Optional[bool] = None
    source_list_source_url: Optional[str] = None
    allow_all_http_header_access: Optional[bool] = None
    website_url: Optional[str] = None
    subscription_rate_limit: Optional[int] = None
    captcha: Optional[CAPTCHA] = None
    primary_claim_field_type: Optional[int] = None
    feeds: Optional[Feeds] = None

    @staticmethod
    def from_dict(obj: Any) -> "SourceListElement":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        author = from_str(obj.get("author"))
        author_url = from_str(obj.get("authorUrl"))
        source_url = from_str(obj.get("sourceUrl"))
        repository_url = from_str(obj.get("repositoryUrl"))
        script_url = from_str(obj.get("scriptUrl"))
        version = from_int(obj.get("version"))
        icon_url = from_str(obj.get("iconUrl"))
        id = UUID(obj.get("id"))
        packages = from_list(Package, obj.get("packages"))
        allow_eval = from_bool(obj.get("allowEval"))
        allow_urls = from_list(from_str, obj.get("allowUrls"))
        tags = from_list(from_str, obj.get("_tags"))
        script_signature = from_union([from_str, from_none], obj.get("scriptSignature"))
        script_public_key = from_union(
            [from_str, from_none], obj.get("scriptPublicKey")
        )
        platform_url = from_union([from_str, from_none], obj.get("platformUrl"))
        authentication = from_union(
            [Authentication.from_dict, from_none], obj.get("authentication")
        )
        settings = from_union(
            [lambda x: from_list(Setting.from_dict, x), from_none], obj.get("settings")
        )
        supported_claim_types = from_union(
            [lambda x: from_list(from_int, x), from_none],
            obj.get("supportedClaimTypes"),
        )
        constants = from_union([Constants.from_dict, from_none], obj.get("constants"))
        custom_buttons = from_union(
            [lambda x: from_list(CustomButton.from_dict, x), from_none],
            obj.get("_customButtons"),
        )
        source_list_icon_url = from_union([from_str, from_none], obj.get("iconUrl_"))
        nsfw = from_union([from_bool, from_none], obj.get("nsfw"))
        source_list_source_url = from_union(
            [from_str, from_none], obj.get("sourceUrl_")
        )
        allow_all_http_header_access = from_union(
            [from_bool, from_none], obj.get("allowAllHttpHeaderAccess")
        )
        website_url = from_union([from_str, from_none], obj.get("websiteUrl"))
        subscription_rate_limit = from_union(
            [from_int, from_none], obj.get("subscriptionRateLimit")
        )
        captcha = from_union([CAPTCHA.from_dict, from_none], obj.get("captcha"))
        primary_claim_field_type = from_union(
            [from_int, from_none], obj.get("primaryClaimFieldType")
        )
        feeds = Feeds.from_dict(obj.get("_feeds"))
        return SourceListElement(
            name,
            description,
            author,
            author_url,
            source_url,
            repository_url,
            script_url,
            version,
            icon_url,
            id,
            packages,
            allow_eval,
            allow_urls,
            tags,
            script_signature,
            script_public_key,
            platform_url,
            authentication,
            settings,
            supported_claim_types,
            constants,
            custom_buttons,
            source_list_icon_url,
            nsfw,
            source_list_source_url,
            allow_all_http_header_access,
            website_url,
            subscription_rate_limit,
            captcha,
            primary_claim_field_type,
            feeds,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["author"] = from_str(self.author)
        result["authorUrl"] = from_str(self.author_url)
        result["sourceUrl"] = from_str(self.source_url)
        result["repositoryUrl"] = from_str(self.repository_url)
        result["scriptUrl"] = from_str(self.script_url)
        result["version"] = from_int(self.version)
        result["iconUrl"] = from_str(self.icon_url)
        result["id"] = str(self.id)
        result["packages"] = from_list(lambda x: to_enum(Package, x), self.packages)
        result["allowEval"] = from_bool(self.allow_eval)
        result["allowUrls"] = from_list(from_str, self.allow_urls)
        if self.tags is not None:
            result["_tags"] = from_list(from_str, self.tags)
        if self.script_signature is not None:
            result["scriptSignature"] = from_union(
                [from_str, from_none], self.script_signature
            )
        if self.script_public_key is not None:
            result["scriptPublicKey"] = from_union(
                [from_str, from_none], self.script_public_key
            )
        if self.feeds is not None:
            result["_feeds"] = Feeds.to_dict(self.feeds)
        if self.platform_url is not None:
            result["platformUrl"] = from_union([from_str, from_none], self.platform_url)
        if self.authentication is not None:
            result["authentication"] = from_union(
                [lambda x: to_class(Authentication, x), from_none], self.authentication
            )
        if self.settings is not None:
            result["settings"] = from_union(
                [lambda x: from_list(lambda x: to_class(Setting, x), x), from_none],
                self.settings,
            )
        if self.supported_claim_types is not None:
            result["supportedClaimTypes"] = from_union(
                [lambda x: from_list(from_int, x), from_none],
                self.supported_claim_types,
            )
        if self.constants is not None:
            result["constants"] = from_union(
                [lambda x: to_class(Constants, x), from_none], self.constants
            )
        if self.custom_buttons is not None:
            result["_customButtons"] = from_union(
                [
                    lambda x: from_list(lambda x: to_class(CustomButton, x), x),
                    from_none,
                ],
                self.custom_buttons,
            )
        if self.source_list_icon_url is not None:
            result["iconUrl_"] = from_union(
                [from_str, from_none], self.source_list_icon_url
            )
        if self.nsfw is not None:
            result["nsfw"] = from_union([from_bool, from_none], self.nsfw)
        if self.source_list_source_url is not None:
            result["sourceUrl_"] = from_union(
                [from_str, from_none], self.source_list_source_url
            )
        if self.allow_all_http_header_access is not None:
            result["allowAllHttpHeaderAccess"] = from_union(
                [from_bool, from_none], self.allow_all_http_header_access
            )
        if self.website_url is not None:
            result["websiteUrl"] = from_union([from_str, from_none], self.website_url)
        if self.subscription_rate_limit is not None:
            result["subscriptionRateLimit"] = from_union(
                [from_int, from_none], self.subscription_rate_limit
            )
        if self.captcha is not None:
            result["captcha"] = from_union(
                [lambda x: to_class(CAPTCHA, x), from_none], self.captcha
            )
        if self.primary_claim_field_type is not None:
            result["primaryClaimFieldType"] = from_union(
                [from_int, from_none], self.primary_claim_field_type
            )
        return result


def source_list_from_dict(s: Any) -> List[SourceListElement]:
    return from_list(SourceListElement.from_dict, s)


def source_list_to_dict(x: List[SourceListElement]) -> Any:
    return from_list(lambda x: to_class(SourceListElement, x), x)


def source_list_from_file(json_path: str) -> List[SourceListElement]:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return source_list_from_dict(data)


def source_list_to_file(json_path: str, source_list: List[SourceListElement], indent=4):
    data = source_list_to_dict(source_list)
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent)


def dict_from_file(json_path: str) -> List[SourceListElement]:
    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


def dict_to_file(json_path: str, data: dict, indent=4):
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent)
