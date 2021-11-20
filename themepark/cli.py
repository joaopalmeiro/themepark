import click
import requests

from . import __version__
from .constants import REQUEST_URL, SORTING_OPTIONS
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
            "sortBy": SORTING_OPTIONS["installs"],
            "sortOrder": 0,
            "pageNumber": 1,
            "pageSize": 50,
        }
    ],
    "flags": 870,
}


@click.command()
@click.argument(
    "output_path",
    type=click.Path(
        exists=False, file_okay=False, dir_okay=True, writable=True, resolve_path=True
    ),
    default="./.vscode",
)
@click.version_option(version=__version__)
def main(output_path):
    """A Python CLI to choose and set a random VS Code theme for a project."""
    # More info:
    # - https://docs.python-requests.org/en/latest/user/advanced/#session-objects
    # - https://github.com/jschr/vscodethemes/issues/197
    # - https://github.com/jschr/vscodethemes/blob/dev/backend/jobs/scrapeExtensions.ts#L84
    # - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

    # click.echo(output_path)
    with requests.Session() as s:
        r = s.post(REQUEST_URL, headers=headers, json=body)
        # click.echo(r.status_code)
        extensions = r.json()["results"][0]["extensions"]

    pretty_print(extensions)
    # click.echo(len(extensions))
