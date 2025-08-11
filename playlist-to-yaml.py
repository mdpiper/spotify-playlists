"""Convert Exportify Spotify playlists from csv to yaml."""
import os
import glob
import pandas
import pathlib
import yaml


year = "2025"
output_dir = "yaml"

os.makedirs(output_dir, exist_ok=True)
csv_files = glob.glob("*.csv", root_dir=year)

for playlist_file in csv_files:
    playlist_name, _ = os.path.splitext(playlist_file)
    yaml_file = f"{output_dir}/{playlist_name}.yaml"
    print(f"- {yaml_file}")

    playlist = pandas.read_csv(pathlib.Path(year) / playlist_file)
    playlist_dict = playlist.to_dict("index")

    with open(yaml_file, "w") as fp:
        fp.write(f"#\n# {playlist_name}\n#\n")
        yaml.safe_dump(playlist_dict, fp)
