#!/usr/bin/env/ ruby
# Removes the hard and soft file limits for holberton

exec { 'beyond_limits_hard':
  command => "sed -i '56s/^/#/' /etc/security/limits.conf",
  path    => ['/bin', 'usr/bin'],
}

exec { 'beyond_limits_soft':
  command => "sed -i '57s/^/#/' /etc/security/limits.conf",
  path    => ['/bin', 'usr/bin'],
}
