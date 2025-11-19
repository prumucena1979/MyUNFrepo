"""
LOADcsvdataset.py
Simple module for loading CSV datasets from the DataSets folder
"""

import pandas as pd
import numpy as np
import os

# Default dataset path
DATASET_PATH = r"C:\Users\fabio\OneDrive - GUSCanada\VSCODEGIT\MOOC\DataSets"

def loadCsvDataSet(dataset_name):
    """
    Main function to load a dataset - designed for notebook use
    
    Args:
        dataset_name (str): Name of the dataset file (e.g., 'research.csv')
    
    Returns:
        pandas.DataFrame: Loaded dataset with basic info displayed
    """
    # Construct full path
    file_path = os.path.join(DATASET_PATH, dataset_name)
    
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
        
        # Display basic information
        print(f"✅ Dataset '{dataset_name}' loaded successfully!")
        print(f"📁 Path: {file_path}")
        print(f"📊 Shape: {data.shape} (rows: {data.shape[0]}, columns: {data.shape[1]})")
        print(f"📋 Columns: {list(data.columns)}")
        
        # Show first few rows
        print(f"\n🔍 First 3 rows:")
        print(data.head(3))
        
        # Check for missing values
        missing = data.isnull().sum()
        if missing.sum() > 0:
            print(f"\n⚠️  Missing values found:")
            print(missing[missing > 0])
        else:
            print(f"\n✅ No missing values found")
            
        return data
        
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        print(f"📁 Make sure the file exists in: {DATASET_PATH}")
        return None
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def show_info(data):
    """
    Display detailed information about the dataset
    
    Args:
        data (pandas.DataFrame): Dataset to analyze
    """
    if data is not None:
        print("\n📊 === DETAILED DATASET INFORMATION ===")
        print(f"📏 Shape: {data.shape}")
        print(f"📋 Columns: {list(data.columns)}")
        print(f"\n🔤 Data Types:")
        print(data.dtypes)
        print(f"\n❓ Missing Values:")
        missing = data.isnull().sum()
        print(missing)
        print(f"\n📈 Basic Statistics:")
        print(data.describe())
        print(f"\n👀 First 5 rows:")
        print(data.head())
    else:
        print("❌ No data provided")

def quick_clean(data):
    """
    Quick dataset cleaning
    
    Args:
        data (pandas.DataFrame): Dataset to clean
    
    Returns:
        pandas.DataFrame: Cleaned dataset
    """
    if data is not None:
        original_shape = data.shape
        
        # Remove duplicates
        data_cleaned = data.drop_duplicates()
        
        print(f"🧹 CLEANING RESULTS:")
        print(f"📏 Original shape: {original_shape}")
        print(f"📏 After removing duplicates: {data_cleaned.shape}")
        print(f"🗑️  Removed {original_shape[0] - data_cleaned.shape[0]} duplicate rows")
        
        return data_cleaned
    return None

def list_datasets():
    """
    List all available datasets in the DataSets folder
    
    Returns:
        list: List of CSV files available
    """
    if os.path.exists(DATASET_PATH):
        files = []
        for file in os.listdir(DATASET_PATH):
            if file.endswith('.csv'):
                files.append(file)
        
        if files:
            print(f"📂 Available CSV datasets in DataSets folder:")
            for i, file in enumerate(files, 1):
                print(f"   {i}. {file}")
        else:
            print(f"❌ No CSV files found in {DATASET_PATH}")
        
        return files
    else:
        print(f"❌ Dataset folder does not exist: {DATASET_PATH}")
        return []

def get_path():
    """
    Get the current dataset folder path
    
    Returns:
        str: Current dataset path
    """
    return DATASET_PATH

# Example usage
if __name__ == "__main__":
    print("📚 LOADcsvdataset module - Simple CSV dataset loader")
    print(f"📁 Dataset folder: {DATASET_PATH}")
    print()
    print("🔥 MAIN FUNCTION FOR NOTEBOOKS:")
    print("   data = loadCsvDataSet('research.csv')")
    print()
    print("🔧 UTILITY FUNCTIONS:")
    print("   list_datasets()           # Show available CSV files")
    print("   show_info(data)           # Detailed dataset information")
    print("   quick_clean(data)         # Basic data cleaning")
    print("   get_path()                # Get dataset folder path")
    print()
    
    # Show available datasets if directory exists
    list_datasets()