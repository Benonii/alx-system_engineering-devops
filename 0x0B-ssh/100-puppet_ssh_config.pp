# Deos the same thing in task 2 except in puppet

file { 2-ssh_config:
  ensure  => file,
  content => "Host 75667-web-01\n\
  	      HostName 34.229.186.0\n\
  	      User ubuntu\n\
  	      IdentityFile ~/.ssh/school\n\
  	      PasswordAuthentication no\n",
  require => File['~/.ssh/school'].
}
