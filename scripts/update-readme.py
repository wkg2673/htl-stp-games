from pathlib import Path

contributors_file = Path("src/assets/contributors")
readme_file = Path("README.md")

contributors = contributors_file.read_text().splitlines()

contributor_list = "\n".join(
    f"- {name.strip()}"
    for name in contributors
    if name.strip()
)

readme = readme_file.read_text()

start = "<!-- CONTRIBUTORS_START -->"
end = "<!-- CONTRIBUTORS_END -->"

before, remainder = readme.split(start)
_, after = remainder.split(end)

updated_readme = (
    before
    + start
    + "\n"
    + contributor_list
    + "\n"
    + end
    + after
)

readme_file.write_text(updated_readme)