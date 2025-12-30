def save_in_txt_file(txt_input_data,txt_file_path):
     try:
        with open(txt_file_path, "w", encoding="utf-8") as f:
            # allow lists / tuples too
            if isinstance(txt_input_data, (list, tuple)):
                f.write("\n".join(map(str, txt_input_data)))
            else:
                f.write(str(txt_input_data))
            return txt_file_path
     except Exception as e:
        print("Error_num-1003: error in save_in_txt_file")
     else:
        return txt_file_path
if __name__=="__main__":
    txt_file_path=r"C:\VikasData\KiteConnect\temp\xyz.txt"
    txt_data="abc"
    output_file_path=save_in_txt_file(txt_data,txt_file_path)
    
    