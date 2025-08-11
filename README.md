# Spotify playlists

Playlists on Spotify are opaque.
To work around this problem,
use [Exportify](https://github.com/watsonbox/exportify)
to export my playlists to CSV.
I can then convert them to something more readable, like YAML.

**The Process:**

* Exportify is a submodule; update && change to repo directory
* Start a python webserver:

      python -m http.server

* Open Exportify at http://localhost:8000/exportify.html
* Download selected playlists as CSV
* Run script to convert them to YAML

Also included is a demo notebook that I used for prototyping.
