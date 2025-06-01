from invoke import task


@task()
def init(ctx):
    """Configure the dev environment."""

    for hook in ["pre-commit", "commit-msg"]:
        ctx.run(f"pre-commit install --hook-type {hook}")

    ctx.run("uv sync")
    ctx.run("uv run ./src/manage.py migrate", pty=True)
    ctx.run("uv run ./src/manage.py createsuperuser", pty=True)

