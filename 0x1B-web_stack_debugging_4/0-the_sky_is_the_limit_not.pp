#!/usr/bin/env ruby
# Raises the file limit to accomodate the number of connections

exec { 'raise_defalut':
  command => 'sed -i "s/-n .*/-n 4096\"/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}
