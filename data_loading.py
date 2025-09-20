import pandas as pd
import os

def load_data_to_csv(df: pd.DataFrame, file_path: str):
    """
    Saves a pandas DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_path (str): The full path to the output CSV file.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Data successfully loaded to {file_path}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

if __name__ == '__main__':
    # Example usage with a sample DataFrame
    data = {'ID': [1, 2, 3], 'Product': ['A', 'B', 'C'], 'Price': [100, 200, 300]}
    sample_df = pd.DataFrame(data)
    
    # Define a folder to save the output file
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    output_file_path = os.path.join(output_dir, 'products.csv')
    
    # Save the sample data
    load_data_to_csv(sample_df, output_file_path)

    # Verify the file was created
    if os.path.exists(output_file_path):
        print("Verification: File exists. Content:")
        loaded_df = pd.read_csv(output_file_path)
        print(loaded_df)
