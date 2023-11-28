import pathlib

YEAR = 2023

day_template = pathlib.Path('./day_XX.py').read_text()

for idx in range(1, 26):
    out_path = pathlib.Path(f'./solutions/day_{idx:02d}.py')
    out_path.parent.mkdir(exist_ok=True, parents=True)
    if not out_path.exists() or True:
        tmp = day_template.replace('YEAR_PLACEHOLDER', str(YEAR))
        tmp = tmp.replace('DAY_PLACEHOLDER', str(idx))
        with out_path.open('w') as f:
            f.write(tmp)
