"""
This script creates a binary file api.bin, which is used to obscure an API key from a public git repo.
"""

import io


api_key = "cdbdcf2a3637d830a4b8541a4f6c72c2c730feb60339216d2d5dc51c35f8cd7d"
f = open('api.bin', 'wb')
str_bytes = api_key.encode()
f.write(str_bytes)
f.close()
