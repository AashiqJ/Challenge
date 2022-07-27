import boto3
import json
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')
val = input("Enter your instance id: ")
instance = ec2.Instance(val)

# Store all the metadata values.
data = {}
data['ami-id'] = instance.image_id
data['instance-id'] = instance.id
data['instance-type'] = instance.instance_type
data['local-hostname'] = instance.private_dns_name
data['local-ipv4'] = instance.private_ip_address
data['placement'] = instance.placement
data['public-hostname'] = instance.public_dns_name
data['public-ipv4'] = instance.public_ip_address
data['keyname'] = instance.id
data['security-groups'] = instance.security_groups
json_data = json.dumps(data)
print("Json output:")
print(data)

# Funtion for displaying Dict in a nice format.
def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():
        print("{} ({})".format(item, amount))

# Dict with all the metadata keys.
metadata = {
'1':'ami_launch_index',
'2':'architecture',
'3':'block_device_mappings',
'4':'capacity_reservation_id',
'5':'capacity_reservation_specification',
'6':'client_token',
'7':'cpu_options',
'8':'ebs_optimized',
'9':'elastic_gpu_associations',
'10':'elastic_inference_accelerator_associations',
'11':'ena_support',
'12':'hibernation_options',
'13':'hypervisor',
'14':'iam_instance_profile',
'15':'image_id',
'16':'instance_id',
'17':'instance_lifecycle',
'18':'instance_type',
'19':'kernel_id',
'20':'key_name',
'21':'launch_time',
'22':'licenses',
'23':'metadata_options',
'24':'monitoring',
'25':'network_interfaces_attribute',
'26':'outpost_arn',
'27':'placement',
'28':'platform',
'29':'private_dns_name',
'30':'private_ip_address',
'31':'product_codes',
'32':'public_dns_name',
'33':'public_ip_address',
'34':'ramdisk_id',
'35':'root_device_name',
'36':'root_device_type',
'37':'security_groups',
'38':'source_dest_check',
'39':'spot_instance_request_id',
'40':'sriov_net_support',
'41':'state',
'42':'state_reason',
'43':'state_transition_reason',
'44':'subnet_id',
'45':'tags',
'46':'virtualization_type',
'47':'vpc_id'
}

# Get user input to display specific metadata value.
while True:
  print_inventory(metadata)
  inp = input("Please enter the required number ")
  value="instance."+metadata[inp]
  print(eval(value))
