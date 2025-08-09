# Spotify playlists

Playlists on Spotify are opaque.
To work around this problem,
use [Exportify](https://github.com/watsonbox/exportify)
to export my playlists to csv.
I can then convert them to yaml
with the script **playlist-to-yaml.py**.

**The Process:**

* Exportify is a submodule; update && change to repo directory
* Start a python webserver:

      python -m http.server

* Open Exportify at http://localhost:8000/exportify.html
* Download exported playlists as csv
* Run script to convert them to yaml

I've included a demo notebook, **spotify-csv-to-yaml.ipynb**.
