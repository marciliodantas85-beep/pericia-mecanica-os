from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


RENAMES = {
    "pericia-01-triagem-processual": "pericia-01-triagem-processual",
    "pericia-02-analise-documental": "pericia-02-analise-documental",
    "pericia-03-proposta-honorarios": "pericia-03-proposta-honorarios",
    "pericia-04-matriz-quesitos": "pericia-04-matriz-quesitos",
    "pericia-05-roteiro-diligencia": "pericia-05-roteiro-diligencia",
    "pericia-06-inventario-evidencias": "pericia-06-inventario-evidencias",
    "pericia-07-anexo-fotografico": "pericia-07-anexo-fotografico",
    "pericia-08-laudo-mecanico": "pericia-08-laudo-mecanico",
    "pericia-09-revisao-impugnacao": "pericia-09-revisao-impugnacao",
    "pericia-10-peticoes": "pericia-10-peticoes",
    "pericia-11-controle-prazos": "pericia-11-controle-prazos",
    "pericia-12-biblioteca-normas": "pericia-12-biblioteca-normas",
}


TEXT_EXTENSIONS = {".md", ".py", ".csv", ".txt", ".yaml", ".yml"}


def replace_text(path: Path):
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return
    try:
        text = path.read_text(encoding="utf-8-sig" if path.suffix.lower() == ".csv" else "utf-8")
    except UnicodeDecodeError:
        return

    new_text = text
    for old, new in RENAMES.items():
        new_text = new_text.replace(old, new)

    if new_text != text:
        encoding = "utf-8-sig" if path.suffix.lower() == ".csv" else "utf-8"
        path.write_text(new_text, encoding=encoding)


def rename_skill_dirs():
    skills_dir = ROOT / "skills"
    for old, new in RENAMES.items():
        old_path = skills_dir / old
        new_path = skills_dir / new
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)


def rename_matrix_files():
    for old, new in RENAMES.items():
        old_csv = ROOT / "skills" / new / "matrices" / f"{old}.csv"
        new_csv = ROOT / "skills" / new / "matrices" / f"{new}.csv"
        if old_csv.exists() and not new_csv.exists():
            old_csv.rename(new_csv)


def main():
    rename_skill_dirs()
    rename_matrix_files()
    for path in ROOT.rglob("*"):
        if path.is_file():
            replace_text(path)


if __name__ == "__main__":
    main()
