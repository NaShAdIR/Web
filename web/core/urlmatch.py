__all__ = [
    'correct_url',
    'is_var',
    'var_parser',
    'split_into_catalogs',
    'pattern_matching'
]

from typing import Union


def correct_url(url: str, separator: str) -> str:
    if url.startswith(separator):
        url = url[1:]
    if url.endswith(separator):
        url = url[:-1]

    return url


def is_var(catalog: str) -> bool:
    return (catalog.startswith('<')
            and catalog.endswith('>'))


def var_parser(catalog: str) -> Union[str, None]:
    if is_var(catalog):
        return catalog[1:][:-1]

    return None


def split_into_catalogs(
        path: str,
        separator: str
) -> list[str]:
    return (
        correct_url(path, separator)
        .split(separator)
    )


def pattern_matching(
        url: str,
        pattern: str,
        separator: str
) -> dict:
    """
    Matches the url with the pattern and
    if there is a match, returns a dictionary of variables.

    patterns:
        'good/<path>' == (
            good/name,
            good/...
        ) -> {'path': ...}

        'good/<path>/<var>' == (
            good/name/age,
            good/.../...
        ) -> {'path': ..., 'var': ...}
    """
    url_catalogs = split_into_catalogs(url, separator)
    pattern_catalogs = split_into_catalogs(pattern, separator)
    coincidence = []
    variables = {}

    if len(url_catalogs) == len(pattern_catalogs):
        for index, (url_catalog, pattern_catalog) in (
                enumerate(
                    zip(url_catalogs,
                        pattern_catalogs)
                )
        ):
            if url_catalog == pattern_catalog:
                coincidence.append(True)
            elif is_var(pattern_catalog) and len(coincidence) == index:
                if var_name := var_parser(pattern_catalog):
                    variables[var_name] = url_catalog
                    coincidence.append(True)
                else:
                    return {}

    return variables
