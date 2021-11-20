from typing import Dict

REQUEST_URL: str = (
    "https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery"
)

SORTING_OPTIONS: Dict[str, int] = {
    "installs": 4,  # Sort By: Installs
    "trending": 8,  # Sort By: Trending
    "rating": 12,  # Sort By: Rating
}
