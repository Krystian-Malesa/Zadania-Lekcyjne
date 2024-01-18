import sys


# print(sys.argv)

# sys.path.append('/path/to')

# # sys.exit()  # wychodzenie z programu

# print(sys.version)
# print(sys.version_info) # bardziej opisuje wersje od sys.version

with open( 'output.txt' , 'w') as f:
    sys.stdout = f
    print('Hello world')

sys.stdout = sys.__stdout__

print(sys.platform)