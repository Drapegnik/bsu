#!/usr/bin/env bash
echo '## 6. `netstat`'
echo ' * `netstat -p TCP`'
echo '```'
netstat -p TCP
echo '```'

echo ' * `netstat -n -p TCP`'
echo '```'
netstat -p -n TCP
echo '```'

echo -e ' * `netstat –a –s –r`\n\n'
echo '`netstat -r` - Show the routing tables.  Use with `-a` to show protocol-cloned routes.  When `-s` is also present, show routing statistics instead'
echo '```'
netstat –a –s –r
echo '```'