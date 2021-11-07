import click
import json
from .lint.lint import Linter

def cli_message(linter):
    click.secho()
    click.secho("stac-check: STAC spec validaton and linting tool", bold=True)
    if linter.version == "1.0.0":
        click.secho(linter.update_msg, fg='green')
    else:
        click.secho(linter.update_msg, fg='red')
    click.secho(f"Validator: stac-validator {linter.validator_version}", bg="blue", fg="white")
    if linter.valid_stac == True:
        click.secho(f"Valid {linter.asset_type}: {linter.valid_stac}", fg='green')
    else:
        click.secho(f"Valid {linter.asset_type}: {linter.valid_stac}", fg='red')

    if len(linter.schema) > 0:
        click.secho("Schemas validated: ", fg="blue")
        for schema in linter.schema:
            click.secho(f"    {schema}")

    if linter.invalid_asset_format and len(linter.invalid_asset_format) > 0:
        click.secho("Asset format error(s): ", fg="red")
        for asset in linter.invalid_asset_format:
            click.secho(f"    {asset}")

    if linter.invalid_asset_request and len(linter.invalid_asset_request) > 0:
        click.secho("Asset request error(s): ", fg="red")
        for asset in linter.invalid_asset_request:
            click.secho(f"    {asset}")

    if linter.invalid_link_format and len(linter.invalid_link_format) > 0:
        click.secho("Link format error(s): ", fg="red")
        for link in linter.invalid_link_format:
            click.secho(f"    {link}")

    if linter.invalid_link_request and len(linter.invalid_link_request) > 0:
        click.secho("Link request error(s): ", fg="red")
        for link in linter.invalid_link_request:
            click.secho(f"    {link}")

    if linter.error_type != "":
        click.secho(f"Validation error type: ", fg="red")
        click.secho(f"    {linter.error_type}")

    if linter.error_msg != "":
        click.secho(f"Validation error message: ", fg='red')
        click.secho(f"    {linter.error_msg}")

    click.secho()

    ### Stac validator response for reference
    # click.secho(json.dumps(linter.message, indent=4))

@click.option(
    "-a", "--assets", is_flag=True, help="Validate assets for format and response."
)
@click.option(
    "-l", "--links", is_flag=True, help="Validate links for format and response."
)
@click.command()
@click.argument('file')
def main(file, assets, links):
    linter = Linter(file, assets, links)
    cli_message(linter)
