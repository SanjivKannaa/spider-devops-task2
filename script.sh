sudo apt install apache2
cat "<proxy balancer://euniversity.edu>" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "        BalancerMember http://127.0.0.1:8081/loadfactor=40" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "        BalancerMember http://127.0.0.1:8082/loadfactor=35" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "        BalancerMember http://127.0.0.1:8083/loadfactor=25" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "        ProxySet lbmethod=bytraffic" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "</proxy>" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "ProxyPass "/site" "balancer://euniversity.edu/"" >> /etc/apache2/conf-enabled/loadbalancer.conf
cat "ProxyPassReverse "/site" "balancer://euniversity.edu/"" >> /etc/apache2/conf-enabled/loadbalancer.conf



sudo systemctl restart apache2


env -i "$BASH" -c 'python3 server1.py'
env -i "$BASH" -c 'python3 server2.py'
env -i "$BASH" -c 'python3 server3.py'



echo "please go to your browser and open 127.0.0.1"