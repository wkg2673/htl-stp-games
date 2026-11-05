from pathlib import Path

contributors_file = Path("src/assets/contributors")
readme_file = Path("README.md")

contributors = contributors_file.read_text().splitlines()

contributor_list = "\n".join(
    f"[{parts[0].strip()}]({parts[1].strip()})"
    for line in contributors
    if line.strip()
    for parts in [line.split(" - ", 1)]
    if len(parts) == 2
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