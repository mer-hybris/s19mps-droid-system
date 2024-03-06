#!/usr/bin/python
# coding: utf-8

# Test case:
#   1. Python 2.7.6 and 3.7.1 test pass on ubuntu.
#   2. Python 2.7.1 test pass on windows.

import os,fnmatch
import struct
import mmap
import sys
import gzip
import zlib

# Reference kernel/printk/printk.c
PRINKT_LOG_STRUCT_FORMAT      = '<Q3H3BI'
PRINKT_LOG_STRUCT_SIZE = 20
TASK_COMM_LEN          = 16

DUMP_FILE = 'minidump'
KMSG_FILE = 'last_kmsg.log'
COMPRESSED_INFO = 'compress_record_file'

MSEC = 1000000000

dump_dir = os.getcwd()


def uncompress_zlib_files(dirname):
    offset = 0
    dump_files=fnmatch.filter(os.listdir(dirname), '*.zlib')
    compressed_info_files=open(os.path.join(dirname, COMPRESSED_INFO))
    for dump_file in dump_files:
        fd = open(os.path.join(dirname, dump_file), 'rb')
        dump_file_out = open(os.path.join(dirname, dump_file).rstrip('.zlib'),"wb")
        name_list1 = dump_file.split('.', 1)[0]
        compressed_info_files.seek(0)
        for line in compressed_info_files:
            line_list1 = line.split(':')[0]
            if name_list1 == line_list1:
                compressed_len_list = line_list1 = line.split(':')[1].split(' ')
                for compressed_len in compressed_len_list:
                    length = int(compressed_len)
                    if length == -1:
                        offset = 0
                        break
                    compress_block = fd.read(length)
                    uncompress_block = zlib.decompress(compress_block, 15)
                    dump_file_out.write(uncompress_block)
                    offset += length
                    fd.seek(offset)
                break
        dump_file_out.close()
        fd.close()
        os.remove(os.path.join(dirname, dump_file))

    compressed_info_files.close()


def uncompress_gzip_files():
    dump_files = fnmatch.filter(os.listdir(dump_dir), '*.gz')
    for dump_file in dump_files:
        f = gzip.open(os.path.join(dump_dir, dump_file), 'rb')
        f_out=open(os.path.join(dump_dir, dump_file).rstrip('.gz'),"w")
        file_content = f.read()
        f_out.write(file_content)
        f.close()
        f_out.close()
        os.remove(os.path.join(dump_dir, dump_file))



def merge_file():
    dump_files = fnmatch.filter(os.listdir(dump_dir), '*_minidump_*')
    if len(dump_files) == 0:
        print('Don\'t exist dump file!!!')
        return

    dump_files.sort(key = lambda x: int(x.split('_',1)[0]))
    #for item in dump_files:
    #    print item
    with open(os.path.join(dump_dir, DUMP_FILE),'wb') as outfile:
        for dump_file in dump_files:
            for line in open(os.path.join(dump_dir, dump_file), 'rb'):
                outfile.write(line)


def parse_kmsg():
    parse_str = ('python parse_log_buf_k54.py')
    if len(sys.argv) == 2:
        parse_str = 'python parse_log_buf_k54.py' + ' ' + dump_dir

    os.system(parse_str)

def generate_elfhdr():
    parse_str = ('python generate_elfhdr_for_mini_v1.0.py')
    if len(sys.argv) == 2:
        parse_str = 'python generate_elfhdr_for_mini_v1.0.py' + ' ' + dump_dir

    os.system(parse_str)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        dump_dir = sys.argv[1]
    for dirpath, dirnames, filenames in os.walk(dump_dir):
        for dirname in dirnames:
            j = os.path.join(dirpath, dirname)
            os.chdir(j)
            i = os.getcwd()
            print(i)
            uncompress_zlib_files(i)
    #generate_elfhdr()
    #parse_kmsg()
    #merge_file()


