# Preprocesamiento del dataset de noticias falsas
from pathlib import Path
import pandas as pd

SEED = 98
DATA_DIR = Path("Tools")
DATA_DIR_NEW = Path("Data/New")
OUTPUT_PATH = DATA_DIR / "dataset_Notices.csv"

FAKE_PATH = DATA_DIR / "Fake.csv"
REAL_PATH = DATA_DIR / "True.csv"

def load_and_label(path: Path, label: str) -> pd.DataFrame:
    """Carga un archivo de noticias y asigna su etiqueta."""
    df = pd.read_csv(path)

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()

    required = {"title", "text", "subject", "date"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"Faltan columnas en {path.name}: {sorted(missing)}"
        )

    df["label"] = label
    return df


# 1. Correspondiente al dataset en el que se encuentren los datos agregaremos una columna extra 
# 2. Para evitar algún patrón posible mezclaremos los datos 
def main():
    # 1. Cargar y etiquetar
    fake = load_and_label(FAKE_PATH, "Fake")
    real = load_and_label(REAL_PATH, "Real")

    # 2. Combinar ambos datasets
    df = pd.concat([fake, real], ignore_index=True)

    # 3. Verificar estructura y calidad
    print("Dimensiones iniciales:", df.shape)
    print("\nDistribución de clases:")
    print(df["label"].value_counts())
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("\nDuplicados exactos de filas:", df.duplicated().sum())

    # 4. Mezclar las filas de forma reproducible
    df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

    # 5. Guardar el dataset unificado
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("\nDataset guardado en:", OUTPUT_PATH)
    print("Dimensiones finales:", df.shape)


if __name__ == "__main__":
    main()