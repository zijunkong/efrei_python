variable_exist = 10 
variable_detection = locals().get('variable_existe', 42)
print(variable_detection)
