# The MIT License (MIT)

# Copyright (c) 2014 Evan Markowitz

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = 'techkid6'

import argparse
from pyproxy.logging import Logger

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.description = 'A simple HTTP proxy with plugin support'

    arg_parser.add_argument('-H', '--host',    default='0.0.0.0',
                            help='The address the proxy will listen on')
    arg_parser.add_argument('-p', '--port',    default=8080,  type=int,
                            help='The port that the proxy will listen to')
    arg_parser.add_argument('-v', '--verbose', default=False, type=bool,
                            help='Show more output in the logs')
    arg_parser.add_argument('-P', '--plugin',                 type=open,
                            help='The file where your plugin is located')

    args = arg_parser.parse_args()
    args_iter = vars(args)

    logger = Logger(args_iter['verbose'])
    for arg in args_iter:
        logger.debug('%s: %s' % (arg, args_iter[arg]))

    logger.info('Starting pyproxy')
    # TODO: Start a proxy with the arguments provided


if __name__ == '__main__':
    main()
