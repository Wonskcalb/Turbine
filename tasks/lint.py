from invoke import task


@task(aliases=("ggs", "scan"))
def ggshield(ctx):
    ctx.run("uv run ggshield secret scan path --recursive --yes src")


@task()
def ruff(ctx):
    """
    Run ruff to lint the code. Reformats as well
    """
    ctx.run("uv run ruff check .")


@task(aliases=("fc", "check"), pre=[ggshield, ruff])
def full_check(_):
    pass
