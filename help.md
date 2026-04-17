validate_func_output =  {'ok': True, 'value': {'mode': 'encode', 'raw_input': 'hello', 'input_kind': 'text'}, 'error': None}
normalize_func_output = {'ok': True, 'mode': 'encode', 'data_bytes': b'hello', 'data_len': 5}

['011010', '000110', '010101', '101100', '011011', '00']

groups file -> return = {'ok': True, 'bit_stream_length': 24, 'missing_bits': 0, 'six_bit_groups': ['011010', '000110', '010101', '101100']}

base64 input = {'ok': True, 'bit_stream_length': 40, 'missing_bits': 2, 'six_bit_groups': ['011010', '000110', '010101', '101100', '011011', '000110', '111100']} 5