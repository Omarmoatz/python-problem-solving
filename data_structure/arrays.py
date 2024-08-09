# Arrays : its same as list but all the elements in it should be with the same data type
# we use Array only when we want to optimze our software 
#       if we use a large groupe of data because Array is more faster than list
from array import array

nums = array('i', [1, 2, 3, 4])


nums.append(5)
# also i can do all list functions with the array
# nums.append('omar')   --> Error: because its not the same data type
nums[0] = 10
# nums[0] = 10.5        --> Error: because its not the same data typen
print(nums)



# Type_code   C_Type   Python_Type  Minimum_size_in_bytes

# 'b'       signed_char       int             1

# 'B'       unsigned_char     int             1

# 'u'       wchar_t       Unicode_character   2

# 'h'       signed_short      int             2

# 'H'       unsigned_short    int             2

# 'i'       signed_int        int             2

# 'I'       unsigned_int      int             2

# 'l'       signed_long       int             4

# 'L'       unsigned_long     int             4

# 'q'       signed_long_long  int             8

# 'Q'       unsigned_long_long int            8

# 'f'         float           float           4

# 'd'         double          float           8
