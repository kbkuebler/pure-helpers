import urllib3
from pypureclient import flasharray as fa

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to FA and create a client
# Enter the IP for the FA that you want to connect to
myTarget = '192.168.0.137'
# Create a service account that has an API key on the FA
myKey = 'c2ad97fc-6b9f-5256-dc88-27d3d8e00e4d'

try:
    c = fa.Client(target=myTarget,
                               api_token='c2ad97fc-6b9f-5256-dc88-27d3d8e00e4d')
    print("Connection Successful")
except:
    print("Cannot establish connection.")

# Get the information that we need

myVols = c.get_volumes_space().items

print(f"{'Name':80}{'Space in GB':}")
for i in myVols:
    if i.space.total_effective/1e+9 > 1:
        print(f"{i.name:80}{round(i.space.total_effective/1024/1024/1024)}")

# Or maybe something like this:

print("="*50)
print("")
hosts = [hosts.name for hosts in c.get_hosts().items]
print("="*50)
print("Let's get our first 5 hosts.")
print("")
print(hosts[0:5])

myHost = hosts[1:2]
print("")
print("="*50)
conn = [conn for conn in c.get_hosts_performance_balance(names="cisco-esx1").items]
for i in conn:
    print(i.target)
print("")
print("="*50)
print("")
conn = c.get_hosts(limit=3).items
for i in conn:
    if "cisco" in i.name:
        print(i.name, "   ",i.port_connectivity)
vname="Volume Name"
drr="Data Reduction"
vspt="Total Provisioned in GiB"
tp="Total Used in GiB"
myVols = c.get_volumes().items
print(f"{vname:30}{drr:<30}{vspt:<40}{tp:<30}")
for vol in myVols:
    if "pxclouddrive" in vol.name:
        print(f"{vol.name:30}{round(vol.space.data_reduction,2):<30}\
        {round(vol.space.total_provisioned/1024/1024/1024,2):<30}\
        {round(vol.space.total_physical/1024/1024/1024,3)}")%                  
