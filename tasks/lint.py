from invoke import task


@task(aliases=("ggs", "scan"))
def ggshield(ctx):
    ctx.run("poetry run ggshield secret scan path --recursive --yes src")


@task
def black(ctx):
    ctx.run("poetry run black .")


@task(pre=[black])
def ruff(ctx):
    """
    Run ruff to lint the code. Reformats with black beforehand
    """
    ctx.run("poetry run ruff check .")


@task(aliases=("fc", "check"), pre=[ggshield, black, ruff])
def full_check(_):
    pass
