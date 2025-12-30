import os

import os
import csv
from datetime import datetime

def save_list_to_csv(data_list,excel_file_path):
    """
    Saves a list to a CSV file in the given output folder.

    Args:
        data_list (list): The list of data to save.
        output_folder (str): Path to the folder where CSV will be saved.
        filename (str, optional): Name of the CSV file. If None, auto-generated.
    
    Returns:
        str: Path of the saved CSV file.
    """
    # Ensure output folder exists
    # os.makedirs(output_folder, exist_ok=True)

    # Auto-generate filename if not provided
    # if filename is None:
    #     filename = f"list_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # file_path = os.path.join(output_folder, filename)

    # Write list to CSV
    try:
        with open(excel_file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(data_list)
    # Each list element goes in a new row
    except Exception as e:
        print("Error_num-1004: error in save_list_to_csv",e)
    else:
        return excel_file_path
if __name__=="__main__":
    my_list = ["Apple", "Banana", "Cherry", "Date"]
    folder_path = r"C:\VikasData\Output"  # Change to your path
    csv_file = save_list_to_csv(my_list, folder_path)
    print(f"CSV file saved at: {csv_file}")
