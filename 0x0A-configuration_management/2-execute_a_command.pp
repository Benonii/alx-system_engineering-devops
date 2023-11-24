# This manifest executes a command pkill

exec {'pkill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => 'usr/bin:/bin',
}
