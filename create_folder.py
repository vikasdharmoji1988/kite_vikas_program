from pathlib import Path

def create_folder(folder_path:str):
    """
    Docstring for create_folder
    
    :param folder_path: Description
    :type folder_path: str
    """
    try:
        output_folder_path=Path(folder_path)
        output_folder_path.mkdir(parents=True,exist_ok=True)
        
    except Exception as e:
        print("Error_num-1001: error create folder:",e)
    else:
        return output_folder_path

if __name__=="__main__":
    x=create_folder(r"C:\VikasData\KiteConnect\OUT\trial")
    print(x)