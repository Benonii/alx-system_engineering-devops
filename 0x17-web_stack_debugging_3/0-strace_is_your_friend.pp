#This manifest fixes the root directory of the Apache 2 server and restarts it

$conf_file = '/etc/apache2/sites-available/000-default.conf'

exec {'fix_root_dir_path':
  command => "sed -i '12 s/$/\\/wp-content/' ${conf_file}",
  path    => ['/usr/bin/', '/bin/'],
}

exec {'restart_apache2_server':
  command => 'sudo service apache2 restart',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
