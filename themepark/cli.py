import click
import requests

from . import __version__
from .constants import REQUEST_URL
from .utils import pretty_print

headers = {
    "accept": "application/json;api-version=6.1-preview.1;excludeUrls=true",
    "content-type": "application/json",
}

body = {
    "filters": [
        {
            "criteria": [
                {"filterType": 8, "value": "Microsoft.VisualStudio.Code"},
                {"filterType": 10, "value": 'target:"Microsoft.VisualStudio.Code" '},
                {"filterType": 12, "value": "37888"},
                {"filterType": 5, "value": "Themes"},
            ],
            "direction": 2,
            "sortBy": 4,  # Sort By: Installs
            "sortOrder": 0,
            "pageNumber": 1,
            "pageSize": 1,
        }
    ],
    "flags": 870,
}


@click.command()
@click.version_option(version=__version__)
def main():
    """A Python CLI to choose and set a random VS Code theme for a project."""
    # More info:
    # - https://docs.python-requests.org/en/latest/user/advanced/#session-objects
    # - https://github.com/jschr/vscodethemes/issues/197
    # - https://github.com/jschr/vscodethemes/blob/dev/backend/jobs/scrapeExtensions.ts#L84
    # - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    with requests.Session() as s:
        r = s.post(REQUEST_URL, headers=headers, json=body)
        # click.echo(r.status_code)

    pretty_print(r.json())
