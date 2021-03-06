import FDFSPythonClient as fdfs
import time
import sys

r = fdfs.init('/etc/fdfs/client.conf', log_level=7, log_fd=sys.stderr.fileno())

if r != 0:
    exit()

print('Upload normal file:')

# read pic content
with open('test.jpg', 'rb') as f:
    file_buff = f.read()

# send normal picture
start = time.perf_counter()

r = fdfs.upload_file(file_buff, 'jpg')

elapsed = time.perf_counter() - start

print('Response:', r)
print('Time Elapsed %f ms.' % (elapsed * 1000))

if r[0] != 0:
    exit()

print()
print('Upload slave file:')

# send slave pic
master_file_id = r[1]
prefix_name = '_1280x800'
file_ext_name = 'jpg'

start = time.perf_counter()

r = fdfs.upload_slave(file_buff, master_file_id, prefix_name, file_ext_name)

elapsed = time.perf_counter() - start

print('Response:', r)
print('Time Elapsed %f ms.' % (elapsed * 1000))

fdfs.destroy()
