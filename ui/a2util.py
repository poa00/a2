# -*- coding: utf-8 -*-
"""
Misc functions - gathered from the a2core module.
This is all too random to be core.
"""
import os
import json
import time
import string
import codecs
import webbrowser
import subprocess

import a2ahk
import a2core


UTF8_CODEC = 'utf-8-sig'
JSON_INDENT = 2
ILLEGAL_NAMES = ('con prn aux nul com1 com2 com3 com4 com5 com6 com7 com8 com9 lpt1 lpt2 lpt3 '
                 'lpt4 lpt5 lpt6 lpt7 lpt8 lpt9'.split())
ALLOWED_CHARS = string.ascii_letters + string.digits + '_-.'
EXPLORER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')


def standard_name_check(NAME, black_list=None, black_list_msg='Name "%s" already in use!'):
    name = NAME.lower()
    if NAME == '':
        return 'Name cannot be empty!'
    if name == 'a2':
        return 'You just cannot name it "a2"! Ok?'
    if name.startswith('.'):
        return 'Names starting with a dot would be ignored!'
    if black_list is not None and name in black_list:
        return black_list_msg % name
    if any([(l in string.whitespace) for l in name]):
        return 'Name cannot have whitespace! Use _ or - insead!'
    if not all([(l in ALLOWED_CHARS) for l in name]):
        return 'Name can only have letters, digits and "_.-"'
    if name in ILLEGAL_NAMES:
        return 'Name cannot be reserved OS device name!'
    if not any([(l in string.ascii_letters) for l in name]):
        return 'Have at least 1 letter in the name!'
    return True


def get_cfg_default_name(cfg):
    """

    :param dict cfg: Element configuration dictionary.
    :rtype: str
    """
    cfg_name = cfg.get('name', cfg.get('typ'))
    if cfg_name is None:
        raise RuntimeError('Could not find name for config piece!\n'
                           'Make sure "name" or "typ" is given in the config dict!')
    return cfg_name


def get_next_free_number(name, name_list, separator=''):
    """
    Browses a list of names to find a free new version of the given name + integer number.
    Just returns the name if its not even in the name_list. Otherwise the first next will be 2.

    Example:

        name = 'trumpet'
        name_list = ['swamp', 'noodle']
        result: 'trumpet'

        name = 'bob'
        name_list = ['bob', 'alice', 'bob 2', 'bob 4']
        result: 'bob 3'

    :param str name: Base name to look up in the list
    :param iterable name_list: List to look for instances of "name"
    :param str separator: string to put between the initial name and the integer number.
    :rtype: str
    """
    if name not in name_list:
        return name

    number = 2
    try_name = name + separator + str(number)

    while try_name in name_list:
        number += 1
        try_name = name + separator + str(number)

    return try_name


def json_read(path):
    with codecs.open(path, encoding=UTF8_CODEC) as fobj:
        return json.load(fobj)


def json_write(path, data):
    with codecs.open(path, 'w', encoding=UTF8_CODEC) as fobj:
        json.dump(data, fobj, indent=JSON_INDENT, sort_keys=True)


def get_date():
    now = time.localtime()
    return '%i %i %i' % (now.tm_year, now.tm_mon, now.tm_mday)


def set_windows_startup(state=True):
    """
    might be doable via python but this is just too easy with AHKs A_Startup
    """
    a2ahk.call_lib_cmd('set_windows_startup', a2core.A2Obj.inst().paths.a2, int(state))


def surf_to(url):
    if url:
        webbrowser.get().open(url)


def load_utf8(path):
    """
    Opens a file with UTF8 codec to return its content in a string
    :param str path: Path to a file to load from.
    :rtype: str
    """
    with codecs.open(path, encoding=UTF8_CODEC) as fobj:
        content = fobj.read()
    return content


def write_utf8(path, content):
    """
    Opens a file path with UTF8 codec to write string content into.
    :param str path: Path to a file to write to.
    :param str content: String content for the file.
    """
    with codecs.open(path, 'w', encoding=UTF8_CODEC) as fobj:
        fobj.write(content)


def explore(path):
    """
    Opens the Windows Explorer for the given path.
    Selects the file if a file path was passed.

    :param str path: Path to a folder or file.
    """
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        args = [EXPLORER_PATH, path]
    elif os.path.isfile(path):
        args = [EXPLORER_PATH, '/select,', path]
    else:
        raise FileNotFoundError('Cannot explore to path "%s"' % path)

    subprocess.run(args)
