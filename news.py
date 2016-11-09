#!/usr/bin/env python

import os
import sys
import shutil

message = """
  .d8888b.                      888   888b    888
 d88P  Y88b                     888   8888b   888
 888    888                     888   88888b  888
 888        .d88b.  .d88b.  .d88888   888Y88b 888 .d88b. 888  888  888.d8888b
 888  88888d88""88bd88""88bd88" 888   888 Y88b888d8P  Y8b888  888  88888K
 888    888888  888888  888888  888   888  Y8888888888888888  888  888"Y8888b.
 Y88b  d88PY88..88PY88..88PY88b 888   888   Y8888Y8b.    Y88b 888 d88P     X88
  "Y8888P88 "Y88P"  "Y88P"  "Y88888   888    Y888 "Y8888  "Y8888888P"  88888P'
"""


def main():
    last_read_path = './.last_read_news'
    last_read = ''

    try:
        with open(last_read_path) as f:
            last_read = f.read()
    except IOError:
        pass

    root = './news'
    fnames = sorted(os.listdir(root))

    printed_message = False

    for fname in fnames:
        path = os.path.join(root, fname)
        if path > last_read:
            if not printed_message:
                print(message)
                printed_message = True
            with open(path) as news_f:
                print('\n' + '-' * 80 + '\n')
                shutil.copyfileobj(news_f, sys.stdout)

    with open('./.last_read_news', 'w') as f:
        f.write(path)


if __name__ == '__main__':
    main()
