def clean_sales(df):
    """Drop rows with missing order IDs."""
    return df.dropna(subset=["ORDER_ID"])
