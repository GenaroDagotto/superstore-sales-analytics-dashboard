import pandas as pd
import sqlite3
from pathlib import Path

# -----------------------------
# 1) Paths (rutas de archivos)
# -----------------------------
# Esto busca la carpeta principal del proyecto automáticamente
project_root = Path(__file__).resolve().parent.parent

# Ruta al CSV original (raw)
raw_path = project_root / "data" / "raw" / "Superstore_Orders_2020-23_24F.csv"

# Carpeta de salida (processed)
processed_dir = project_root / "data" / "processed"
processed_dir.mkdir(parents=True, exist_ok=True)

# Archivos de salida
clean_csv_path = processed_dir / "superstore_clean.csv"
db_path = processed_dir / "superstore.db"

# -----------------------------
# 2) Leer CSV
# -----------------------------
print("Reading CSV...")
df = pd.read_csv(raw_path)

print("Original shape:", df.shape)
print("Columns:", list(df.columns))

# -----------------------------
# 3) Limpieza básica
# -----------------------------

# Estandarizar nombres de columnas (sin espacios)
df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# Eliminar duplicados exactos
df = df.drop_duplicates()

# Convertir fechas si existen estas columnas
for date_col in ["Order_Date", "Ship_Date"]:
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

# -----------------------------
# 4) Crear columnas útiles para análisis
# -----------------------------
if "Order_Date" in df.columns:
    df["Order_Year"] = df["Order_Date"].dt.year
    df["Order_Month"] = df["Order_Date"].dt.month
    df["Order_Month_Name"] = df["Order_Date"].dt.month_name()

if "Sales" in df.columns and "Profit" in df.columns:
    # Profit margin % (evitando división por cero)
    df["Profit_Margin_Pct"] = df.apply(
        lambda row: (row["Profit"] / row["Sales"] * 100) if pd.notnull(row["Sales"]) and row["Sales"] != 0 else None,
        axis=1
    )

if "Profit" in df.columns:
    # Marca si la orden fue con pérdida
    df["Is_Loss_Order"] = df["Profit"].apply(lambda x: 1 if pd.notnull(x) and x < 0 else 0)

# Rellenar vacíos en columnas de texto con "Unknown"
text_cols = df.select_dtypes(include=["object"]).columns
for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# -----------------------------
# 5) Guardar CSV limpio
# -----------------------------
df.to_csv(clean_csv_path, index=False)
print(f"Clean CSV saved to: {clean_csv_path}")

# -----------------------------
# 6) Guardar también en SQLite (SQL)
# -----------------------------
conn = sqlite3.connect(db_path)
df.to_sql("orders", conn, if_exists="replace", index=False)
conn.close()

print(f"SQLite DB saved to: {db_path}")
print("Final shape:", df.shape)
print("Done.")