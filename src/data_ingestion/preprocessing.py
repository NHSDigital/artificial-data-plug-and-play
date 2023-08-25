"""
Loads data into duckdb tables.
"""

import pathlib

from duckdb import DuckDBPyConnection

from ..utils import data_connections


def load_csvs_into_tables(
    conn: DuckDBPyConnection,
    data_dir: pathlib.Path,
    replace: bool = False,
    exists_ok: bool = True
) -> list[str]:
    """
    Create artificial hes tables in the duckdb instance 

    Args:
        conn (duckdb.DuckDBPyConnection): Database to create tables within
        data_dir (pathlib.Path): Directory containing csv data to load into tables
        replace (bool, optional): Determins ether tables should be replaced if they 
            exist already. Defaults to False.
        exists_ok (bool, optional): Determines whether an error will be raised if a 
            table already exists. Defaults to True.

    Returns:
        list[str]: Names of created tables
    """
    table_names = []

    for csv_path in data_dir.glob("**/*.csv"):
        table_name = data_connections.create_table_from_csv(
            conn,
            csv_path,
            replace=replace,
            exists_ok=exists_ok,
        )
        table_names.append(table_name)

    return table_names
