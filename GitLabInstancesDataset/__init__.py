import typing
from pathlib import Path

__all__ = ("isGitLab",)


def _convertToTuple(s: str) -> typing.Tuple[str]:
	return tuple(el.lower() for el in reversed(s.split(".")) if el)


knownServicesFile = Path(__file__).parent.absolute() / "KnownGitLabInstances.txt"
knownServices = set(_convertToTuple(el) for el in knownServicesFile.read_text().splitlines())


def isGitLab(domain: typing.Union[str, tuple]) -> bool:
	"""Pass a domain name NOT CONTAINING the token `gitlab`, and get a boolean saying if it is present within the dataset"""

	if isinstance(domain, str):
		domain = _convertToTuple(domain)

	return domain in knownServices
