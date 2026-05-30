import pandas as pd

df=pd.read_csv("SuperMarket Analysis.csv")

print("=" * 60)
print("資料筆數與欄位數")
print("=" * 60)

print(df.shape)

print("\n")
print("=" * 60)
print("前5筆資料")
print("=" * 60)

print(df.head())

filtered_df=df[
    (df["Branch"].str.startswith("A")) &
    (df["Customer type"] == "Member")
]

print("\n")
print("=" * 60)
print("Branch=A 且 Customer type=Member")
print("=" * 60)

print(filtered_df.head())

print(f"\n符合條件筆數：{len(filtered_df)}")

product_summary=(
    df.groupby("Product line")
      .agg(
          Total_Sales=("Sales", "sum"),
          Average_Rating=("Rating", "mean")
      )
      .reset_index()
)


product_summary["Total_Sales"]=(
    product_summary["Total_Sales"].round(2)
)

product_summary["Average_Rating"]=(
    product_summary["Average_Rating"].round(2)
)

print("\n")
print("=" * 60)
print("各產品線銷售與評分")
print("=" * 60)

print(product_summary)

city_gender_summary=(
    df.groupby(["City", "Gender"])
      .agg(
          Average_Sales=("Sales", "mean"),
          Transaction_Count=("Invoice ID", "count")
      )
      .reset_index()
)

city_gender_summary["Average_Sales"]=(
    city_gender_summary["Average_Sales"].round(2)
)

print("\n")
print("=" * 60)
print("City + Gender 分析")
print("=" * 60)

print(city_gender_summary)

top_product=product_summary.loc[
    product_summary["Total_Sales"].idxmax()
]

print("\n")
print("=" * 60)
print("總銷售額最高產品線")
print("=" * 60)

print(f"產品線：{top_product['Product line']}")
print(f"總銷售額：{top_product['Total_Sales']:.2f}")

product_summary.to_csv(
    "0520_pandas_3OK.CSV",
    index=False,
    encoding="utf-8-sig"
)

print("\n")
print("已輸出檔案：0520_pandas_3OK.CSV")