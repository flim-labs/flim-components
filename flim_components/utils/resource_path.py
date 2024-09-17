import importlib.resources as pkg_resources


def get_asset_path(asset_name: str) -> str:
    return str(pkg_resources.files("flim_components").joinpath(asset_name))
