#!/usr/bin/env python3

import re

class Wiki_Parser:
  def _inner_link_parse(self, m):
    ''' parse link wiki markup tag to html tag'''
    groups = m.groups()
    ip_name = groups[0].strip()
    #to-do: generate a unique ip address against ip_name
    ip_addr = ip_name

    if groups[2]:
      display_name = groups[2].strip()
    else:
      display_name = ip_name

    return '<a href="' + ip_name + '">' + display_name + '</a>'

  def _outter_link_parse(self, m):
    ''' parse wiki markup tag of link into html tag'''
    groups = m.groups()
    ip_addr = groups[1].strip()
    if groups[3]:
      display_name = groups[3].strip()
    else:
      display_name = ip_addr
    return '<a href="' + ip_addr + '">' + display_name + '</a>'

  def _header_parse(self, value):
    s = value
    i = j = 0
    for e in s:
      if e == '=':
        i += 1
      else:
        break
    for e in s[::-1]:
      if e == '=':
        j += 1
      else:
        break
    level = min(i, j)
    value = s[level:-level].strip()
    if level == len(s) or value == '':
      return s
    else:
      return '<h' + str(level) + '>' + value + '</h' + str(level) + '>'

  def replace(self, m):
    iter = filter(lambda t: t[1] != None, m.groupdict().items())
    tag_type, value = next(iter)
    print(tag_type)
    f = getattr(self, "_" + tag_type + "_parse")
    return f(value)


  def parse(self, text):
    inner_link_re = r'(?P<inner_link>^\[{2}(.*?)(\|(.*?)\[{2}$)'
    outter_link_re = r'(?P<outter>^\[([^\[].*?)(\s+(.*?))?\]$)'
    header_re = r'(?P<header>^=.*?=$)'

    re_list = [outter_link_re, header_re]
    regex = r"|".join(re_list)
    print("regex: " + regex)
    result = ""
    for line in text.split("\n"):
      result += re.sub(regex, self.replace, line)
    return result


if __name__ == '__main__':
  ''' just for test '''
  s = "===hello==="
  parser = Wiki_Parser()
  t = parser.parse(s)
  print(t)

