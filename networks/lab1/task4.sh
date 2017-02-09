#!/usr/bin/env bash
echo '## 4. `traceroute`'
echo ' * `traceroute -d tut.by:`'
echo '```'
traceroute -d tut.by
echo '```'
echo ' * `traceroute -m 8 onliner.by`'
echo '```'
traceroute -m 8 onliner.by
echo '```'