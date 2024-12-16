import pandas as pd

def transform_sales_data(sales_df):
    """Clean and transform sales data."""
    sales_df['order_date'] = pd.to_datetime(sales_df['order_date'])
    sales_df['total_price'] = sales_df['quantity'] * sales_df['unit_price']
    sales_df.dropna(inplace=True)
    return sales_df
