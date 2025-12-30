import random



def get_unique_character_str(arleady_used:tuple,num_captial_char:int,num_lower_char:int,num_num_char:int,num_special_char):
    abc_capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc_lower="abcdefghijklmnopqrstuvwxyz"
    num_char="0123456789"
    special_char="!@#$%&+_-~"

    final_string=""
    
    for i in range(num_captial_char):
     final_string=final_string+random.choice(abc_capital)
    
    for i in range(num_lower_char):
     final_string=final_string+random.choice(abc_lower)
    
    for i in range(num_num_char):
      final_string=final_string+random.choice(num_char)
    
    for i in range(num_special_char):
      final_string=final_string+random.choice(special_char)
    
    for i in arleady_used:
      if final_string==i :
        yz=get_unique_character_str(arleady_used,num_captial_char,num_lower_char,num_num_char,num_special_char)
        break
    return final_string
    
if __name__=="__main__":
  already_exist=()
  xyz=get_unique_character_str(already_exist,1,1,1,1)
  print(xyz)