"""
Functions to aquire the zip files from the artificial data pilot page
"""

from typing import Literal
import zipfile
import shutil
import os
import io
import pathlib
import requests


DATA_PATH = pathlib.Path(__file__).parent.parent.parent / "data"
INPUT_PATH = DATA_PATH / "input"
ARTIFICIAL_HES_BASE_URL = "https://s3.eu-west-2.amazonaws.com/files.digital.nhs.uk/assets/Services/Artificial+data/Artificial+HES+final"  # pylint: disable=line-too-long


def download_zip_from_url(
    zip_file_url: str, overwrite: bool = False, output_path: pathlib.Path = None
) -> str:
    """Downloads a zipfile from the specified URL

    Parameters
    ----------
    zip_file_url : str
        The url string of where the zipfile is held
    overwrite : bool
        if True, then running this again will overwrite existing files of the same name, otherwise
        it will not.
    output_path : pathlib.Path
        Where you want the zip to be saved to - if left as "None" then it will be saved to
        "data/{filename}"

    Returns
    ----------
    output_path : pathlib.Path

    """
    filename = pathlib.Path(zip_file_url).stem

    if output_path is None:
        output_path = INPUT_PATH / filename
    if os.path.exists(output_path) and overwrite is True:
        shutil.rmtree(output_path, ignore_errors=False, onerror=None)
    elif os.path.exists(output_path) and overwrite is not True:
        raise FileExistsError(f"The zipfile already exists at: {output_path}")

    response = requests.get(zip_file_url, stream=True, timeout=3600)
    downloaded_zip = zipfile.ZipFile(io.BytesIO(response.content))
    downloaded_zip.extractall(output_path)
    return output_path


def download_artificial_hes_zip(
    dataset_name: Literal["ae", "apc", "op"],
    version: str = "202302_v1",
    size: Literal["sample", "full"] = "sample",
) -> pathlib.Path:
    """
    Download and unpack artificial hes zip file.

    Parameters
    ----------
    dataset_name : Literal["ae", "apc", "op"]
        Name of dataset to download.
    version : str, optional
        Version to download, by default "202302_v1"
    size : str, optional
        Size to download, by default "sample"

    Returns
    -------
    pathlib.Path
        Path to the downloaded file.
    """
    zip_name = f"artificial_hes_{dataset_name}_{version}_{size}.zip"
    zip_url = f"{ARTIFICIAL_HES_BASE_URL}/{zip_name}"
    zip_path = download_zip_from_url(zip_url, overwrite=True)
    return zip_path
