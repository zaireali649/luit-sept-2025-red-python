from helpers import *


def create_instances(ec2_client, ami_type="ubuntu", instance_amount=1):
    cleaned_ami_type = ami_type.lower().strip().replace(" ", "")

    for i in range(instance_amount):
        if cleaned_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Ubuntu Created")
        elif cleaned_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Linux 2023 Created")
        elif cleaned_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Linux 2 Created")
        else:
            print("Unsupported AMI")


if __name__ == "__main__":
    ec2_client = get_ec2_client()
    create_instances(ec2_client)
    create_instances(ec2_client, ami_type="Linux 2", instance_amount=3)
    create_instances(ec2_client, ami_type="ubuntu")
    create_instances(ec2_client, ami_type="ubuNtu")
    create_instances(ec2_client, ami_type="linUx 2023")
    create_instances(ec2_client, ami_type="linUx 2023 ")
    create_instances(ec2_client, ami_type=" linUx 2023 ")
    create_instances(ec2_client, ami_type="linUx  2023 ")
