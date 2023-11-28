# Deos the same thing in task 2 except in puppet

file { '/root/alx-system_engineering-devops/0x0B-ssh/2-ssh_config':
  ensure  => file,
  content => "Host 75667-web-01\n\
              HostName 100.25.109.172\n\
              User ubuntu\n\
              IdentityFile ~/.ssh/school\n\
              PasswordAuthentication no\n",
}
