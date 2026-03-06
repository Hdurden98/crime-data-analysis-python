import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LOAD DATA
# =========================
file_path = "Crime_incidents_in_2025.csv"
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())
print("\nDataset shape:")
print(df.shape)
print("\nColumn names:")
print(df.columns.tolist())


# =========================
# 2. CLEAN COLUMN NAMES
# =========================
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
    .str.replace("-", "_")
)

print("\nCleaned column names:")
print(df.columns.tolist())


# =========================
# 3. HELPER FUNCTION TO FIND COLUMNS
# =========================
def find_column(possible_names):
    for col in df.columns:
        if col in possible_names:
            return col
    return None


offense_col = find_column(["offense", "crime_type", "incident_type"])
date_col = find_column(["report_date", "start_date", "end_date", "reportdatetime", "report_datetime"])
shift_col = find_column(["shift"])
ward_col = find_column(["ward"])
district_col = find_column(["district"])
method_col = find_column(["method"])
block_col = find_column(["block"])
neighborhood_col = find_column(["neighborhood_cluster", "neighborhood"])
psa_col = find_column(["psa", "police_service_area"])

print("\nDetected columns:")
print("offense_col:", offense_col)
print("date_col:", date_col)
print("shift_col:", shift_col)
print("ward_col:", ward_col)
print("district_col:", district_col)
print("method_col:", method_col)
print("block_col:", block_col)
print("neighborhood_col:", neighborhood_col)
print("psa_col:", psa_col)


# =========================
# 4. BASIC INFO
# =========================
print("\nData info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe(include="all"))


# =========================
# 5. TOP CRIME TYPES
# =========================
if offense_col:
    top_offenses = df[offense_col].value_counts().head(10)
    print("\nTop 10 crime types:")
    print(top_offenses)

    plt.figure(figsize=(10, 6))
    top_offenses.plot(kind="bar")
    plt.title("Top 10 Crime Types")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 6. CRIMES BY SHIFT
# =========================
if shift_col:
    shift_counts = df[shift_col].value_counts()
    print("\nCrime incidents by shift:")
    print(shift_counts)

    plt.figure(figsize=(8, 5))
    shift_counts.plot(kind="bar")
    plt.title("Crime Incidents by Shift")
    plt.xlabel("Shift")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# 7. CRIMES BY WARD
# =========================
if ward_col:
    ward_counts = df[ward_col].value_counts().sort_index()
    print("\nCrime incidents by ward:")
    print(ward_counts)

    plt.figure(figsize=(8, 5))
    ward_counts.plot(kind="bar")
    plt.title("Crime Incidents by Ward")
    plt.xlabel("Ward")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# 8. CRIMES BY DISTRICT
# =========================
if district_col:
    district_counts = df[district_col].value_counts().sort_values(ascending=False)
    print("\nCrime incidents by district:")
    print(district_counts)

    plt.figure(figsize=(8, 5))
    district_counts.plot(kind="bar")
    plt.title("Crime Incidents by District")
    plt.xlabel("District")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# 9. TOP METHODS
# =========================
if method_col:
    method_counts = df[method_col].value_counts().head(10)
    print("\nTop crime methods:")
    print(method_counts)

    plt.figure(figsize=(10, 6))
    method_counts.plot(kind="bar")
    plt.title("Top 10 Crime Methods")
    plt.xlabel("Method")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 10. TOP NEIGHBORHOODS
# =========================
if neighborhood_col:
    neighborhood_counts = df[neighborhood_col].value_counts().head(10)
    print("\nTop 10 neighborhoods by incidents:")
    print(neighborhood_counts)

    plt.figure(figsize=(10, 6))
    neighborhood_counts.plot(kind="bar")
    plt.title("Top 10 Neighborhoods by Crime Incidents")
    plt.xlabel("Neighborhood")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 11. TOP BLOCKS
# =========================
if block_col:
    block_counts = df[block_col].value_counts().head(10)
    print("\nTop 10 blocks by incidents:")
    print(block_counts)

    plt.figure(figsize=(10, 6))
    block_counts.plot(kind="bar")
    plt.title("Top 10 Blocks by Crime Incidents")
    plt.xlabel("Block")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 12. MONTHLY CRIME TREND
# =========================
if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    df["month"] = df[date_col].dt.month
    df["day_name"] = df[date_col].dt.day_name()

    monthly_counts = df["month"].value_counts().sort_index()
    print("\nCrime incidents by month:")
    print(monthly_counts)

    plt.figure(figsize=(8, 5))
    monthly_counts.plot(kind="line", marker="o")
    plt.title("Crime Incidents by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Incidents")
    plt.tight_layout()
    plt.show()

    daily_counts = df["day_name"].value_counts().reindex(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )
    print("\nCrime incidents by day of week:")
    print(daily_counts)

    plt.figure(figsize=(9, 5))
    daily_counts.plot(kind="bar")
    plt.title("Crime Incidents by Day of Week")
    plt.xlabel("Day")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# =========================
# 13. OFFENSE BY SHIFT
# =========================
if offense_col and shift_col:
    offense_shift = pd.crosstab(df[offense_col], df[shift_col])

    print("\nCrime type by shift:")
    print(offense_shift.head(10))

    top_offense_names = df[offense_col].value_counts().head(10).index
    offense_shift_top = pd.crosstab(df[df[offense_col].isin(top_offense_names)][offense_col],
                                    df[df[offense_col].isin(top_offense_names)][shift_col])

    offense_shift_top.plot(kind="bar", figsize=(12, 6))
    plt.title("Top Crime Types by Shift")
    plt.xlabel("Crime Type")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 14. OFFENSE BY WARD
# =========================
if offense_col and ward_col:
    top_offense_names = df[offense_col].value_counts().head(5).index
    filtered = df[df[offense_col].isin(top_offense_names)]

    offense_ward = pd.crosstab(filtered[ward_col], filtered[offense_col])
    print("\nTop offenses by ward:")
    print(offense_ward)

    offense_ward.plot(kind="bar", figsize=(12, 6))
    plt.title("Top Offenses by Ward")
    plt.xlabel("Ward")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# =========================
# 15. POLICE SERVICE AREA ANALYSIS
# =========================
if psa_col:
    psa_counts = df[psa_col].value_counts().head(10)
    print("\nTop 10 Police Service Areas by incidents:")
    print(psa_counts)

    plt.figure(figsize=(10, 6))
    psa_counts.plot(kind="bar")
    plt.title("Top 10 Police Service Areas by Crime Incidents")
    plt.xlabel("PSA")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# =========================
# 16. SAVE CLEANED COPY
# =========================
df.to_csv("crime_incidents_2025_cleaned.csv", index=False)
print("\nCleaned dataset saved as crime_incidents_2025_cleaned.csv")


# =========================
# 17. SIMPLE INSIGHTS OUTPUT
# =========================
print("\n--- Key Insights Template ---")
print("1. Identify the most common offense types from the Top 10 Crime Types chart.")
print("2. Use the district and ward charts to describe where incidents are concentrated.")
print("3. Use the monthly trend chart to describe whether incidents rise or fall over time.")
print("4. Use the shift chart to explain whether crimes happen more often during certain shifts.")
print("5. Use the neighborhood / block / PSA charts to highlight local hotspots.")
