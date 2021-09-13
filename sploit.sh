#!/bin/bash
$(iconv -f utf-8 -t utf-16be < xxe.xml > xxe-utf-16.xml)

$(iconv -f utf-8 -t utf-16be < dtd.xml > dtd-utf-16.xml)