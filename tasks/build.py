from invoke import task


@task(aliases=("scan",))
def scan_image(ctx):
    """Scan turbine:latest image with ggshield."""
    ctx.run("poetry run ggshield secret scan docker turbine:latest")


@task(post=[scan_image], help={"clean": "Clean build without caching"})
def docker(ctx, clean=False):
    """Build a docker image and scan it"""
    ctx.run("poetry export -f requirements.txt > requirements.txt")

    ctx.run(f"docker build {'--no-cache' if clean else ''} --tag turbine:latest .")
