#!/usr/bin/env ruby
# Raises the file limit to accomodate the number of connections

exec { 'raise_default':
  command => 'sed -i "s/-n .*/-n 5012\"/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

exec { 'reload_nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
