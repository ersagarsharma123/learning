list_d=[]
dict_d={}
set_d=set({})
int_d=5
char_d='a'
float_d=2.5
bool_d=bool()
tuple_d= tuple()
complex_d=5+3j

#lambda function
get_methods = lambda data_type: [i for i in dir(data_type) if not i.startswith('__')]

print("list_methods=", get_methods(list_d),',', len(get_methods(list_d)),end='\n\n')
print("dict_methods=",get_methods(dict_d),',', len(get_methods(dict_d)), end='\n\n')
print("set_methods=",get_methods(set_d),',', len(get_methods(set_d)), end='\n\n')
print("int_methods=",get_methods(int_d),',', len(get_methods(int_d)), end='\n\n')
print("char_methods=",get_methods(char_d),',', len(get_methods(char_d)), end='\n\n')
print("float_methods=",get_methods(float_d),',', len(get_methods(float_d)), end='\n\n')
print("boolean_methods=",get_methods(bool_d),',', len(get_methods(bool_d)), end='\n\n')
print("tuple_methods=",get_methods(tuple_d),',', len(get_methods(tuple_d)), end='\n\n')
print("complex_number_methods=",get_methods(complex_d),',', len(get_methods(complex_d)))

list_methods = ['append', 'extend', 'insert', 'copy', 'clear', 'pop', 'remove', 'index ', 'count', 'reverse', 'sort'] , 11


dict_methods = ['copy', 'update', 'setdefault', 'pop', 'popitem', 'clear', 'fromkeys', 'get', 'items', 'keys', 'values'] , 11

set_methods= ['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 
              'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'] , 17

tuple_methods= ['count', 'index'] , 2

int_methods= ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'] , 10

string_methods= ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
               'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
               'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
               'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] , 47

float_methods= ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real'] , 7

boolean_methods= ['as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'] , 10

complex_number_methods= ['conjugate', 'imag', 'real'] , 3

print('hello')