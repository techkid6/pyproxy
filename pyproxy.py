#!/usr/bin/env python

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
from proxy.logging import Logger
from proxy.HTTPProxy import HTTPProxy

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

    try:
        args = arg_parser.parse_args()
    except IOError:
        # Temporary logger because we haven't set up the initial one yet
        Logger(False).severe('Error finding plugin file, exiting')
        exit(1)


    args_iter = vars(args)

    logger = Logger(args_iter['verbose'])
    for arg in args_iter:
        logger.debug('%s: %s' % (arg, args_iter[arg]))

    plugin = None

    if args_iter['plugin'] is not None:
        if args_iter['plugin'].name.endswith('.py'):
            plugin_name = args_iter['plugin'].name.replace('/', '.')[:-3]
            logger.info("Loading plugin: %s" % plugin_name)
            try:
                plugin = __import__(plugin_name)
            except IOError:
                logger.severe('Failed to load %s' % plugin_name)
                exit(1)

    logger.info('Starting proxy')
    proxy = HTTPProxy(args_iter['host'], args_iter['port'], plugin)

if __name__ == '__main__':
    main()
