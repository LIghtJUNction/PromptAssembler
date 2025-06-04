import click
from pathlib import Path




@click.group()
def main():
    """Prompt Assembler CLI"""
    pass


@main.command()
@click.option("-s", "--source", required=True, help="Path to the source code.")
@click.option("-o", "--output", default="./build/", help="Path to the output files.")
@click.option("-t", "--type", type=click.Choice(['ProjectRefactoring','PR', 'BugRemediation','BR', 'StaticAnalysis','SA', 'TestCaseGeneration','TCG', 'CodeSanitization','CS'], case_sensitive=True), default='StaticAnalysis', help="Type of prompt to build.")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose output.")
def build(output: str, source: str, type: str, verbose: bool) -> None:
    """Build the prompt from the source code."""

    source_path : Path = Path(source)
    output_path : Path = Path(output)

    if not source_path.exists():
        raise click.ClickException(f"Source file {source_path} does not exist.")

    if not source_path.is_file():
        raise click.ClickException(f"Source path {source_path} is not a file.")

    output_path.mkdir(parents=True, exist_ok=True)

    # 生成中间件
    match type.lower():
        case 'projectrefactoring' | 'pr':
            click.echo("Building Project Refactoring prompt...")
        case 'bugremediation' | 'br':
            click.echo("Building Bug Remediation prompt...")
        case 'staticanalysis' | 'sa':
            click.echo("Building Static Analysis prompt...")
        case 'testcasegeneration' | 'tcg':
            click.echo("Building Test Case Generation prompt...")
        case 'codesanitization' | 'cs':
            click.echo("Building Code Sanitization prompt...")
        case _:
            raise click.ClickException(f"Unknown type {type}. Supported types are: ProjectRefactoring, BugRemediation, StaticAnalysis, TestCaseGeneration, CodeSanitization.")



@main.group()
def dev():
    """Development commands"""
    pass



@dev.command()
@click.option("-s", "--source", required=True, help="Path to the source code.")
@click.option("-o", "--output", default="./build/", help="Path to the output files.")
def 