## Steps to create an image from OpenStack instance
0) RUN, source /etc/kolla/kolla-toolbox/admin-openrc.sh
1) openstack server list
2) openstack server stop <instance_name>
3) nova image-create --poll <instance_name> <instance_name_snapshot>
4) glance image-download --file <image_name>.qcow2 <UUID_of_snapshot>
5) Get UUID_of_snapshot using \"glance image-list\"
6) Upload new image on to Glance, \"openstack image create sriov1 --public --container-format bare --disk-format qcow2 --file <image_name>.qcow2\"
